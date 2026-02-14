import sys

if sys.platform == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
