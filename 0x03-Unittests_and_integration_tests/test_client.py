#!/usr/bin/env python3
"""Test module for client module."""

import unittest
from unittest import mock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Test the github org client."""

    @parameterized.expand([("google",), ("abc",)])
    @mock.patch("client.get_json", return_value=TEST_PAYLOAD)
    def test_org(self, org: str, mocked: mock.Mock) -> None:
        """test that GithubOrgClient.org returns the correct value."""
        n_org = GithubOrgClient(org)
        self.assertEqual(n_org.org, TEST_PAYLOAD)
        mocked.assert_called_once()
