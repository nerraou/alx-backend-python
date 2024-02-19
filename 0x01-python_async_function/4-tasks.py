#!/usr/bin/env python3
"""
wait n module
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    call wait task_wait_random n times with max_delay
    """
    delays: List[float] = []
    tasks: List[asyncio.Future] = []

    for _ in range(0, n):
        tasks.append(task_wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delays.append(await task)

    return delays
