#!/usr/bin/env python3
"""Module for time measurement functions."""

import asyncio
import time
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measure the total execution time of wait_n.

    Args:
        n: number for task wait_n will create and wait for.
        max_delay: max delay that any task can sleep for.
    Return: Total time of execution.
    """
    s_t = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    return time.perf_counter() - s_t
