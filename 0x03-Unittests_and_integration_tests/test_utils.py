#!/usr/bin/env python3
"""Test module for the util module."""

from unittest import TestCase, mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized


class TestAccessNestedMap(TestCase):
    """
    Test the functionality of access_nested_map.
    """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test with parameterized expand."""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b"),
    ])
    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test with parameterized expand."""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(TestCase):
    """
    Test the get json function.
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, expected):
        """Test get_json method behaviour.

        Path the request get method to return a mocked object
        with a json method.
        """
        mock_with_json = mock.MagicMock()
        mock_with_json.json = lambda: expected
        with mock.patch("requests.get", create=True,
                        return_value=mock_with_json,) as mocked:
            self.assertEqual(get_json(test_url), expected)
            mocked.assert_called_once_with(test_url)


class TestMemoize(TestCase):
    """Test the memoize method."""

    def test_memoize(self):
        """Check if test_memoize decorator works well."""
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with mock.patch.object(TestClass, "a_method",
                               return_value=42) as mocked:
            test_m = TestClass()
            self.assertEqual(test_m.a_property, 42)
            self.assertEqual(test_m.a_property, 42)
            mocked.assert_called_once()
