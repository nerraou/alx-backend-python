#!/usr/bin/env python3
"""
sum of float list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    sum of float list
    """
    return sum(mxd_lst)
