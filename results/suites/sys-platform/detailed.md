# Python Type Checker Detailed Report

Generated: 2026-02-14T23:00:41+00:00

Suites: sys-platform

## sys-platform/platform-alias-variable-equality

- Feature: `p = sys.platform`
- Description: A local alias of sys.platform should preserve equality-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-alias-variable-equality/sample.py`

### Sample Code

```python
import sys

p = sys.platform
if p == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `155`
- Command: `mypy samples/sys-platform/platform-alias-variable-equality/sample.py`

#### stdout

```text
samples/sys-platform/platform-alias-variable-equality/sample.py:7: error: Name "x" already defined on line 5  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `458`
- Command: `pyright samples/sys-platform/platform-alias-variable-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-alias-variable-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-alias-variable-equality/sample.py:5:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-alias-variable-equality/sample.py:5:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-alias-variable-equality/sample.py:9:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `17`
- Command: `ty check samples/sys-platform/platform-alias-variable-equality/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `108`
- Command: `pyrefly check samples/sys-platform/platform-alias-variable-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-alias-variable-equality/sample.py:7:5
  |
7 |     x: str = "not-target"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-alias-variable-equality/sample.py:9:10
  |
9 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-constant-targets-tuple

- Feature: `TARGETS tuple`
- Description: Membership check against a named tuple constant should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-constant-targets-tuple/sample.py`

### Sample Code

```python
import sys

TARGETS = ("darwin", "linux")
if sys.platform in TARGETS:
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `152`
- Command: `mypy samples/sys-platform/platform-constant-targets-tuple/sample.py`

#### stdout

```text
samples/sys-platform/platform-constant-targets-tuple/sample.py:7: error: Name "x" already defined on line 5  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `438`
- Command: `pyright samples/sys-platform/platform-constant-targets-tuple/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-constant-targets-tuple/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-constant-targets-tuple/sample.py:5:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-constant-targets-tuple/sample.py:5:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-constant-targets-tuple/sample.py:9:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `19`
- Command: `ty check samples/sys-platform/platform-constant-targets-tuple/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "other-platform"]` is not assignable to `int`
 --> samples/sys-platform/platform-constant-targets-tuple/sample.py:9:4
  |
7 |     x: str = "other-platform"
8 |
9 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "other-platform"]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `85`
- Command: `pyrefly check samples/sys-platform/platform-constant-targets-tuple/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-constant-targets-tuple/sample.py:7:5
  |
7 |     x: str = "other-platform"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-constant-targets-tuple/sample.py:9:10
  |
9 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-disjunction-check

- Feature: `or`
- Description: Disjunction of platform equalities should select the int-typed definition used afterward
- Expectation: `accept`
- Path: `samples/sys-platform/platform-disjunction-check/sample.py`

### Sample Code

```python
import sys

if sys.platform == "linux" or sys.platform == "darwin":
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `137`
- Command: `mypy samples/sys-platform/platform-disjunction-check/sample.py`

#### stdout

```text
Success: no issues found in 1 source file
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `430`
- Command: `pyright samples/sys-platform/platform-disjunction-check/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `16`
- Command: `ty check samples/sys-platform/platform-disjunction-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `80`
- Command: `pyrefly check samples/sys-platform/platform-disjunction-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-equality-check

- Feature: `==`
- Description: Equality guard should select the int-typed definition that is used after the conditional
- Expectation: `accept`
- Path: `samples/sys-platform/platform-equality-check/sample.py`

### Sample Code

```python
import sys

if sys.platform == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `143`
- Command: `mypy samples/sys-platform/platform-equality-check/sample.py`

#### stdout

```text
Success: no issues found in 1 source file
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `451`
- Command: `pyright samples/sys-platform/platform-equality-check/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `15`
- Command: `ty check samples/sys-platform/platform-equality-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-platform/platform-equality-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-from-import-equality

- Feature: `from sys import platform`
- Description: Using 'from sys import platform' should preserve platform-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-from-import-equality/sample.py`

### Sample Code

```python
from sys import platform

