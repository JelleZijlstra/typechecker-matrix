# Python Type Checker Detailed Report

Generated: 2026-02-14T23:00:52+00:00

Suites: sys-version-info

## sys-version-info/version-chained-range

- Feature: `chained range`
- Description: Chained range comparison should preserve narrowing for the in-range branch
- Expectation: `accept`
- Path: `samples/sys-version-info/version-chained-range/sample.py`

### Sample Code

```python
import sys

if (3, 14) <= sys.version_info < (3, 15):
    x: int = 1
else:
    x: str = "out-of-range"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `165`
- Command: `mypy samples/sys-version-info/version-chained-range/sample.py`

#### stdout

```text
samples/sys-version-info/version-chained-range/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `436`
- Command: `pyright samples/sys-version-info/version-chained-range/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-chained-range/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-chained-range/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-chained-range/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-chained-range/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Command: `ty check samples/sys-version-info/version-chained-range/sample.py`

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
- Duration (ms): `104`
- Command: `pyrefly check samples/sys-version-info/version-chained-range/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-chained-range/sample.py:6:5
  |
6 |     x: str = "out-of-range"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-chained-range/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-from-import-alias-gte

- Feature: `from sys import version_info as v`
- Description: Using 'from sys import version_info as v' should preserve version-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-from-import-alias-gte/sample.py`

### Sample Code

```python
from sys import version_info as v

if v >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `151`
- Command: `mypy samples/sys-version-info/version-from-import-alias-gte/sample.py`

#### stdout

```text
samples/sys-version-info/version-from-import-alias-gte/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `567`
- Command: `pyright samples/sys-version-info/version-from-import-alias-gte/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-alias-gte/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-alias-gte/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-alias-gte/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-alias-gte/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Command: `ty check samples/sys-version-info/version-from-import-alias-gte/sample.py`

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
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-version-info/version-from-import-alias-gte/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-from-import-alias-gte/sample.py:6:5
  |
6 |     x: str = "older"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-from-import-alias-gte/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-from-import-gte

- Feature: `from sys import version_info`
- Description: Using 'from sys import version_info' should preserve version-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-from-import-gte/sample.py`

### Sample Code

```python
from sys import version_info

if version_info >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-version-info/version-from-import-gte/sample.py`

#### stdout

```text
samples/sys-version-info/version-from-import-gte/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `459`
- Command: `pyright samples/sys-version-info/version-from-import-gte/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-gte/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-gte/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-gte/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-from-import-gte/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `16`
- Command: `ty check samples/sys-version-info/version-from-import-gte/sample.py`

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
- Duration (ms): `84`
- Command: `pyrefly check samples/sys-version-info/version-from-import-gte/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-from-import-gte/sample.py:6:5
  |
6 |     x: str = "older"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-from-import-gte/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-gte-current-tuple

- Feature: `>= tuple`
- Description: sys.version_info >= (3, 14) should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-gte-current-tuple/sample.py`

### Sample Code

```python
import sys

if sys.version_info >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `149`
- Command: `mypy samples/sys-version-info/version-gte-current-tuple/sample.py`

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
- Duration (ms): `436`
- Command: `pyright samples/sys-version-info/version-gte-current-tuple/sample.py`

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
- Command: `ty check samples/sys-version-info/version-gte-current-tuple/sample.py`

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
- Command: `pyrefly check samples/sys-version-info/version-gte-current-tuple/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-version-info/version-gte-five-part-tuple

- Feature: `>= tuple (5-part)`
- Description: sys.version_info >= (3, 14, 0, 'final', 0) should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-gte-five-part-tuple/sample.py`

### Sample Code

```python
import sys

if sys.version_info >= (3, 14, 0, "final", 0):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `149`
- Command: `mypy samples/sys-version-info/version-gte-five-part-tuple/sample.py`

#### stdout

```text
samples/sys-version-info/version-gte-five-part-tuple/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `450`
- Command: `pyright samples/sys-version-info/version-gte-five-part-tuple/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `25`
- Command: `ty check samples/sys-version-info/version-gte-five-part-tuple/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "older"]` is not assignable to `int`
 --> samples/sys-version-info/version-gte-five-part-tuple/sample.py:8:4
  |
6 |     x: str = "older"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "older"]`
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
- Command: `pyrefly check samples/sys-version-info/version-gte-five-part-tuple/sample.py`

