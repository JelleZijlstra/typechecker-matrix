import sys

if "darwin" == sys.platform:
    x: int = 1
else:
    x: str = "not-target"

y: int = x
