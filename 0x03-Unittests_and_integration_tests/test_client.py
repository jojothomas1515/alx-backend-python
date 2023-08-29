#!/usr/bin/env python3
"""Test module for client module."""

import unittest
from parameterized import (
    parameterized,
    parameterized_class)
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest.mock import (
    patch,
    Mock)


class TestGithubOrgClient(unittest.TestCase):
    """Test the github org client."""

    @parameterized.expand([("google",), ("abc",)])
    @patch("client.get_json", return_value=TEST_PAYLOAD)
    def test_org(self, org: str, mocked: Mock) -> None:
        """test that GithubOrgClient.org returns the correct value."""
        n_org = GithubOrgClient(org)
        self.assertEqual(n_org.org, TEST_PAYLOAD)
        mocked.assert_called_once()

    @patch("client.GithubOrgClient._public_repos_url",
           new_callable=mock.PropertyMock,
           return_value="jojothomas.repo")
    def test_public_repos_url(self, mocked):
        """Test public repo."""
        self.assertEqual(GithubOrgClient("abc")._public_repos_url,
                         "jojothomas.repo")

    @patch("client.get_json", return_value=TEST_PAYLOAD[0][1])
    @patch("client.GithubOrgClient._public_repos_url",
           new_callable=mock.PropertyMock,
           return_value="http://jojothomas.com")
    def test_public_repos(self, mocked: Mock, mk: Mock):
        """Test public repos."""

        self.assertEqual(GithubOrgClient("abc").public_repos(
            "bsd-3-clause"), ['episodes.dart'])
        mk.assert_called_once()
        mocked.assert_called_once()

    expand = [
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ]

    @parameterized.expand(expand)
    def test_has_license(self, repo, license_key, expected):
        """Testing the has license static method."""
        self.assertEqual(GithubOrgClient.has_license(
            repo, license_key), expected)


@parameterized_class([{
    "org_payload": TEST_PAYLOAD[0][0],
    "repos_payload":TEST_PAYLOAD[0][1],
    "expected_repos":TEST_PAYLOAD[0][2],
    "apache2_repos":TEST_PAYLOAD[0][3]
}])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for public repos method."""

    @classmethod
    def setUpClass(cls):
        """Preparation class method."""

        def side_effect(url):
            """side effect."""
            if url == "https://api.github.com/orgs/google":
                return Mock(**{"json.return_value": cls.org_payload})
            elif url == "https://api.github.com/orgs/google/repos":
                return Mock(**{"json.return_value": cls.repos_payload})
            else:
                return Mock(**{"json.return_value": []})

        cls.get_patcher: Mock = patch("requests.get",
                                      autospec=True,
                                      side_effect=side_effect)
        cls.get_patcher.start()

    def test_dummy(self):
        """Dummy test."""
        self.assertEqual(1, 1)

    @classmethod
    def tearDownClass(cls):
        """Cleanup class method."""
        cls.get_patcher.stop()
