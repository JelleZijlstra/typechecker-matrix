#!/usr/bin/env python3
from __future__ import annotations

import argparse
import html
import os
import posixpath
import re
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse


def _inline(text: str) -> str:
    escaped = html.escape(text, quote=False)
    return re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)


def render_markdown(source: str) -> str:
    lines = source.splitlines()
    out: list[str] = []
    i = 0
    in_code = False
    code_lang = ""
    in_ul = False
    in_ol = False
    in_table = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_table() -> None:
        nonlocal in_table
        if in_table:
            out.append("</tbody></table>")
            in_table = False

    while i < len(lines):
        line = lines[i]

        if line.startswith("```"):
            close_lists()
            close_table()
            if in_code:
                out.append("</code></pre>")
                in_code = False
                code_lang = ""
            else:
                code_lang = line[3:].strip()
                cls = f' class="language-{html.escape(code_lang)}"' if code_lang else ""
                out.append(f"<pre><code{cls}>")
                in_code = True
            i += 1
            continue

        if in_code:
            out.append(html.escape(line))
            i += 1
            continue

        if not line.strip():
            close_lists()
            close_table()
            i += 1
            continue

        table_match = "|" in line and line.strip().startswith("|") and line.strip().endswith("|")
        if table_match:
            if i + 1 < len(lines):
                sep = lines[i + 1].strip()
                if re.fullmatch(r"\|[\s:|\-]+\|", sep):
                    close_lists()
                    close_table()
                    headers = [c.strip() for c in line.strip().strip("|").split("|")]
                    out.append("<table><thead><tr>")
                    for h in headers:
                        out.append(f"<th>{_inline(h)}</th>")
                    out.append("</tr></thead><tbody>")
                    in_table = True
                    i += 2
                    continue
            if in_table:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                out.append("<tr>")
                for c in cells:
                    out.append(f"<td>{_inline(c)}</td>")
                out.append("</tr>")
                i += 1
                continue

        close_table()

        heading = re.match(r"^(#{1,6})\s+(.*)$", line)
        if heading:
            close_lists()
            level = len(heading.group(1))
            out.append(f"<h{level}>{_inline(heading.group(2).strip())}</h{level}>")
            i += 1
            continue

        ul = re.match(r"^\s*-\s+(.*)$", line)
        if ul:
            if in_ol:
                out.append("</ol>")
                in_ol = False
            if not in_ul:
                out.append("<ul>")
                in_ul = True
            out.append(f"<li>{_inline(ul.group(1))}</li>")
            i += 1
            continue

        ol = re.match(r"^\s*\d+\.\s+(.*)$", line)
        if ol:
            if in_ul:
                out.append("</ul>")
                in_ul = False
            if not in_ol:
                out.append("<ol>")
                in_ol = True
            out.append(f"<li>{_inline(ol.group(1))}</li>")
            i += 1
            continue

        close_lists()
        out.append(f"<p>{_inline(line.strip())}</p>")
        i += 1

    close_lists()
    close_table()
    if in_code:
        out.append("</code></pre>")
    return "\n".join(out)


def _safe_relpath(root: Path, candidate: str) -> Path | None:
    raw = unquote(candidate).replace("\\", "/")
    normalized = posixpath.normpath(raw).lstrip("/")
    if normalized.startswith("../"):
        return None
    path = (root / normalized).resolve()
    try:
        path.relative_to(root.resolve())
    except ValueError:
        return None
    return path


def discover_markdown(root: Path) -> list[Path]:
    return sorted(
        p
        for p in root.rglob("*.md")
        if ".git" not in p.parts and "__pycache__" not in p.parts and ".mypy_cache" not in p.parts
    )


def make_handler(root: Path) -> type[BaseHTTPRequestHandler]:
    class Handler(BaseHTTPRequestHandler):
        def _send_html(self, body: str, status: int = 200) -> None:
            payload = (
                "<!doctype html><html><head><meta charset='utf-8'>"
                "<meta name='viewport' content='width=device-width, initial-scale=1'>"
                "<title>Markdown Viewer</title>"
                "<style>"
                "body{font-family:ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,sans-serif;"
                "margin:2rem auto;max-width:1100px;padding:0 1rem;line-height:1.5;color:#1f2937;}"
                "a{color:#0f766e;text-decoration:none}a:hover{text-decoration:underline}"
                "code{background:#f3f4f6;padding:.1rem .3rem;border-radius:4px;font-family:ui-monospace,Menlo,monospace}"
                "pre{background:#f8fafc;color:#0f172a;padding:1rem;border-radius:8px;overflow:auto;border:1px solid #dbe3ea}"
                "pre code{background:transparent;padding:0;border-radius:0;color:inherit}"
                "table{border-collapse:collapse;width:100%;margin:1rem 0}th,td{border:1px solid #d1d5db;padding:.5rem;text-align:left}"
                "th{background:#f3f4f6}ul,ol{padding-left:1.2rem}.meta{color:#6b7280;font-size:.95rem}"
                "</style></head><body>"
                f"{body}</body></html>"
            ).encode("utf-8")
            self.send_response(status)
            self.send_header("Content-Type", "text/html; charset=utf-8")
            self.send_header("Content-Length", str(len(payload)))
            self.end_headers()
            self.wfile.write(payload)

        def _home(self) -> None:
            files = discover_markdown(root)
            items = []
            for path in files:
                rel = path.relative_to(root).as_posix()
                href = "/view?path=" + quote(rel)
                items.append(f"<li><a href='{href}'>{html.escape(rel)}</a></li>")
            body = (
                "<h1>Markdown Reports</h1>"
                f"<p class='meta'>Root: <code>{html.escape(str(root))}</code></p>"
                "<p>Click a file to view a rendered version.</p>"
                + ("<ul>" + "".join(items) + "</ul>" if items else "<p>No markdown files found.</p>")
            )
            self._send_html(body)

        def _view(self, rel_path: str) -> None:
            path = _safe_relpath(root, rel_path)
            if path is None or not path.exists() or path.suffix.lower() != ".md":
                self._send_html("<h1>Not found</h1><p>Invalid markdown path.</p>", status=404)
                return
            raw = path.read_text(encoding="utf-8")
            rendered = render_markdown(raw)
            rel = path.relative_to(root).as_posix()
            body = (
                f"<p><a href='/'>Back to index</a></p><h1>{html.escape(rel)}</h1>"
                f"<p class='meta'>File: <code>{html.escape(str(path))}</code></p>"
                f"{rendered}"
            )
            self._send_html(body)

        def do_GET(self) -> None:
            parsed = urlparse(self.path)
            if parsed.path == "/":
                self._home()
                return
            if parsed.path == "/view":
                query = parse_qs(parsed.query)
                rel = query.get("path", [""])[0]
                self._view(rel)
                return
            self._send_html("<h1>Not found</h1>", status=404)

        def log_message(self, format: str, *args: object) -> None:
            return

    return Handler


def main() -> int:
    parser = argparse.ArgumentParser(description="Serve rendered markdown files in a browser.")
    parser.add_argument("--host", default="127.0.0.1", help="Bind host")
    parser.add_argument("--port", type=int, default=8000, help="Bind port")
    parser.add_argument("--root", default=".", help="Directory to scan for markdown files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    os.chdir(root)
    server = ThreadingHTTPServer((args.host, args.port), make_handler(root))
    print(f"Serving markdown from {root}")
    print(f"Open http://{args.host}:{args.port}/")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
