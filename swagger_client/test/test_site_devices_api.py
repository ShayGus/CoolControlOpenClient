# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import cool_open_client.client
from cool_open_client.client.api.site_devices_api import SiteDevicesApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestSiteDevicesApi(unittest.TestCase):
    """SiteDevicesApi unit test stubs"""

    def setUp(self):
        self.api = SiteDevicesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_sites_site_id_devices_get(self):
        """Test case for sites_site_id_devices_get

        get site devices  # noqa: E501
        """
        pass

    def test_sites_site_id_devices_post(self):
        """Test case for sites_site_id_devices_post

        add device to site  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
