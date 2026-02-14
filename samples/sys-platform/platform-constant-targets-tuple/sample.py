import sys

TARGETS = ("darwin", "linux")
if sys.platform in TARGETS:
    x: int = 1
else:
    x: str = "other-platform"

y: int = x
