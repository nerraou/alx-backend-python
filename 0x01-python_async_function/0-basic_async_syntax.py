#!/usr/bin/env python3
"""
basic async syntax
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    sleep for a random time
    """
    randomDelay: float = random.uniform(0, max_delay)
    await asyncio.sleep(randomDelay)

    return randomDelay
