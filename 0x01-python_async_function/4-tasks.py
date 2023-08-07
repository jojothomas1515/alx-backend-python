#!/usr/bin/env python3
"""Module for functions that performs cuccurent operation."""
from typing import List, Union
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Return the list of all the delays (float values).

    The list of the delays should be in ascending order
    without using sort() because of concurrency.

    Args:
        n: number for time to run wait_random.
        max_delay: maximum delay wait_random can sleep for.
    Return: list of all delays.
    """
    tasks = [asyncio.create_task(task_wait_random(max_delay))
             for _ in range(n)]

    result: List[Union[float, int]] = []
    for t in asyncio.as_completed(tasks):
        res = await t
        result.append(res)

    return result