#### stdout

```text
ERROR `str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-gte-five-part-tuple/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 1 error
```

## sys-version-info/version-gte-three-part-tuple

- Feature: `>= tuple (3-part)`
- Description: sys.version_info >= (3, 14, 0) should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-gte-three-part-tuple/sample.py`

### Sample Code

```python
import sys

if sys.version_info >= (3, 14, 0):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `134`
- Command: `mypy samples/sys-version-info/version-gte-three-part-tuple/sample.py`

#### stdout

```text
samples/sys-version-info/version-gte-three-part-tuple/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `448`
- Command: `pyright samples/sys-version-info/version-gte-three-part-tuple/sample.py`

#### stdout

```text
0 errors, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `18`
- Command: `ty check samples/sys-version-info/version-gte-three-part-tuple/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "older"]` is not assignable to `int`
 --> samples/sys-version-info/version-gte-three-part-tuple/sample.py:8:4
  |
6 |     x: str = "older"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "older"]`
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
- Command: `pyrefly check samples/sys-version-info/version-gte-three-part-tuple/sample.py`

#### stdout

```text
ERROR `str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-gte-three-part-tuple/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 1 error
```

## sys-version-info/version-import-alias-gte

- Feature: `import sys as other_name`
- Description: Using 'import sys as other_name' should preserve version-guard narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-import-alias-gte/sample.py`

### Sample Code

```python
import sys as other_name

if other_name.version_info >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `141`
- Command: `mypy samples/sys-version-info/version-import-alias-gte/sample.py`

#### stdout

```text
samples/sys-version-info/version-import-alias-gte/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `0`
- Duration (ms): `432`
- Command: `pyright samples/sys-version-info/version-import-alias-gte/sample.py`

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
- Command: `ty check samples/sys-version-info/version-import-alias-gte/sample.py`

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
- Command: `pyrefly check samples/sys-version-info/version-import-alias-gte/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-import-alias-gte/sample.py:6:5
  |
6 |     x: str = "older"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-import-alias-gte/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-in-supported-set

- Feature: `in supported set`
- Description: Membership in a set of supported major/minor tuples should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-in-supported-set/sample.py`

### Sample Code

```python
import sys

if sys.version_info[:2] in {(3, 13), (3, 14)}:
    x: int = 1
else:
    x: str = "unsupported"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `138`
- Command: `mypy samples/sys-version-info/version-in-supported-set/sample.py`

#### stdout

```text
samples/sys-version-info/version-in-supported-set/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `430`
- Command: `pyright samples/sys-version-info/version-in-supported-set/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-in-supported-set/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-in-supported-set/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-in-supported-set/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-in-supported-set/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Command: `ty check samples/sys-version-info/version-in-supported-set/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal[1, "unsupported"]` is not assignable to `int`
 --> samples/sys-version-info/version-in-supported-set/sample.py:8:4
  |
6 |     x: str = "unsupported"
7 |
8 | y: int = x
  |    ---   ^ Incompatible value of type `Literal[1, "unsupported"]`
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
- Command: `pyrefly check samples/sys-version-info/version-in-supported-set/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-in-supported-set/sample.py:6:5
  |
6 |     x: str = "unsupported"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-in-supported-set/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-index-major-equality

- Feature: `[0] ==`
- Description: Index-based major version check should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-index-major-equality/sample.py`

### Sample Code

```python
import sys

if sys.version_info[0] == 3:
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `135`
- Command: `mypy samples/sys-version-info/version-index-major-equality/sample.py`

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
- Duration (ms): `462`
- Command: `pyright samples/sys-version-info/version-index-major-equality/sample.py`

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
- Command: `ty check samples/sys-version-info/version-index-major-equality/sample.py`

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
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-version-info/version-index-major-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-index-major-equality/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-index-major-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-local-alias-slice-equality

- Feature: `local alias slice ==`
- Description: Local alias of sys.version_info with slice equality should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-local-alias-slice-equality/sample.py`

### Sample Code

```python
import sys

