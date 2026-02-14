import sys

p = sys.platform
if p == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
