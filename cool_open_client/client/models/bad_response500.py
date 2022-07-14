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

class BadResponse500(object):
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
        'message': 'str'
    }

    attribute_map = {
        'success': 'success',
        'message': 'message'
    }

    def __init__(self, success=None, message=None):  # noqa: E501
        """BadResponse500 - a model defined in Swagger"""  # noqa: E501
        self._success = None
        self._message = None
        self.discriminator = None
        if success is not None:
            self.success = success
        if message is not None:
            self.message = message

    @property
    def success(self):
        """Gets the success of this BadResponse500.  # noqa: E501

        success status  # noqa: E501

        :return: The success of this BadResponse500.  # noqa: E501
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this BadResponse500.

        success status  # noqa: E501

        :param success: The success of this BadResponse500.  # noqa: E501
        :type: bool
        """

        self._success = success

    @property
    def message(self):
        """Gets the message of this BadResponse500.  # noqa: E501

        text message describing the error  # noqa: E501

        :return: The message of this BadResponse500.  # noqa: E501
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this BadResponse500.

        text message describing the error  # noqa: E501

        :param message: The message of this BadResponse500.  # noqa: E501
        :type: str
        """

        self._message = message

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
        if issubclass(BadResponse500, dict):
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
        if not isinstance(other, BadResponse500):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
