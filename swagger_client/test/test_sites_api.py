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
from cool_open_client.client.api.sites_api import SitesApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestSitesApi(unittest.TestCase):
    """SitesApi unit test stubs"""

    def setUp(self):
        self.api = SitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sites_get(self):
        """Test case for sites_get

        get my sites  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
