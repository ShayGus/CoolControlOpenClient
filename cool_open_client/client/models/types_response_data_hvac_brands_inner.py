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

class TypesResponseDataHvacBrandsInner(object):
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
        'value': 'int',
        'type': 'str',
        'name': 'str',
        'is_water_heater': 'bool',
        'has_booster': 'bool'
    }

    attribute_map = {
        'value': 'value',
        'type': 'type',
        'name': 'name',
        'is_water_heater': 'isWaterHeater',
        'has_booster': 'hasBooster'
    }

    def __init__(self, value=None, type=None, name=None, is_water_heater=None, has_booster=None):  # noqa: E501
        """TypesResponseDataHvacBrandsInner - a model defined in Swagger"""  # noqa: E501
        self._value = None
        self._type = None
        self._name = None
        self._is_water_heater = None
        self._has_booster = None
        self.discriminator = None
        if value is not None:
            self.value = value
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if is_water_heater is not None:
            self.is_water_heater = is_water_heater
        if has_booster is not None:
            self.has_booster = has_booster

    @property
    def value(self):
        """Gets the value of this TypesResponseDataHvacBrandsInner.  # noqa: E501

        hvac type id  # noqa: E501

        :return: The value of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this TypesResponseDataHvacBrandsInner.

        hvac type id  # noqa: E501

        :param value: The value of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :type: int
        """

        self._value = value

    @property
    def type(self):
        """Gets the type of this TypesResponseDataHvacBrandsInner.  # noqa: E501

        Brand type  # noqa: E501

        :return: The type of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TypesResponseDataHvacBrandsInner.

        Brand type  # noqa: E501

        :param type: The type of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def name(self):
        """Gets the name of this TypesResponseDataHvacBrandsInner.  # noqa: E501

        Brand Name  # noqa: E501

        :return: The name of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TypesResponseDataHvacBrandsInner.

        Brand Name  # noqa: E501

        :param name: The name of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def is_water_heater(self):
        """Gets the is_water_heater of this TypesResponseDataHvacBrandsInner.  # noqa: E501

        Is the device water heater  # noqa: E501

        :return: The is_water_heater of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :rtype: bool
        """
        return self._is_water_heater

    @is_water_heater.setter
    def is_water_heater(self, is_water_heater):
        """Sets the is_water_heater of this TypesResponseDataHvacBrandsInner.

        Is the device water heater  # noqa: E501

        :param is_water_heater: The is_water_heater of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :type: bool
        """

        self._is_water_heater = is_water_heater

    @property
    def has_booster(self):
        """Gets the has_booster of this TypesResponseDataHvacBrandsInner.  # noqa: E501

        Does the device has booster  # noqa: E501

        :return: The has_booster of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :rtype: bool
        """
        return self._has_booster

    @has_booster.setter
    def has_booster(self, has_booster):
        """Sets the has_booster of this TypesResponseDataHvacBrandsInner.

        Does the device has booster  # noqa: E501

        :param has_booster: The has_booster of this TypesResponseDataHvacBrandsInner.  # noqa: E501
        :type: bool
        """

        self._has_booster = has_booster

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
        if issubclass(TypesResponseDataHvacBrandsInner, dict):
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
        if not isinstance(other, TypesResponseDataHvacBrandsInner):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
