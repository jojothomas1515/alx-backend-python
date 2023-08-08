#!/usr/bin/env python3
"""Generators."""

import asyncio
import random
from typing import Iterator

async def async_generator() -> Iterator[float]:
    """Random no async gen."""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
