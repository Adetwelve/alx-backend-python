#!/usr/bin/env python3
from typing import Union, List
""" type-annotated function: sum_mixed_list """


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ return sum of list """
    return float(sum(mxd_lst))
