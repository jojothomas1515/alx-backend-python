#!/usr/bin/env python3
"""Module for a function that sum a list."""


def sum_list(input_list: list[float]) -> float:
    """Sum a list."""
    acc: float = 0
    for i in input_list:
        acc += i
    return acc
