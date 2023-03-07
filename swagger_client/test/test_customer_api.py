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
from cool_open_client.client.api.customer_api import CustomerApi  # noqa: E501
from cool_open_client.client.rest import ApiException


class TestCustomerApi(unittest.TestCase):
    """CustomerApi unit test stubs"""

    def setUp(self):
        self.api = CustomerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_customers_customer_id_delete(self):
        """Test case for customers_customer_id_delete

        delete customer  # noqa: E501
        """
        pass

    def test_customers_customer_id_get(self):
        """Test case for customers_customer_id_get

        get customer  # noqa: E501
        """
        pass

    def test_customers_customer_id_post(self):
        """Test case for customers_customer_id_post

        create customer  # noqa: E501
        """
        pass

    def test_customers_customer_id_put(self):
        """Test case for customers_customer_id_put

        update customer  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
