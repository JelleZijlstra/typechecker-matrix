# AGENTS.md

## Environment
- Always use the local virtual environment: `source .venv/bin/activate`.
- Run commands from the repo root.

## Core Commands
- Run all suites: `python run_matrix.py all`
- Run one suite: `python run_matrix.py all --suite <suite-name>`
- Regenerate reports from latest run: `python run_matrix.py summarize`
- Start report viewer: `python serve_reports.py --host 127.0.0.1 --port 8000 --root .`

## Sample Conventions
- Samples live at `samples/<suite>/<sample-id>/`.
- Each sample requires:
  - `sample.toml`
  - `sample.py`
- Keep sample IDs feature-focused and concise.
- For `sys.platform` experiments, prefer the existing style used in this repo:
  - branch-local typed `x` assignments
  - post-conditional check `y: int = x`

## Reports
- Summary output: `results/summary.md`
- Detailed output: `results/detailed.md`
- Detailed report is the source of truth for checker diagnostics.

## Quality Bar
- After changing samples or runner logic, rerun `python run_matrix.py all`.
- Ensure both summary and detailed reports are regenerated.
