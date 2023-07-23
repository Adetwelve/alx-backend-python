#!/usr/bin/env python3
""" A type_annotated function """


from typing import Mapping, Any, Optional, TypeVar, Union

T = TypeVar('T')
Resp = Union[Any, T]
Deft = Union[T, None]


def safely_get_value(dct: Mapping, key: Any, default: Deft = None) -> Resp:
    """
       A funtion that retrieves value from a dict using key.
    """
    if key in dct:
        return dct[key]
    else:
        return default
