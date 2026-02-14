import sys

if not (sys.version_info >= (3, 14)):
    x: str = "older"
else:
    x: int = 1

y: int = x
