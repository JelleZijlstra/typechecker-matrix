import sys

if sys.version_info >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
