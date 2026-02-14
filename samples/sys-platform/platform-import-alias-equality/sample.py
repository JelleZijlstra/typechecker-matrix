import sys as other_name

if other_name.platform == "darwin":
    x: int = 1
else:
    x: str = "not-target"

y: int = x
