import sys

if (3, 14) == sys.version_info[:2]:
    x: int = 1
else:
    x: str = "other"

y: int = x
