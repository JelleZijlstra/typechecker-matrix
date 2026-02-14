import sys

if sys.platform in ("darwin", "linux"):
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
