#!/usr/bin/env python3
"""
Complex types
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    to kv
    """
    return (k, v**2)
