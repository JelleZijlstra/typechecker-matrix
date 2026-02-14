from typing import Literal


def f(x: Literal["a", "b"]) -> int:
    if x == "a":
        return 1
    return 2
