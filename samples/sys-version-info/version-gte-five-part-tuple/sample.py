import sys

if sys.version_info >= (3, 14, 0, "final", 0):
    x: int = 1
else:
    x: str = "older"

y: int = x
