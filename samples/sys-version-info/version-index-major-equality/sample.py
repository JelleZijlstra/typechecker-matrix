import sys

if sys.version_info[0] == 3:
    x: int = 1
else:
    x: str = "other"

y: int = x
