#!/usr/bin/env python3
"""
Complex types
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    make multiplier
    """
    def multiplies(n: float):
        """
        multiply two numbers
        """
        return n * multiplier
    return multiplies
