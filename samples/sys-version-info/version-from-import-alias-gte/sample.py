from sys import version_info as v

if v >= (3, 14):
    x: int = 1
else:
    x: str = "older"

y: int = x
