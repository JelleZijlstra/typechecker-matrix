# Python Type Checker Detailed Report

Generated: 2026-02-14T23:00:39+00:00

Suites: literals

## literals/literal-narrowing-failure

- Feature: `Literal narrowing`
- Description: Reject incompatible assignment under Literal type
- Expectation: `reject`
- Path: `samples/literals/literal-narrowing-failure/sample.py`

### Sample Code

```python
from typing import Literal

x: Literal["a"] = "b"
```

### mypy

- Status: `supported`
- Return code: `1`
- Duration (ms): `275`
- Command: `mypy samples/literals/literal-narrowing-failure/sample.py`

#### stdout

```text
samples/literals/literal-narrowing-failure/sample.py:3: error: Incompatible types in assignment (expression has type "Literal['b']", variable has type "Literal['a']")  [assignment]
Found 1 error in 1 file (checked 1 source file)
```

#### stderr

```text
(empty)
```

### pyright

- Status: `supported`
- Return code: `1`
- Duration (ms): `531`
- Command: `pyright samples/literals/literal-narrowing-failure/sample.py`

#### stdout

```text
/Users/jelle/py/typechecker-matrix/samples/literals/literal-narrowing-failure/sample.py
  /Users/jelle/py/typechecker-matrix/samples/literals/literal-narrowing-failure/sample.py:3:19 - error: Type "Literal['b']" is not assignable to declared type "Literal['a']"
    "Literal['b']" is not assignable to type "Literal['a']" (reportAssignmentType)
1 error, 0 warnings, 0 informations
```

#### stderr

```text
(empty)
```

### ty

- Status: `supported`
- Return code: `1`
- Duration (ms): `41`
- Command: `ty check samples/literals/literal-narrowing-failure/sample.py`

#### stdout

```text
error[invalid-assignment]: Object of type `Literal["b"]` is not assignable to `Literal["a"]`
 --> samples/literals/literal-narrowing-failure/sample.py:3:4
  |
1 | from typing import Literal
2 |
3 | x: Literal["a"] = "b"
  |    ------------   ^^^ Incompatible value of type `Literal["b"]`
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

- Status: `supported`
- Return code: `1`
- Duration (ms): `108`
- Command: `pyrefly check samples/literals/literal-narrowing-failure/sample.py`

#### stdout

```text
ERROR `Literal['b']` is not assignable to `Literal['a']` [bad-assignment]
 --> samples/literals/literal-narrowing-failure/sample.py:3:19
  |
3 | x: Literal["a"] = "b"
  |                   ^^^
  |
```

#### stderr

```text
 INFO 1 error
```

## literals/literal-narrowing-success

- Feature: `Literal narrowing`
- Description: Type checker understands Literal-based branch narrowing
- Expectation: `accept`
- Path: `samples/literals/literal-narrowing-success/sample.py`

### Sample Code

```python
from typing import Literal


def f(x: Literal["a", "b"]) -> int:
    if x == "a":
        return 1
    return 2
```

### mypy

- Status: `supported`
- Return code: `0`
- Duration (ms): `139`
- Command: `mypy samples/literals/literal-narrowing-success/sample.py`

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
- Duration (ms): `474`
- Command: `pyright samples/literals/literal-narrowing-success/sample.py`

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
- Command: `ty check samples/literals/literal-narrowing-success/sample.py`

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
- Duration (ms): `88`
- Command: `pyrefly check samples/literals/literal-narrowing-success/sample.py`

#### stdout

```text
(empty)
```

#### stderr

```text
 INFO 0 errors
```
