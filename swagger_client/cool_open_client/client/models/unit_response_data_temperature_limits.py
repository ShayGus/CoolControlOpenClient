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

class UnitResponseDataTemperatureLimits(object):
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
        '_0': 'list[int]',
        '_1': 'list[int]',
        '_2': 'list[int]'
    }

    attribute_map = {
        '_0': '0',
        '_1': '1',
        '_2': '2'
    }

    def __init__(self, _0=None, _1=None, _2=None):  # noqa: E501
        """UnitResponseDataTemperatureLimits - a model defined in Swagger"""  # noqa: E501
        self.__0 = None
        self.__1 = None
        self.__2 = None
        self.discriminator = None
        if _0 is not None:
            self._0 = _0
        if _1 is not None:
            self._1 = _1
        if _2 is not None:
            self._2 = _2

    @property
    def _0(self):
        """Gets the _0 of this UnitResponseDataTemperatureLimits.  # noqa: E501


        :return: The _0 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :rtype: list[int]
        """
        return self.__0

    @_0.setter
    def _0(self, _0):
        """Sets the _0 of this UnitResponseDataTemperatureLimits.


        :param _0: The _0 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :type: list[int]
        """

        self.__0 = _0

    @property
    def _1(self):
        """Gets the _1 of this UnitResponseDataTemperatureLimits.  # noqa: E501


        :return: The _1 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :rtype: list[int]
        """
        return self.__1

    @_1.setter
    def _1(self, _1):
        """Sets the _1 of this UnitResponseDataTemperatureLimits.


        :param _1: The _1 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :type: list[int]
        """

        self.__1 = _1

    @property
    def _2(self):
        """Gets the _2 of this UnitResponseDataTemperatureLimits.  # noqa: E501


        :return: The _2 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :rtype: list[int]
        """
        return self.__2

    @_2.setter
    def _2(self, _2):
        """Sets the _2 of this UnitResponseDataTemperatureLimits.


        :param _2: The _2 of this UnitResponseDataTemperatureLimits.  # noqa: E501
        :type: list[int]
        """

        self.__2 = _2

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
        if issubclass(UnitResponseDataTemperatureLimits, dict):
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
        if not isinstance(other, UnitResponseDataTemperatureLimits):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other