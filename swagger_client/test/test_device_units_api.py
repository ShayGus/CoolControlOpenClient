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
from cool_open_client.client.api.device_units_api import DeviceUnitsApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestDeviceUnitsApi(unittest.TestCase):
    """DeviceUnitsApi unit test stubs"""

    def setUp(self):
        self.api = DeviceUnitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_devices_device_id_units_get(self):
        """Test case for devices_device_id_units_get

        get device units  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
