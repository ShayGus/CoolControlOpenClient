# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: none@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cool_open_client.client
from cool_open_client.client.api.user_api import UserApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestUserApi(unittest.TestCase):
    """UserApi unit test stubs"""

    def setUp(self):
        self.api = UserApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_users_user_id_delete(self):
        """Test case for users_user_id_delete

        delete user  # noqa: E501
        """
        pass

    def test_users_user_id_get(self):
        """Test case for users_user_id_get

        get user  # noqa: E501
        """
        pass

    def test_users_user_id_put(self):
        """Test case for users_user_id_put

        update user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
