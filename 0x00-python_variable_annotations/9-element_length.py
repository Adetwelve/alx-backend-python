#!/usr/bin/env python3
""" Annotate the function """
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Annotate the below function’s parameters
        return values with the appropriate types
    """
    return [(i, len(i)) for i in lst]
