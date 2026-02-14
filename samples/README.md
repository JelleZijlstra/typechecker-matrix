# Samples

Samples are grouped by suite:

- `samples/<suite>/<sample-id>/sample.toml`
- `samples/<suite>/<sample-id>/sample.py`

Each sample directory contains:

- `sample.toml`: metadata used in reports.
- `sample.py`: Python code to type-check.

`sample.toml` format:

```toml
id = "unique-id"
feature = "Feature name"
description = "What this verifies"
expectation = "accept" # or "reject"
tags = ["optional", "labels"]
```

`expectation` meaning:

- `accept`: checker should return success (`exit code 0`).
- `reject`: checker should return a type error (`non-zero exit code`).
