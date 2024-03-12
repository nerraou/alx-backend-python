#!/usr/bin/env python3
"""
Unittest for test_access_nested([..])
"""

import unittest
from parameterized import parameterized
from unittest.mock import patch
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test TestGithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch("client.get_json")
    def test_org(self, org_name, mock):
        """test return value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()

        url = f"https://api.github.com/orgs/{org_name}"
        mock.assert_called_once_with(url)


if __name__ == "__main__":
    unittest.main()
