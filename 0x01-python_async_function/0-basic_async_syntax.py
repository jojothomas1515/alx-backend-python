#!/usr/bin/env python3
"""Module for a random async timer function."""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait random  asynchronusly wait for a random amount of
    time that is between the max_delay and 0 number of seconds.
    """
    secs = random.uniform(0, max_delay)
    await asyncio.sleep(secs)
    return secs
