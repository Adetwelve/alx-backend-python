#!/usr/bin/env python3
from typing import Union, List
""" type-annotated function: sum_mixed_list """


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """ return sum of list """
    return sum(mxd_lst)
