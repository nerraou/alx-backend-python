#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    measure the runtime
    """

    start = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    diffrence = time.perf_counter() - start

    return diffrence
