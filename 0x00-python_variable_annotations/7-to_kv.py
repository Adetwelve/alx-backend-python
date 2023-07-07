#!/usr/bin/env python3
""" type-annotated function: to_kv
    parameter: k, v
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ return a tuple containing key and the square of the value """
    return k, v ** 2
