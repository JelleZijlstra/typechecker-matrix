import sys

if (3, 14) <= sys.version_info < (3, 15):
    x: int = 1
else:
    x: str = "out-of-range"

y: int = x
