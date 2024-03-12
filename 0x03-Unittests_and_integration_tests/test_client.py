#!/usr/bin/env python3
"""
Unittest for test_access_nested([..])
"""

import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    def test_public_repos_url(self):
        """test public repo url"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as mock:
            response = {"repos_url": "mock_repo_url"}

            mock.return_value = response

            test_class = GithubOrgClient("test_repo_name")

            result = test_class._public_repos_url
            self.assertEqual(result, response["repos_url"])

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """test public repos"""
        payload = [{"name": "google"}, {"name": "abc"}]
        mock.return_value = payload

        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock_public:

            mock_public.return_value = "mock/repo"
            test_class = GithubOrgClient("test_repo_name")
            response = test_class.public_repos()

            repos_names = list(map(lambda repo: repo["name"], payload))
            self.assertEqual(response, repos_names)

            mock_public.assert_called_once()
            mock.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """test has_license"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """TestIntegrationGithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """setup"""
        config = {"return_value.json.side_effect":
                  [
                    cls.org_payload, cls.repos_payload,
                    cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch("requests.get", **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """test public repos"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """test_public_repos_with_license"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """tearDownClass: stop patcher"""
        cls.get_patcher.stop()


if __name__ == "__main__":
    unittest.main()