if platform == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `155`
- Command: `mypy samples/sys-platform/platform-from-import-equality/sample.py`

#### stdout

```text
samples/sys-platform/platform-from-import-equality/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `438`
- Command: `pyright samples/sys-platform/platform-from-import-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-from-import-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-from-import-equality/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-from-import-equality/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-from-import-equality/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `15`
- Command: `ty check samples/sys-platform/platform-from-import-equality/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `82`
- Command: `pyrefly check samples/sys-platform/platform-from-import-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-from-import-equality/sample.py:6:5
  |
6 |     x: str = "not-target"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-from-import-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-import-alias-equality

- Feature: `import sys as other_name`
- Description: Using 'import sys as other_name' should preserve platform-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-import-alias-equality/sample.py`

### Sample Code

```python
import sys as other_name

if other_name.platform == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-import-alias-equality/sample.py`

#### stdout

```text
samples/sys-platform/platform-import-alias-equality/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `435`
- Command: `pyright samples/sys-platform/platform-import-alias-equality/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `15`
- Command: `ty check samples/sys-platform/platform-import-alias-equality/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `81`
- Command: `pyrefly check samples/sys-platform/platform-import-alias-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-import-alias-equality/sample.py:6:5
  |
6 |     x: str = "not-target"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-import-alias-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-in-list-literal

- Feature: `in (list)`
- Description: Membership test against a list literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-in-list-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform in ["darwin", "linux"]:
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `134`
- Command: `mypy samples/sys-platform/platform-in-list-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-in-list-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `445`
- Command: `pyright samples/sys-platform/platform-in-list-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-list-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-list-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-list-literal/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-list-literal/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `18`
- Command: `ty check samples/sys-platform/platform-in-list-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "other-platform"]` is not assignable to `int`
 --> samples/sys-platform/platform-in-list-literal/sample.py:8:4
  |
6 |     x: str = "other-platform"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "other-platform"]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `82`
- Command: `pyrefly check samples/sys-platform/platform-in-list-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-in-list-literal/sample.py:6:5
  |
6 |     x: str = "other-platform"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-in-list-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-in-set-literal

- Feature: `in (set)`
- Description: Membership test against a set literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-in-set-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform in {"darwin", "linux"}:
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-in-set-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-in-set-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `434`
- Command: `pyright samples/sys-platform/platform-in-set-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-set-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-set-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-set-literal/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-set-literal/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `19`
- Command: `ty check samples/sys-platform/platform-in-set-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "other-platform"]` is not assignable to `int`
 --> samples/sys-platform/platform-in-set-literal/sample.py:8:4
  |
6 |     x: str = "other-platform"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "other-platform"]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-platform/platform-in-set-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-in-set-literal/sample.py:6:5
  |
6 |     x: str = "other-platform"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-in-set-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-in-tuple-literal

- Feature: `in (tuple)`
- Description: Membership test against a tuple literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-in-tuple-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform in ("darwin", "linux"):
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `134`
- Command: `mypy samples/sys-platform/platform-in-tuple-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-in-tuple-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `426`
- Command: `pyright samples/sys-platform/platform-in-tuple-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-tuple-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-tuple-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-tuple-literal/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-in-tuple-literal/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `16`
- Command: `ty check samples/sys-platform/platform-in-tuple-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "other-platform"]` is not assignable to `int`
 --> samples/sys-platform/platform-in-tuple-literal/sample.py:8:4
  |
6 |     x: str = "other-platform"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "other-platform"]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `81`
- Command: `pyrefly check samples/sys-platform/platform-in-tuple-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-platform/platform-in-tuple-literal/sample.py:6:5
  |
6 |     x: str = "other-platform"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-in-tuple-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-inequality-check

- Feature: `!=`
- Description: Inequality guard should still select the int-typed definition used after the conditional
- Expectation: `accept`
- Path: `samples/sys-platform/platform-inequality-check/sample.py`

