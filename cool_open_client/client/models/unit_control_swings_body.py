# coding: utf-8

"""
    OpenClientCoolAutomationAPI

    Cool platform REST API  # noqa: E501

    OpenAPI spec version: 2.0.1
    Contact: none@gmail.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UnitControlSwingsBody(object):
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
        'swing_mode': 'int'
    }

    attribute_map = {
        'swing_mode': 'swingMode'
    }

    def __init__(self, swing_mode=None):  # noqa: E501
        """UnitControlSwingsBody - a model defined in Swagger"""  # noqa: E501
        self._swing_mode = None
        self.discriminator = None
        self.swing_mode = swing_mode

    @property
    def swing_mode(self):
        """Gets the swing_mode of this UnitControlSwingsBody.  # noqa: E501

        requested operation status from the swing mode enumeration  # noqa: E501

        :return: The swing_mode of this UnitControlSwingsBody.  # noqa: E501
        :rtype: int
        """
        return self._swing_mode

    @swing_mode.setter
    def swing_mode(self, swing_mode):
        """Sets the swing_mode of this UnitControlSwingsBody.

        requested operation status from the swing mode enumeration  # noqa: E501

        :param swing_mode: The swing_mode of this UnitControlSwingsBody.  # noqa: E501
        :type: int
        """
        if swing_mode is None:
            raise ValueError("Invalid value for `swing_mode`, must not be `None`")  # noqa: E501

        self._swing_mode = swing_mode

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
        if issubclass(UnitControlSwingsBody, dict):
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
        if not isinstance(other, UnitControlSwingsBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
