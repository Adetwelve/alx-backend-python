#!/usr/bin/env python3
""" type-annotated function: sum_mixed_list """
from typing import Union, List


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ return sum of list """
    return sum(mxd_lst)
