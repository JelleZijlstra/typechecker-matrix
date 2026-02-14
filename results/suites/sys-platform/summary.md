# Python Type Checker Feature Matrix

Generated: 2026-02-14T23:00:41+00:00

Suites: sys-platform

Legend: ✅ supported, ❌ unsupported, ⚪ unavailable, ⚠️ error

| Feature | mypy | pyright | ty | pyrefly |
| --- | --- | --- | --- | --- |
| p = sys.platform | ❌ | ❌ | ✅ | ❌ |
| TARGETS tuple | ❌ | ❌ | ❌ | ❌ |
| or | ✅ | ✅ | ✅ | ✅ |
| == | ✅ | ✅ | ✅ | ✅ |
| from sys import platform | ❌ | ❌ | ✅ | ❌ |
| import sys as other_name | ❌ | ✅ | ✅ | ❌ |
| in (list) | ❌ | ❌ | ❌ | ❌ |
| in (set) | ❌ | ❌ | ❌ | ❌ |
| in (tuple) | ❌ | ❌ | ❌ | ❌ |
| != | ✅ | ✅ | ✅ | ✅ |
| startswith | ✅ | ❌ | ✅ | ✅ |
| not (==) | ✅ | ✅ | ✅ | ✅ |
| not in (list) | ❌ | ❌ | ❌ | ❌ |
| not in (set) | ❌ | ❌ | ❌ | ❌ |
| not in (tuple) | ❌ | ❌ | ❌ | ❌ |
| reverse == | ❌ | ❌ | ✅ | ✅ |
| reverse != | ❌ | ❌ | ✅ | ✅ |

## Totals

| Checker | ✅ supported | ❌ unsupported | ⚪ unavailable | ⚠️ error |
| --- | --- | --- | --- | --- |
| mypy | 5 | 12 | 0 | 0 |
| pyright | 5 | 12 | 0 | 0 |
| ty | 10 | 7 | 0 | 0 |
| pyrefly | 7 | 10 | 0 | 0 |
