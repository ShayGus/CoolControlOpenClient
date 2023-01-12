# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 2.0.0
    Contact: info@coolautomation.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UsersResponse(object):
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
        'success': 'bool',
        'data': 'UsersResponseData'
    }

    attribute_map = {
        'success': 'success',
        'data': 'data'
    }

    def __init__(self, success=None, data=None):  # noqa: E501
        """UsersResponse - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._data = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if data is not None:
            self.data = data

    @property
    def success(self):
        """Gets the success of this UsersResponse.  # noqa: E501

        success status  # noqa: E501

        :return: The success of this UsersResponse.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this UsersResponse.

        success status  # noqa: E501

        :param success: The success of this UsersResponse.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def data(self):
        """Gets the data of this UsersResponse.  # noqa: E501


        :return: The data of this UsersResponse.  # noqa: E501
        :rtype: UsersResponseData
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this UsersResponse.


        :param data: The data of this UsersResponse.  # noqa: E501
        :type: UsersResponseData
        """

        self._data = data

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
        if issubclass(UsersResponse, dict):
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
        if not isinstance(other, UsersResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
