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
from cool_open_client.client.api.unit_api import UnitApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestUnitApi(unittest.TestCase):
    """UnitApi unit test stubs"""

    def setUp(self):
        self.api = UnitApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_units_unit_id_get(self):
        """Test case for units_unit_id_get

        get unit  # noqa: E501
        """
        pass

    def test_units_unit_id_put(self):
        """Test case for units_unit_id_put

        update unit  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
