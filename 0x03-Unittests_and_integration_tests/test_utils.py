#!/usr/bin/env python3
"""
Unittest for test_access_nested([..])
"""

import unittest
from parameterized import parameterized
from unittest import mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """test access_nested_map"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {'b': 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test return value"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("b", "b",)),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test get_json"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test return value"""
        response = {"return_value.json.return_value": test_payload}
        patcher = mock.patch("requests.get", **response)

        mock_call = patcher.start()

        self.assertEqual(get_json(test_url), test_payload)
        mock_call.assert_called_once()

        patcher.stop()


class TestMemoize(unittest.TestCase):
    """ Class for Testing Memoize """

    def test_memoize(self):
        """
        test that a_property called only once
        """

        class TestClass:
            """
            TestClass for memoize
            """

            def a_method(self):
                """non memoized test method"""
                return 42

            @memoize
            def a_property(self):
                """memoized test method"""
                return self.a_method()

        with mock.patch.object(TestClass, "a_method") as mk:
            test_class = TestClass()
            test_class.a_property()
            test_class.a_property()
            mk.assert_called_once()


if __name__ == "__main__":
    unittest.main()
