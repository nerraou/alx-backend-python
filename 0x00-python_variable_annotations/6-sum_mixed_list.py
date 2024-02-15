#!/usr/bin/env python3
"""
sum of float list function
"""
from typing import List, Union


def sum_mixed_list(mixList: List[Union[float, int]]) -> float:
    """
    sum of float list
    """
    return sum(mixList)