### Sample Code

```python
import sys

if sys.platform != "darwin":
    x: str = "not-target"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-inequality-check/sample.py`

#### stdout

```text
Success: no issues found in 1 source file
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `450`
- Command: `pyright samples/sys-platform/platform-inequality-check/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `17`
- Command: `ty check samples/sys-platform/platform-inequality-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `82`
- Command: `pyrefly check samples/sys-platform/platform-inequality-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-method-check

- Feature: `startswith`
- Description: Method-based platform checks are a contrast case for post-conditional narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-method-check/sample.py`

### Sample Code

```python
import sys

if sys.platform.startswith("dar"):
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-method-check/sample.py`

#### stdout

```text
Success: no issues found in 1 source file
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `517`
- Command: `pyright samples/sys-platform/platform-method-check/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-method-check/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-method-check/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-method-check/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-method-check/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `18`
- Command: `ty check samples/sys-platform/platform-method-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `84`
- Command: `pyrefly check samples/sys-platform/platform-method-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-not-equality-wrapper

- Feature: `not (==)`
- Description: Negated equality expression should preserve narrowing in the else branch
- Expectation: `accept`
- Path: `samples/sys-platform/platform-not-equality-wrapper/sample.py`

### Sample Code

```python
import sys

if not (sys.platform == "darwin"):
    x: str = "not-target"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-not-equality-wrapper/sample.py`

#### stdout

```text
Success: no issues found in 1 source file
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `457`
- Command: `pyright samples/sys-platform/platform-not-equality-wrapper/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `17`
- Command: `ty check samples/sys-platform/platform-not-equality-wrapper/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `85`
- Command: `pyrefly check samples/sys-platform/platform-not-equality-wrapper/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-not-in-list-literal

- Feature: `not in (list)`
- Description: Negative membership test against a list literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-not-in-list-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform not in ["darwin", "linux"]:
    x: str = "other-platform"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `148`
- Command: `mypy samples/sys-platform/platform-not-in-list-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-not-in-list-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
samples/sys-platform/platform-not-in-list-literal/sample.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `457`
- Command: `pyright samples/sys-platform/platform-not-in-list-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-list-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-list-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-list-literal/sample.py:4:14 - error: Type "Literal['other-platform']" is not assignable to declared type "int"
    "Literal['other-platform']" is not assignable to "int" (reportAssignmentType)
2 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `16`
- Command: `ty check samples/sys-platform/platform-not-in-list-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal["other-platform", 1]` is not assignable to `int`
 --> samples/sys-platform/platform-not-in-list-literal/sample.py:8:4
  |
6 |     x: int = 1
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal["other-platform", 1]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-platform/platform-not-in-list-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `int`, it is already defined with type `str` [redefinition]
 --> samples/sys-platform/platform-not-in-list-literal/sample.py:6:5
  |
6 |     x: int = 1
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-not-in-list-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-not-in-set-literal

- Feature: `not in (set)`
- Description: Negative membership test against a set literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-not-in-set-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform not in {"darwin", "linux"}:
    x: str = "other-platform"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-not-in-set-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-not-in-set-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
samples/sys-platform/platform-not-in-set-literal/sample.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `450`
- Command: `pyright samples/sys-platform/platform-not-in-set-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-set-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-set-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-set-literal/sample.py:4:14 - error: Type "Literal['other-platform']" is not assignable to declared type "int"
    "Literal['other-platform']" is not assignable to "int" (reportAssignmentType)
2 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `16`
- Command: `ty check samples/sys-platform/platform-not-in-set-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal["other-platform", 1]` is not assignable to `int`
 --> samples/sys-platform/platform-not-in-set-literal/sample.py:8:4
  |
