from __future__ import annotations

import dataclasses
import datetime as dt
import json
import shutil
import subprocess
import time
import tomllib
from pathlib import Path
from typing import Literal

Expectation = Literal["accept", "reject"]
Status = Literal["supported", "unsupported", "error", "unavailable"]


@dataclasses.dataclass(slots=True)
class Sample:
    suite: str
    id: str
    feature: str
    description: str
    expectation: Expectation
    tags: list[str]
    path: Path


@dataclasses.dataclass(slots=True)
class Checker:
    name: str
    command: list[str]


@dataclasses.dataclass(slots=True)
class CheckerResult:
    checker: str
    status: Status
    return_code: int | None
    duration_ms: int
    stdout: str
    stderr: str
    command: list[str]
    error: str | None = None


def load_checkers(config_path: Path) -> list[Checker]:
    data = tomllib.loads(config_path.read_text(encoding="utf-8"))
    out: list[Checker] = []
    for item in data.get("checker", []):
        name = str(item["name"]).strip()
        cmd = [str(part) for part in item["command"]]
        out.append(Checker(name=name, command=cmd))
    if not out:
        raise ValueError(f"No checkers found in {config_path}")
    return out


def _load_sample(sample_dir: Path, suite_name: str) -> Sample:
    meta_path = sample_dir / "sample.toml"
    code_path = sample_dir / "sample.py"
    if not meta_path.exists() or not code_path.exists():
        raise ValueError(f"Sample dir must contain sample.toml and sample.py: {sample_dir}")

    meta = tomllib.loads(meta_path.read_text(encoding="utf-8"))
    expectation = str(meta["expectation"]).strip()
    if expectation not in {"accept", "reject"}:
        raise ValueError(f"Invalid expectation in {meta_path}: {expectation}")

    return Sample(
        suite=suite_name,
        id=str(meta["id"]).strip(),
        feature=str(meta["feature"]).strip(),
        description=str(meta["description"]).strip(),
        expectation=expectation,
        tags=[str(x).strip() for x in meta.get("tags", [])],
        path=code_path,
    )


def _visible_dirs(path: Path) -> list[Path]:
    return sorted([p for p in path.iterdir() if p.is_dir() and not p.name.startswith(".")])


def discover_suites(samples_dir: Path) -> list[str]:
    return [p.name for p in _visible_dirs(samples_dir)]


def load_samples(samples_dir: Path, suite: str | None = None) -> list[Sample]:
    suites = discover_suites(samples_dir)
    if suite is not None:
        if suite.startswith("."):
            raise ValueError(f"Invalid suite name: {suite}")
        if suite not in suites:
            raise FileNotFoundError(f"Suite not found: {suite}")
        suites = [suite]

    out: list[Sample] = []
    for suite_name in suites:
        suite_dir = samples_dir / suite_name
        sample_dirs = _visible_dirs(suite_dir)
        out.extend(_load_sample(sample_dir, suite_name=suite_name) for sample_dir in sample_dirs)

    seen: set[str] = set()
    for sample in out:
        key = f"{sample.suite}/{sample.id}"
        if key in seen:
            raise ValueError(f"Duplicate sample id in suite: {key}")
        seen.add(key)
    return out


def _normalize_support(expectation: Expectation, return_code: int) -> Status:
    checker_accepts = return_code == 0
    if expectation == "accept":
        return "supported" if checker_accepts else "unsupported"
    return "supported" if not checker_accepts else "unsupported"


def run_checker(checker: Checker, sample: Sample, timeout_s: int) -> CheckerResult:
    executable = checker.command[0]
    if shutil.which(executable) is None:
        return CheckerResult(
            checker=checker.name,
            status="unavailable",
            return_code=None,
            duration_ms=0,
            stdout="",
            stderr="",
            command=checker.command,
            error=f"Executable not found: {executable}",
        )

    cmd = [part.replace("{sample}", str(sample.path)) for part in checker.command]
    start = time.perf_counter()
    try:
        proc = subprocess.run(
            cmd,
            text=True,
            capture_output=True,
            timeout=timeout_s,
            check=False,
        )
        duration_ms = int((time.perf_counter() - start) * 1000)
        status = _normalize_support(sample.expectation, proc.returncode)
        return CheckerResult(
            checker=checker.name,
            status=status,
            return_code=proc.returncode,
            duration_ms=duration_ms,
            stdout=proc.stdout,
            stderr=proc.stderr,
            command=cmd,
        )
    except subprocess.TimeoutExpired as exc:
        duration_ms = int((time.perf_counter() - start) * 1000)
        return CheckerResult(
            checker=checker.name,
            status="error",
            return_code=None,
            duration_ms=duration_ms,
            stdout=exc.stdout or "",
            stderr=exc.stderr or "",
            command=cmd,
            error=f"Timeout after {timeout_s}s",
        )


