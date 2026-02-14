import sys

if sys.platform not in {"darwin", "linux"}:
    x: str = "other-platform"
else:
    x: int = 1

y: int = x