6 |     x: int = 1
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal["other-platform", 1]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `82`
- Command: `pyrefly check samples/sys-platform/platform-not-in-set-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `int`, it is already defined with type `str` [redefinition]
 --> samples/sys-platform/platform-not-in-set-literal/sample.py:6:5
  |
6 |     x: int = 1
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-not-in-set-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-not-in-tuple-literal

- Feature: `not in (tuple)`
- Description: Negative membership test against a tuple literal should narrow branch selection
- Expectation: `accept`
- Path: `samples/sys-platform/platform-not-in-tuple-literal/sample.py`

### Sample Code

```python
import sys

if sys.platform not in ("darwin", "linux"):
    x: str = "other-platform"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-not-in-tuple-literal/sample.py`

#### stdout

```text
samples/sys-platform/platform-not-in-tuple-literal/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
samples/sys-platform/platform-not-in-tuple-literal/sample.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `449`
- Command: `pyright samples/sys-platform/platform-not-in-tuple-literal/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-tuple-literal/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-tuple-literal/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-not-in-tuple-literal/sample.py:4:14 - error: Type "Literal['other-platform']" is not assignable to declared type "int"
    "Literal['other-platform']" is not assignable to "int" (reportAssignmentType)
2 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `17`
- Command: `ty check samples/sys-platform/platform-not-in-tuple-literal/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal["other-platform", 1]` is not assignable to `int`
 --> samples/sys-platform/platform-not-in-tuple-literal/sample.py:8:4
  |
6 |     x: int = 1
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal["other-platform", 1]`
  |    |
  |    Declared type
  |
info: rule `invalid-assignment` is enabled by default

Found 1 diagnostic
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `81`
- Command: `pyrefly check samples/sys-platform/platform-not-in-tuple-literal/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `int`, it is already defined with type `str` [redefinition]
 --> samples/sys-platform/platform-not-in-tuple-literal/sample.py:6:5
  |
6 |     x: int = 1
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-platform/platform-not-in-tuple-literal/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-platform/platform-reverse-equality-check

- Feature: `reverse ==`
- Description: Reverse equality order should preserve platform-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-reverse-equality-check/sample.py`

### Sample Code

```python
import sys

if "darwin" == sys.platform:
    x: int = 1
else:
    x: str = "not-target"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-reverse-equality-check/sample.py`

#### stdout

```text
samples/sys-platform/platform-reverse-equality-check/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `431`
- Command: `pyright samples/sys-platform/platform-reverse-equality-check/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-equality-check/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-equality-check/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-equality-check/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-equality-check/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
    "str" is not assignable to "int" (reportAssignmentType)
3 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `15`
- Command: `ty check samples/sys-platform/platform-reverse-equality-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `82`
- Command: `pyrefly check samples/sys-platform/platform-reverse-equality-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-platform/platform-reverse-inequality-check

- Feature: `reverse !=`
- Description: Reverse inequality order should preserve platform-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-platform/platform-reverse-inequality-check/sample.py`

### Sample Code

```python
import sys

if "darwin" != sys.platform:
    x: str = "not-target"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-platform/platform-reverse-inequality-check/sample.py`

#### stdout

```text
samples/sys-platform/platform-reverse-inequality-check/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
samples/sys-platform/platform-reverse-inequality-check/sample.py:8: error: Incompatible types in assignment (expression has type "str", variable has type "int")  [assignment]
Found 2 errors in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `422`
- Command: `pyright samples/sys-platform/platform-reverse-inequality-check/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-inequality-check/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-inequality-check/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-platform/platform-reverse-inequality-check/sample.py:4:14 - error: Type "Literal['not-target']" is not assignable to declared type "int"
    "Literal['not-target']" is not assignable to "int" (reportAssignmentType)
2 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `0`
- Duration (ms): `15`
- Command: `ty check samples/sys-platform/platform-reverse-inequality-check/sample.py`

#### stdout

```text
All checks passed!
```

#### stderr

```text
(empty)
```

### pyrefly

- Status: `supported`
- Return code: `0`
- Duration (ms): `81`
- Command: `pyrefly check samples/sys-platform/platform-reverse-inequality-check/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```
