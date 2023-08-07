#!/usr/bin/env python3
"""Module for function that create a task."""

import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates a wait_random task.

    Args:
        max_delay: The max time that wait_random task can sleep for.
    Return: Awaitable Task
    """
    return asyncio.create_task(wait_random(max_delay))
