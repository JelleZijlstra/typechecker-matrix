import sys

if sys.version_info[:2] == (3, 14):
    x: int = 1
else:
    x: str = "other"

y: int = x
