import sys as other_name

if other_name.version_info >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
