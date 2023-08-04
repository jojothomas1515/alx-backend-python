#!/usr/bin/env python3
"""Module for function that return a tuple."""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Take the arguments passed and makes it a tuple."""
    return (k, float(v))
