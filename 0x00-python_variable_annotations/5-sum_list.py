#!/usr/bin/env python3
""" type-annotated function: sum_list
    parameter: input_list
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ return sum of float in list """
    return sum(input_list)
