from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

from .core import (
    discover_suites,
    latest_run_path,
    load_checkers,
    load_samples,
    run_matrix,
    summarize,
    summarize_detailed,
    write_run,
    write_summary,
)


def _slugify(raw: str) -> str:
    slug = re.sub(r"[^a-zA-Z0-9]+", "-", raw.strip().lower()).strip("-")
    if not slug:
        raise ValueError("Sample id cannot be empty")
    return slug


def cmd_add_sample(args: argparse.Namespace) -> int:
    suite = _slugify(args.suite)
    sample_id = _slugify(args.id)
    sample_dir = Path(args.samples_dir) / suite / sample_id
    if sample_dir.exists():
        raise FileExistsError(f"Sample already exists: {sample_dir}")

    sample_dir.mkdir(parents=True)
    meta = (
        f'id = "{sample_id}"\n'
        f'feature = "{args.feature}"\n'
        f'description = "{args.description}"\n'
        f'expectation = "{args.expectation}"\n'
        f'tags = {json.dumps(args.tags)}\n'
    )
    (sample_dir / "sample.toml").write_text(meta, encoding="utf-8")

    code = args.code
    if code is None:
        code = (
            "# Fill in this sample with the exact typing behavior you want to test.\n"
            "# expectation = 'accept' means the checker should succeed.\n"
            "# expectation = 'reject' means the checker should report a type error.\n"
        )
    (sample_dir / "sample.py").write_text(code.rstrip() + "\n", encoding="utf-8")

    print(f"Created sample: {sample_dir}")
    return 0


def cmd_run(args: argparse.Namespace) -> int:
    checkers = load_checkers(Path(args.config))
    samples = load_samples(Path(args.samples_dir), suite=args.suite)
    if not samples:
        if args.suite is None:
            raise ValueError(f"No samples found in {args.samples_dir}")
        raise ValueError(f"No samples found in suite '{args.suite}'")

    run_data = run_matrix(checkers=checkers, samples=samples, timeout_s=args.timeout)
    run_path = write_run(run_data, Path(args.results_dir))
    print(f"Wrote run results: {run_path}")
    return 0


def cmd_summarize(args: argparse.Namespace) -> int:
    run_path = Path(args.run_file) if args.run_file else latest_run_path(Path(args.results_dir))
    run_data = json.loads(run_path.read_text(encoding="utf-8"))
    markdown = summarize(run_data)
    detailed_markdown = summarize_detailed(run_data)

    out_path = Path(args.output)
    detailed_out_path = Path(args.detailed_output)
    write_summary(markdown, out_path)
    write_summary(detailed_markdown, detailed_out_path)
    print(f"Wrote summary: {out_path}")
    print(f"Wrote detailed report: {detailed_out_path}")
    if args.print:
        print()
        print(markdown)
    return 0


def cmd_all(args: argparse.Namespace) -> int:
    cmd_run(args)
    summarize_args = argparse.Namespace(
        run_file=None,
        results_dir=args.results_dir,
        output=args.output,
        detailed_output=args.detailed_output,
        print=args.print,
    )
    return cmd_summarize(summarize_args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Build a Python type checker feature matrix")
    parser.add_argument("--config", default="typecheckers.toml", help="Checker config TOML path")
    parser.add_argument("--samples-dir", default="samples", help="Samples directory")
    parser.add_argument("--results-dir", default="results", help="Results directory")

    sub = parser.add_subparsers(dest="command", required=True)

    add = sub.add_parser("add-sample", help="Create a new sample")
    add.add_argument("--suite", required=True, help="Suite name, e.g. literals")
    add.add_argument("id", help="Unique sample id (used as folder name)")
    add.add_argument("--feature", required=True, help="Feature name (table row group)")
    add.add_argument("--description", required=True, help="Human-readable sample description")
    add.add_argument(
        "--expectation",
        choices=["accept", "reject"],
        required=True,
        help="Expected checker behavior for this sample",
    )
    add.add_argument("--tag", action="append", dest="tags", default=[], help="Optional tag")
    add.add_argument("--code", default=None, help="Inline Python sample content")
    add.set_defaults(func=cmd_add_sample)

    run = sub.add_parser("run", help="Run all checkers on all samples")
    run.add_argument("--suite", default=None, help="Optional suite name to run only that suite")
    run.add_argument("--timeout", type=int, default=30, help="Per-checker timeout in seconds")
    run.set_defaults(func=cmd_run)

    suites = sub.add_parser("list-suites", help="List discovered sample suites")
    suites.set_defaults(
        func=lambda args: (
            print("\n".join(discover_suites(Path(args.samples_dir)))) or 0
        )
    )

    summ = sub.add_parser("summarize", help="Render a markdown summary table")
    summ.add_argument("--run-file", default=None, help="Specific run file; defaults to latest")
    summ.add_argument("--output", default="results/summary.md", help="Output markdown path")
    summ.add_argument(
        "--detailed-output",
        default="results/detailed.md",
        help="Detailed markdown output path",
    )
    summ.add_argument("--print", action="store_true", help="Print markdown to stdout")
    summ.set_defaults(func=cmd_summarize)

    all_cmd = sub.add_parser("all", help="Run and summarize in one command")
    all_cmd.add_argument("--suite", default=None, help="Optional suite name to run only that suite")
    all_cmd.add_argument("--timeout", type=int, default=30, help="Per-checker timeout in seconds")
    all_cmd.add_argument("--output", default="results/summary.md", help="Output markdown path")
    all_cmd.add_argument(
        "--detailed-output",
        default="results/detailed.md",
        help="Detailed markdown output path",
    )
    all_cmd.add_argument("--print", action="store_true", help="Print markdown to stdout")
    all_cmd.set_defaults(func=cmd_all)

    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
