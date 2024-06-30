#!/usr/bin/env python3
""" Test client module """
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """ Test github org client """
    @parameterized.expand([
        ("google",),
        ("abc",),
        ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """ test org """
        expected_result = {"org_name": org_name}
        mock_get_json.return_value = expected_result

        client = GithubOrgClient(org_name)
        self.assertEqual(client.org, expected_result)

        mock_get_json.assert_called_once_with(
                f"https://api.github.com/orgs/{org_name}")


if __name__ == '__main__':
    unittest.main()
