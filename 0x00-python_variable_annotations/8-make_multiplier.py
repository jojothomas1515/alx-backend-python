#!/usr/bin/env python3
"""Module for function that return a multipiler function."""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Make multiplier function."""
    return (lambda x: x * multiplier)
