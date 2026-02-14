import sys

if not (sys.platform == "darwin"):
    x: str = "not-target"
else:
    x: int = 1

y: int = x
