#!/usr/bin/env python3
"""
wait n module
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    call wait wait_random n times with max_delay
    """
    delays: List[float] = []
    tasks: List[asyncio.Future] = []

    for _ in range(0, n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delays.append(await task)

    return delays
