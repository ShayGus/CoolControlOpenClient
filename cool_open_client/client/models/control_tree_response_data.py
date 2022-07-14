# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 1.0.2
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ControlTreeResponseData(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'customers': 'ControlTreeResponseDataCustomers'
    }

    attribute_map = {
        'customers': 'customers'
    }

    def __init__(self, customers=None):  # noqa: E501
        """ControlTreeResponseData - a model defined in Swagger"""  # noqa: E501
        self._customers = None
        self.discriminator = None
        if customers is not None:
            self.customers = customers

    @property
    def customers(self):
        """Gets the customers of this ControlTreeResponseData.  # noqa: E501


        :return: The customers of this ControlTreeResponseData.  # noqa: E501
        :rtype: ControlTreeResponseDataCustomers
        """
        return self._customers

    @customers.setter
    def customers(self, customers):
        """Sets the customers of this ControlTreeResponseData.


        :param customers: The customers of this ControlTreeResponseData.  # noqa: E501
        :type: ControlTreeResponseDataCustomers
        """

        self._customers = customers

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ControlTreeResponseData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ControlTreeResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
