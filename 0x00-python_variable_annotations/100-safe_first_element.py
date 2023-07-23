#!/usr/bin/env python3
""" Funtion: duck-typed annotation """
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """ A function that get 1st element
        of a sequence if it exists
    """
    if lst:
        return lst[0]
    else:
        return None
