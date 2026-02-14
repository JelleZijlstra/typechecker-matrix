import sys

if (3, 14) <= sys.version_info:
    x: int = 1
else:
    x: str = "older"

y: int = x
