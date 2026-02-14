# Python Type Checker Feature Matrix

Generated: 2026-02-14T18:22:05+00:00

Suites: sys-platform

Legend: ✅ supported, ❌ unsupported, ⚪ unavailable, ⚠️ error

| Feature | mypy | pyright | ty | pyrefly |
| --- | --- | --- | --- | --- |
| or | ✅ | ✅ | ✅ | ✅ |
| == | ✅ | ✅ | ✅ | ✅ |
| from sys import platform | ❌ | ❌ | ✅ | ❌ |
| import sys as other_name | ❌ | ✅ | ✅ | ❌ |
| in (list) | ❌ | ❌ | ❌ | ❌ |
| in (set) | ❌ | ❌ | ❌ | ❌ |
| in (tuple) | ❌ | ❌ | ❌ | ❌ |
| != | ✅ | ✅ | ✅ | ✅ |
| startswith | ✅ | ❌ | ✅ | ✅ |
| not in (list) | ❌ | ❌ | ❌ | ❌ |
| not in (set) | ❌ | ❌ | ❌ | ❌ |
| not in (tuple) | ❌ | ❌ | ❌ | ❌ |
| reverse == | ❌ | ❌ | ✅ | ✅ |
| reverse != | ❌ | ❌ | ✅ | ✅ |

## Totals

| Checker | ✅ supported | ❌ unsupported | ⚪ unavailable | ⚠️ error |
| --- | --- | --- | --- | --- |
| mypy | 4 | 10 | 0 | 0 |
| pyright | 4 | 10 | 0 | 0 |
| ty | 8 | 6 | 0 | 0 |
| pyrefly | 6 | 8 | 0 | 0 |
