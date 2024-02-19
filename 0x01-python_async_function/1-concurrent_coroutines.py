#!/usr/bin/env python3
"""
wait n module
"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int):
    """
    call wait wait_random n times with max_delay
    """
    awaited_delays = []

    for _ in range(0, n):
        awaited_delays.append(await wait_random(max_delay))

    return awaited_delays
