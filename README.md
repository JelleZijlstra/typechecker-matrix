# Python Type Checker Feature Matrix

This project builds a comparison matrix for Python type checkers (`mypy`, `pyright`, `ty`, `pyrefly`) using executable samples.

## What this gives you

- Easy sample authoring (`add-sample` command + simple folder format)
- Automated matrix runs across configured checkers (`run` or `all`), for all suites or one suite
- Markdown summary table with per-checker totals (`summarize`)
- Detailed markdown report per sample with checker outputs (`summarize`)

## Layout

- `typecheckers.toml`: checker command definitions
- `samples/<suite>/<sample>/`: suite-grouped samples (`sample.toml` + `sample.py`)
- `results/run-*.json`: raw run output
- `results/summary.md`: rendered table
- `results/detailed.md`: per-sample detailed output report
- `run_matrix.py`: CLI entrypoint

## Usage

### 1) Add a sample

```bash
./run_matrix.py add-sample protocol-support \
  --suite literals \
  --feature "Protocols" \
  --description "Structural typing with Protocol" \
  --expectation accept \
  --tag protocols
```

You can also provide code inline:

```bash
./run_matrix.py add-sample typed-dict-error \
  --suite typeddict \
  --feature "TypedDict" \
  --description "Missing required key should error" \
  --expectation reject \
  --code 'from typing import TypedDict\n\nclass U(TypedDict):\n    x: int\n\nu: U = {}'
```

### 2) Discover suites

```bash
./run_matrix.py list-suites
```

Current starter suites:

- `literals`
- `sys-platform`

### 3) Run all checkers on all samples

```bash
./run_matrix.py run
```

Run one suite only:

```bash
./run_matrix.py run --suite literals
```

Or run + summarize in one step:

```bash
./run_matrix.py all --print
```

Or one suite only:

```bash
./run_matrix.py all --suite literals --print
```

### 4) Generate summary table

```bash
./run_matrix.py summarize --output results/summary.md --print
```

This also writes `results/detailed.md` by default (customizable via `--detailed-output`).

### 5) View rendered markdown in browser

```bash
./serve_reports.py --host 127.0.0.1 --port 8000 --root .
```

Then open:

- `http://127.0.0.1:8000/` for the markdown index
- `http://127.0.0.1:8000/view?path=results/summary.md` for a specific file

## Checker configuration

Edit `typecheckers.toml` to adjust command templates. `{sample}` is replaced with the path to each sample:

```toml
[[checker]]
name = "mypy"
command = ["mypy", "{sample}"]
```

If a checker executable is missing, that checker is marked `⚪ unavailable` instead of failing the run.

## Output semantics

For each sample and checker:

- `✅ supported`: checker behavior matches sample expectation
- `❌ unsupported`: checker behavior does not match expectation
- `⚪ unavailable`: checker command not installed/found
- `⚠️ error`: timeout or runtime execution issue
