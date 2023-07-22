#!/usr/bin/env python3
""" A type-annotated function make_multiplier """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a lambda function that multiplies a float by the given multiplier."""
    return lambda v: v * multiplier