v = sys.version_info
if v[:2] == (3, 14):
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `137`
- Command: `mypy samples/sys-version-info/version-local-alias-slice-equality/sample.py`

#### stdout

```text
samples/sys-version-info/version-local-alias-slice-equality/sample.py:7: error: Name "x" already defined on line 5  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `447`
- Command: `pyright samples/sys-version-info/version-local-alias-slice-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-local-alias-slice-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-local-alias-slice-equality/sample.py:5:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-local-alias-slice-equality/sample.py:5:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-local-alias-slice-equality/sample.py:9:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `16`
- Command: `ty check samples/sys-version-info/version-local-alias-slice-equality/sample.py`

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
- Command: `pyrefly check samples/sys-version-info/version-local-alias-slice-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-local-alias-slice-equality/sample.py:7:5
  |
7 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-local-alias-slice-equality/sample.py:9:10
  |
9 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-lt-next-minor

- Feature: `< tuple`
- Description: sys.version_info < (3, 15) should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-lt-next-minor/sample.py`

### Sample Code

```python
import sys

if sys.version_info < (3, 15):
    x: int = 1
else:
    x: str = "newer"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `135`
- Command: `mypy samples/sys-version-info/version-lt-next-minor/sample.py`

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
- Duration (ms): `443`
- Command: `pyright samples/sys-version-info/version-lt-next-minor/sample.py`

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
- Command: `ty check samples/sys-version-info/version-lt-next-minor/sample.py`

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
- Duration (ms): `95`
- Command: `pyrefly check samples/sys-version-info/version-lt-next-minor/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-version-info/version-major-attr

- Feature: `.major ==`
- Description: sys.version_info.major equality should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-major-attr/sample.py`

### Sample Code

```python
import sys

if sys.version_info.major == 3:
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `183`
- Command: `mypy samples/sys-version-info/version-major-attr/sample.py`

#### stdout

```text
samples/sys-version-info/version-major-attr/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `696`
- Command: `pyright samples/sys-version-info/version-major-attr/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-attr/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-attr/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-attr/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-attr/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `44`
- Command: `ty check samples/sys-version-info/version-major-attr/sample.py`

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
- Duration (ms): `117`
- Command: `pyrefly check samples/sys-version-info/version-major-attr/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-major-attr/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-major-attr/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-major-minor-tuple-equality

- Feature: `(major, minor) ==`
- Description: Tuple comparison of sys.version_info.major/minor should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-major-minor-tuple-equality/sample.py`

### Sample Code

```python
import sys

if (sys.version_info.major, sys.version_info.minor) == (3, 14):
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `334`
- Command: `mypy samples/sys-version-info/version-major-minor-tuple-equality/sample.py`

#### stdout

```text
samples/sys-version-info/version-major-minor-tuple-equality/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `481`
- Command: `pyright samples/sys-version-info/version-major-minor-tuple-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-minor-tuple-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-minor-tuple-equality/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-minor-tuple-equality/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-major-minor-tuple-equality/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `16`
- Command: `ty check samples/sys-version-info/version-major-minor-tuple-equality/sample.py`

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
- Command: `pyrefly check samples/sys-version-info/version-major-minor-tuple-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-major-minor-tuple-equality/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-major-minor-tuple-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-minor-attr

- Feature: `.minor ==`
- Description: sys.version_info.minor equality should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-minor-attr/sample.py`

### Sample Code

```python
import sys

if sys.version_info.minor == 14:
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `135`
- Command: `mypy samples/sys-version-info/version-minor-attr/sample.py`

#### stdout

```text
samples/sys-version-info/version-minor-attr/sample.py:6: error: Name "x" already defined on line 4  [no-redef]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `unsupported`
- Return code: `1`
- Duration (ms): `430`
- Command: `pyright samples/sys-version-info/version-minor-attr/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-minor-attr/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-minor-attr/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-minor-attr/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-minor-attr/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Command: `ty check samples/sys-version-info/version-minor-attr/sample.py`

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
- Duration (ms): `83`
- Command: `pyrefly check samples/sys-version-info/version-minor-attr/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-minor-attr/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-minor-attr/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-not-gte-wrapper

- Feature: `not (>=)`
- Description: Negated version comparison should preserve narrowing in else branch
- Expectation: `accept`
- Path: `samples/sys-version-info/version-not-gte-wrapper/sample.py`

### Sample Code

```python
import sys

