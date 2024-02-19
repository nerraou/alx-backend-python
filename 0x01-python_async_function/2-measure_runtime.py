#!/usr/bin/env python3
""" Measure the runtime """
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    measure the runtime
    """

    current_time = time.time()
    asyncio.run(wait_n(max_delay, n))
    last_time = time.time() - current_time
    total_time = last_time / n

    return total_time
