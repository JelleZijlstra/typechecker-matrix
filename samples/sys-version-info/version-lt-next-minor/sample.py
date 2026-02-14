import sys

if sys.version_info < (3, 15):
    x: int = 1
else:
    x: str = "newer"

y: int = x
