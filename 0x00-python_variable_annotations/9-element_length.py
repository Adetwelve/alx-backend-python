#!/usr/bin/env python3
""" Annotate the function """
from typing import List, Tuple


def element_length(lst: List[str]) -> List[Tuple[str, int]]:
    """ return """
    return [(i, len(i)) for i in lst]
