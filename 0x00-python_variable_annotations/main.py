from typing import Callable


def return_function() -> Callable[[int], int]:

    return lambda x, y: x + y


jj: Callable[[int], int] = return_function()
jj(2)


all()
