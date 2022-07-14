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
from cool_open_client.client.api.customer_sites_api import CustomerSitesApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestCustomerSitesApi(unittest.TestCase):
    """CustomerSitesApi unit test stubs"""

    def setUp(self):
        self.api = CustomerSitesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_customer_id_sites_get(self):
        """Test case for customers_customer_id_sites_get

        get customer sites  # noqa: E501
        """
        pass

    def test_customers_customer_id_sites_post(self):
        """Test case for customers_customer_id_sites_post

        create customer site  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()