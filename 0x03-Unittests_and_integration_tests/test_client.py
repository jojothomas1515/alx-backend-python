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

    @mock.patch("client.GithubOrgClient._public_repos_url",
                new_callable=mock.PropertyMock,
                return_value="jojothomas.repo")
    def test_public_repos_url(self, mocked):
        """Test public repo."""
        self.assertEqual(GithubOrgClient("abc")._public_repos_url,
                         "jojothomas.repo")

    payload = {"payload": True}

    @mock.patch("client.get_json", return_value=TEST_PAYLOAD[0][1])
    def test_public_repos(self, mocked: mock.Mock):
        """Test public repos."""
        with mock.patch("client.GithubOrgClient._public_repos_url",
                        new_callable=mock.PropertyMock,
                        return_value="http://jojothomas.repo") as mk:

            self.assertEqual(GithubOrgClient("abc").public_repos(
                "bsd-3-clause"), ['episodes.dart'])
            mk.assert_called_once()
        mocked.assert_called_once()
