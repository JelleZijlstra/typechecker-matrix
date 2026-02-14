import sys

if sys.platform == "linux" or sys.platform == "darwin":
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
