#!/usr/bin/env python3
""" Parameterize a unit test """
import unittest
from typing import Tuple, Union, Dict, Any, Type
from utils import access_nested_map
from parameterized import parameterized


class TestAccessNestedMap(unittest.TestCase):
    """ Test the 'access_nested_map' function """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",),{"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])

    def test_access_nested_map(
            self,
            nested_map: Dict,
            path: Tuple[str],
            expected: Union[Dict, int]
            ) -> None:
        """ Test 'access_nested_map' output """
        self.assertEqual(access_nested_map(nested_map, path), expected)
    
    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])


    def test_access_nested_map_exception(
            self,
            nested_map: Dict[Any, Any],
            path: Tuple[str],
            expected: Type[Exception]
            ) -> None:
        """ Test "access_nested_map" for Keyerror """
        with self.assertRaises(expected):
            access_nested_map(nested_map, path)


