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
from cool_open_client.client.api.zone_units_api import ZoneUnitsApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestZoneUnitsApi(unittest.TestCase):
    """ZoneUnitsApi unit test stubs"""

    def setUp(self):
        self.api = ZoneUnitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_zones_zone_id_units_get(self):
        """Test case for zones_zone_id_units_get

        get zone units  # noqa: E501
        """
        pass

    def test_zones_zone_id_units_unit_id_delete(self):
        """Test case for zones_zone_id_units_unit_id_delete

        remove unit from zone  # noqa: E501
        """
        pass

    def test_zones_zone_id_units_unit_id_post(self):
        """Test case for zones_zone_id_units_unit_id_post

        add unit to zone  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
