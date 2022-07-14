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

class UpdateUnitRequestBody(object):
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
        'name': 'str',
        'type': 'int',
        'supported_switch_modes': 'list[int]',
        'supported_modes': 'list[int]',
        'supported_fan_modes': 'list[int]',
        'supported_swing_modes': 'list[int]',
        'temperature_limits': 'object'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'supported_switch_modes': 'supportedSwitchModes',
        'supported_modes': 'supportedModes',
        'supported_fan_modes': 'supportedFanModes',
        'supported_swing_modes': 'supportedSwingModes',
        'temperature_limits': 'temperatureLimits'
    }

    def __init__(self, name=None, type=None, supported_switch_modes=None, supported_modes=None, supported_fan_modes=None, supported_swing_modes=None, temperature_limits=None):  # noqa: E501
        """UpdateUnitRequestBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._type = None
        self._supported_switch_modes = None
        self._supported_modes = None
        self._supported_fan_modes = None
        self._supported_swing_modes = None
        self._temperature_limits = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if supported_switch_modes is not None:
            self.supported_switch_modes = supported_switch_modes
        if supported_modes is not None:
            self.supported_modes = supported_modes
        if supported_fan_modes is not None:
            self.supported_fan_modes = supported_fan_modes
        if supported_swing_modes is not None:
            self.supported_swing_modes = supported_swing_modes
        if temperature_limits is not None:
            self.temperature_limits = temperature_limits

    @property
    def name(self):
        """Gets the name of this UpdateUnitRequestBody.  # noqa: E501

        unit name  # noqa: E501

        :return: The name of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateUnitRequestBody.

        unit name  # noqa: E501

        :param name: The name of this UpdateUnitRequestBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this UpdateUnitRequestBody.  # noqa: E501

        unit type from the unit type enumeration  # noqa: E501

        :return: The type of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this UpdateUnitRequestBody.

        unit type from the unit type enumeration  # noqa: E501

        :param type: The type of this UpdateUnitRequestBody.  # noqa: E501
        :type: int
        """

        self._type = type

    @property
    def supported_switch_modes(self):
        """Gets the supported_switch_modes of this UpdateUnitRequestBody.  # noqa: E501

        operation status the unit supports - array of integers from the operation status enumeration  # noqa: E501

        :return: The supported_switch_modes of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_switch_modes

    @supported_switch_modes.setter
    def supported_switch_modes(self, supported_switch_modes):
        """Sets the supported_switch_modes of this UpdateUnitRequestBody.

        operation status the unit supports - array of integers from the operation status enumeration  # noqa: E501

        :param supported_switch_modes: The supported_switch_modes of this UpdateUnitRequestBody.  # noqa: E501
        :type: list[int]
        """

        self._supported_switch_modes = supported_switch_modes

    @property
    def supported_modes(self):
        """Gets the supported_modes of this UpdateUnitRequestBody.  # noqa: E501

        operation modes the unit supports - array of integers from the operation modes enumeration  # noqa: E501

        :return: The supported_modes of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_modes

    @supported_modes.setter
    def supported_modes(self, supported_modes):
        """Sets the supported_modes of this UpdateUnitRequestBody.

        operation modes the unit supports - array of integers from the operation modes enumeration  # noqa: E501

        :param supported_modes: The supported_modes of this UpdateUnitRequestBody.  # noqa: E501
        :type: list[int]
        """

        self._supported_modes = supported_modes

    @property
    def supported_fan_modes(self):
        """Gets the supported_fan_modes of this UpdateUnitRequestBody.  # noqa: E501

        fan modes the unit supports - array of integers from the fan modes enumeration  # noqa: E501

        :return: The supported_fan_modes of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_fan_modes

    @supported_fan_modes.setter
    def supported_fan_modes(self, supported_fan_modes):
        """Sets the supported_fan_modes of this UpdateUnitRequestBody.

        fan modes the unit supports - array of integers from the fan modes enumeration  # noqa: E501

        :param supported_fan_modes: The supported_fan_modes of this UpdateUnitRequestBody.  # noqa: E501
        :type: list[int]
        """

        self._supported_fan_modes = supported_fan_modes

    @property
    def supported_swing_modes(self):
        """Gets the supported_swing_modes of this UpdateUnitRequestBody.  # noqa: E501

        swing modes the unit supports - array of integers from the swing modes enumeration  # noqa: E501

        :return: The supported_swing_modes of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_swing_modes

    @supported_swing_modes.setter
    def supported_swing_modes(self, supported_swing_modes):
        """Sets the supported_swing_modes of this UpdateUnitRequestBody.

        swing modes the unit supports - array of integers from the swing modes enumeration  # noqa: E501

        :param supported_swing_modes: The supported_swing_modes of this UpdateUnitRequestBody.  # noqa: E501
        :type: list[int]
        """

        self._supported_swing_modes = supported_swing_modes

    @property
    def temperature_limits(self):
        """Gets the temperature_limits of this UpdateUnitRequestBody.  # noqa: E501

        TBD  # noqa: E501

        :return: The temperature_limits of this UpdateUnitRequestBody.  # noqa: E501
        :rtype: object
        """
        return self._temperature_limits

    @temperature_limits.setter
    def temperature_limits(self, temperature_limits):
        """Sets the temperature_limits of this UpdateUnitRequestBody.

        TBD  # noqa: E501

        :param temperature_limits: The temperature_limits of this UpdateUnitRequestBody.  # noqa: E501
        :type: object
        """

        self._temperature_limits = temperature_limits

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
        if issubclass(UpdateUnitRequestBody, dict):
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
        if not isinstance(other, UpdateUnitRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
