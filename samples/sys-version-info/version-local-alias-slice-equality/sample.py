import sys

v = sys.version_info
if v[:2] == (3, 14):
    x: int = 1
else:
    x: str = "other"

y: int = x