if not (sys.version_info >= (3, 14)):
    x: str = "older"
else:
    x: int = 1

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `137`
- Command: `mypy samples/sys-version-info/version-not-gte-wrapper/sample.py`

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
- Duration (ms): `447`
- Command: `pyright samples/sys-version-info/version-not-gte-wrapper/sample.py`

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
- Command: `ty check samples/sys-version-info/version-not-gte-wrapper/sample.py`

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
- Duration (ms): `87`
- Command: `pyrefly check samples/sys-version-info/version-not-gte-wrapper/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-version-info/version-reverse-gte-tuple

- Feature: `reverse <= tuple`
- Description: Reverse comparator order (3, 14) <= sys.version_info should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-reverse-gte-tuple/sample.py`

### Sample Code

```python
import sys

if (3, 14) <= sys.version_info:
    x: int = 1
else:
    x: str = "older"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `155`
- Command: `mypy samples/sys-version-info/version-reverse-gte-tuple/sample.py`

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
- Duration (ms): `545`
- Command: `pyright samples/sys-version-info/version-reverse-gte-tuple/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-gte-tuple/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-gte-tuple/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-gte-tuple/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-gte-tuple/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `46`
- Command: `ty check samples/sys-version-info/version-reverse-gte-tuple/sample.py`

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
- Duration (ms): `125`
- Command: `pyrefly check samples/sys-version-info/version-reverse-gte-tuple/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```

## sys-version-info/version-reverse-slice-equality

- Feature: `reverse == slice`
- Description: Reverse equality order for version slice should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-reverse-slice-equality/sample.py`

### Sample Code

```python
import sys

if (3, 14) == sys.version_info[:2]:
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `245`
- Command: `mypy samples/sys-version-info/version-reverse-slice-equality/sample.py`

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
- Duration (ms): `491`
- Command: `pyright samples/sys-version-info/version-reverse-slice-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-slice-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-slice-equality/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-slice-equality/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-reverse-slice-equality/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `19`
- Command: `ty check samples/sys-version-info/version-reverse-slice-equality/sample.py`

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
- Duration (ms): `85`
- Command: `pyrefly check samples/sys-version-info/version-reverse-slice-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-reverse-slice-equality/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-reverse-slice-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```

## sys-version-info/version-slice-equality

- Feature: `[:2] == tuple`
- Description: sys.version_info[:2] equality should preserve narrowing
- Expectation: `accept`
- Path: `samples/sys-version-info/version-slice-equality/sample.py`

### Sample Code

```python
import sys

if sys.version_info[:2] == (3, 14):
    x: int = 1
else:
    x: str = "other"

y: int = x
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `143`
- Command: `mypy samples/sys-version-info/version-slice-equality/sample.py`

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
- Duration (ms): `446`
- Command: `pyright samples/sys-version-info/version-slice-equality/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-slice-equality/sample.py
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-slice-equality/sample.py:4:5 - error: Declaration "x" is obscured by a declaration of the same name (reportRedeclaration)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-slice-equality/sample.py:4:14 - error: Type "Literal[1]" is not assignable to declared type "str"
    "Literal[1]" is not assignable to "str" (reportAssignmentType)
  /Users/jelle/py/typechecker-matrix/samples/sys-version-info/version-slice-equality/sample.py:8:10 - error: Type "str" is not assignable to declared type "int"
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
- Duration (ms): `16`
- Command: `ty check samples/sys-version-info/version-slice-equality/sample.py`

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
- Command: `pyrefly check samples/sys-version-info/version-slice-equality/sample.py`

#### stdout

```text
ERROR `x` cannot be annotated with `str`, it is already defined with type `int` [redefinition]
 --> samples/sys-version-info/version-slice-equality/sample.py:6:5
  |
6 |     x: str = "other"
  |     ^
  |
ERROR `int | str` is not assignable to `int` [bad-assignment]
 --> samples/sys-version-info/version-slice-equality/sample.py:8:10
  |
8 | y: int = x
  |          ^
  |
```

#### stderr

```text
 INFO 2 errors
```