def run_matrix(checkers: list[Checker], samples: list[Sample], timeout_s: int) -> dict:
    started_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    rows: list[dict] = []
    for sample in samples:
        results = [run_checker(checker, sample, timeout_s=timeout_s) for checker in checkers]
        rows.append(
            {
                "sample": {
                    "suite": sample.suite,
                    "id": sample.id,
                    "feature": sample.feature,
                    "description": sample.description,
                    "expectation": sample.expectation,
                    "tags": sample.tags,
                    "path": str(sample.path),
                    "code": sample.path.read_text(encoding="utf-8"),
                },
                "results": [dataclasses.asdict(result) for result in results],
            }
        )

    return {
        "schema_version": 1,
        "started_at": started_at,
        "suites": sorted({sample.suite for sample in samples}),
        "checkers": [dataclasses.asdict(c) for c in checkers],
        "rows": rows,
    }


def write_run(result: dict, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    ts = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    out_path = output_dir / f"run-{ts}.json"
    out_path.write_text(json.dumps(result, indent=2), encoding="utf-8")
    return out_path


def latest_run_path(output_dir: Path) -> Path:
    runs = sorted(output_dir.glob("run-*.json"))
    if not runs:
        raise FileNotFoundError(f"No run files found in {output_dir}")
    return runs[-1]


def summarize(run_data: dict) -> str:
    checker_names = [checker["name"] for checker in run_data["checkers"]]
    suites = run_data.get("suites", [])
    show_suite_col = len(suites) > 1

    lines = [
        "# Python Type Checker Feature Matrix",
        "",
        f"Generated: {run_data['started_at']}",
        "",
        "Suites: " + ", ".join(run_data.get("suites", [])),
        "",
        "Legend: ✅ supported, ❌ unsupported, ⚪ unavailable, ⚠️ error",
        "",
    ]

    header = ["Feature", *checker_names]
    if show_suite_col:
        header = ["Suite", *header]
    sep = ["---"] * len(header)
    lines.append("| " + " | ".join(header) + " |")
    lines.append("| " + " | ".join(sep) + " |")

    status_icon = {
        "supported": "✅",
        "unsupported": "❌",
        "unavailable": "⚪",
        "error": "⚠️",
    }

    for row in run_data["rows"]:
        sample = row["sample"]
        result_by_checker = {r["checker"]: r for r in row["results"]}
        cells = [sample["feature"]]
        if show_suite_col:
            cells = [sample.get("suite", ""), *cells]
        for checker in checker_names:
            result = result_by_checker[checker]
            icon = status_icon.get(result["status"], "?")
            cells.append(icon)
        lines.append("| " + " | ".join(cells) + " |")

    lines.append("")
    lines.append("## Totals")
    lines.append("")

    counts: dict[str, dict[str, int]] = {
        name: {"supported": 0, "unsupported": 0, "unavailable": 0, "error": 0}
        for name in checker_names
    }

    for row in run_data["rows"]:
        for result in row["results"]:
            counts[result["checker"]][result["status"]] += 1

    lines.append("| Checker | ✅ supported | ❌ unsupported | ⚪ unavailable | ⚠️ error |")
    lines.append("| --- | --- | --- | --- | --- |")
    for checker in checker_names:
        c = counts[checker]
        lines.append(
            f"| {checker} | {c['supported']} | {c['unsupported']} | {c['unavailable']} | {c['error']} |"
        )

    lines.append("")
    return "\n".join(lines)


def summarize_detailed(run_data: dict) -> str:
    lines = [
        "# Python Type Checker Detailed Report",
        "",
        f"Generated: {run_data['started_at']}",
        "",
        "Suites: " + ", ".join(run_data.get("suites", [])),
        "",
    ]

    for row in run_data["rows"]:
        sample = row["sample"]
        sample_label = f"{sample.get('suite', '')}/{sample['id']}".strip("/")
        lines.append(f"## {sample_label}")
        lines.append("")
        lines.append(f"- Feature: `{sample['feature']}`")
        lines.append(f"- Description: {sample['description']}")
        lines.append(f"- Expectation: `{sample['expectation']}`")
        lines.append(f"- Path: `{sample['path']}`")
        lines.append("")
        lines.append("### Sample Code")
        lines.append("")
        lines.append("```python")
        lines.append(sample.get("code", "").rstrip())
        lines.append("```")
        lines.append("")

        for result in row["results"]:
            lines.append(f"### {result['checker']}")
            lines.append("")
            lines.append(f"- Status: `{result['status']}`")
            lines.append(f"- Return code: `{result['return_code']}`")
            lines.append(f"- Duration (ms): `{result['duration_ms']}`")
            lines.append(f"- Command: `{' '.join(result['command'])}`")
            if result.get("error"):
                lines.append(f"- Error: `{result['error']}`")
            lines.append("")
            lines.append("#### stdout")
            lines.append("")
            lines.append("```text")
            lines.append((result.get("stdout") or "").rstrip() or "(empty)")
            lines.append("```")
            lines.append("")
            lines.append("#### stderr")
            lines.append("")
            lines.append("```text")
            lines.append((result.get("stderr") or "").rstrip() or "(empty)")
            lines.append("```")
            lines.append("")

    return "\n".join(lines)


def write_summary(markdown: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(markdown, encoding="utf-8")
    return output_path
