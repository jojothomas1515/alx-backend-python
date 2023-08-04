#!/usr/bin/env python3
"""Module from the sum_mixed_list function."""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Return the sum of a missed list with both floats and int."""
    acc: float = 0
    for i in mxd_list:
        acc += i
    return acc
