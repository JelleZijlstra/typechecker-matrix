# Python Type Checker Feature Matrix

Generated: 2026-02-14T22:44:57+00:00

Suites: sys-version-info

Legend: ✅ supported, ❌ unsupported, ⚪ unavailable, ⚠️ error

| Feature | mypy | pyright | ty | pyrefly |
| --- | --- | --- | --- | --- |
| chained range | ❌ | ❌ | ✅ | ❌ |
| from sys import version_info as v | ❌ | ❌ | ✅ | ❌ |
| from sys import version_info | ❌ | ❌ | ✅ | ❌ |
| >= tuple | ✅ | ✅ | ✅ | ✅ |
| >= tuple (5-part) | ❌ | ✅ | ❌ | ❌ |
| >= tuple (3-part) | ❌ | ✅ | ❌ | ❌ |
| import sys as other_name | ❌ | ✅ | ✅ | ❌ |
| in supported set | ❌ | ❌ | ❌ | ❌ |
| [0] == | ✅ | ✅ | ✅ | ❌ |
| local alias slice == | ❌ | ❌ | ✅ | ❌ |
| < tuple | ✅ | ✅ | ✅ | ✅ |
| .major == | ❌ | ❌ | ✅ | ❌ |
| (major, minor) == | ❌ | ❌ | ✅ | ❌ |
| .minor == | ❌ | ❌ | ✅ | ❌ |
| not (>=) | ✅ | ✅ | ✅ | ✅ |
| reverse <= tuple | ✅ | ❌ | ✅ | ✅ |
| reverse == slice | ✅ | ❌ | ✅ | ❌ |
| [:2] == tuple | ✅ | ❌ | ✅ | ❌ |

## Totals

| Checker | ✅ supported | ❌ unsupported | ⚪ unavailable | ⚠️ error |
| --- | --- | --- | --- | --- |
| mypy | 7 | 11 | 0 | 0 |
| pyright | 7 | 11 | 0 | 0 |
| ty | 15 | 3 | 0 | 0 |
| pyrefly | 4 | 14 | 0 | 0 |
