"""Unittest for test_access_nested([..])
"""

import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """test access_nested_map"""

    def test_access_nested_map_no_params(self):
        """test no params"""
        with self.assertRaises(TypeError):
            access_nested_map()

    def test_access_nested_map_one_params(self):
        """test one params"""
        with self.assertRaises(TypeError):
            access_nested_map({})

    def test_access_nested_map_more_params(self):
        """test more params"""
        with self.assertRaises(TypeError):
            access_nested_map({}, [], "")

    def test_access_nested_wrong_param_type(self):
        """wrong param type"""
        with self.assertRaises(TypeError):
            access_nested_map({}, 1)

    def test_access_nested_map_simple_key(self):
        """simple key"""
        r = access_nested_map({"a": 1}, ["a"])
        self.assertEqual(r, 1)

    def test_access_nested_map_not_found_key(self):
        """not found key"""
        with self.assertRaises(KeyError):
            access_nested_map({"a": 1}, ["a", "b"])


if __name__ == "__main__":
    unittest.main()
