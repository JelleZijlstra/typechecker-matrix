import sys

if "darwin" != sys.platform:
    x: str = "not-target"
else:
    x: int = 1

y: int = x
