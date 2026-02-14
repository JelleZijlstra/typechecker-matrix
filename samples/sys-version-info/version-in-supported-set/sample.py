import sys

if sys.version_info[:2] in {(3, 13), (3, 14)}:
    x: int = 1
else:
    x: str = "unsupported"

y: int = x
