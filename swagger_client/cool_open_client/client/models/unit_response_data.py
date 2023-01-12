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

class UnitResponseData(object):
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
        'id': 'str',
        'name': 'str',
        'device': 'str',
        'is_connected': 'bool',
        'supported_operation_statuses': 'list[int]',
        'supported_operation_modes': 'list[int]',
        'supported_fan_modes': 'list[int]',
        'supported_swing_modes': 'list[int]',
        'temperature_limits': 'UnitResponseDataTemperatureLimits',
        'brand': 'int',
        'active_setpoint': 'int',
        'ambient_temperature': 'int',
        'active_operation_status': 'int',
        'active_operation_mode': 'int',
        'active_fan_mode': 'int',
        'active_swing_mode': 'int',
        'filter': 'bool',
        'enable_cool_mode': 'bool',
        'enable_heat_mode': 'bool',
        'enable_auto_mode': 'bool',
        'is_half_c_degree_enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'device': 'device',
        'is_connected': 'isConnected',
        'supported_operation_statuses': 'supportedOperationStatuses',
        'supported_operation_modes': 'supportedOperationModes',
        'supported_fan_modes': 'supportedFanModes',
        'supported_swing_modes': 'supportedSwingModes',
        'temperature_limits': 'temperatureLimits',
        'brand': 'brand',
        'active_setpoint': 'activeSetpoint',
        'ambient_temperature': 'ambientTemperature',
        'active_operation_status': 'activeOperationStatus',
        'active_operation_mode': 'activeOperationMode',
        'active_fan_mode': 'activeFanMode',
        'active_swing_mode': 'activeSwingMode',
        'filter': 'filter',
        'enable_cool_mode': 'enableCoolMode',
        'enable_heat_mode': 'enableHeatMode',
        'enable_auto_mode': 'enableAutoMode',
        'is_half_c_degree_enabled': 'isHalfCDegreeEnabled'
    }

    def __init__(self, id=None, name=None, device=None, is_connected=None, supported_operation_statuses=None, supported_operation_modes=None, supported_fan_modes=None, supported_swing_modes=None, temperature_limits=None, brand=None, active_setpoint=None, ambient_temperature=None, active_operation_status=None, active_operation_mode=None, active_fan_mode=None, active_swing_mode=None, filter=None, enable_cool_mode=None, enable_heat_mode=None, enable_auto_mode=None, is_half_c_degree_enabled=None):  # noqa: E501
        """UnitResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._device = None
        self._is_connected = None
        self._supported_operation_statuses = None
        self._supported_operation_modes = None
        self._supported_fan_modes = None
        self._supported_swing_modes = None
        self._temperature_limits = None
        self._brand = None
        self._active_setpoint = None
        self._ambient_temperature = None
        self._active_operation_status = None
        self._active_operation_mode = None
        self._active_fan_mode = None
        self._active_swing_mode = None
        self._filter = None
        self._enable_cool_mode = None
        self._enable_heat_mode = None
        self._enable_auto_mode = None
        self._is_half_c_degree_enabled = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if device is not None:
            self.device = device
        if is_connected is not None:
            self.is_connected = is_connected
        if supported_operation_statuses is not None:
            self.supported_operation_statuses = supported_operation_statuses
        if supported_operation_modes is not None:
            self.supported_operation_modes = supported_operation_modes
        if supported_fan_modes is not None:
            self.supported_fan_modes = supported_fan_modes
        if supported_swing_modes is not None:
            self.supported_swing_modes = supported_swing_modes
        if temperature_limits is not None:
            self.temperature_limits = temperature_limits
        if brand is not None:
            self.brand = brand
        if active_setpoint is not None:
            self.active_setpoint = active_setpoint
        if ambient_temperature is not None:
            self.ambient_temperature = ambient_temperature
        if active_operation_status is not None:
            self.active_operation_status = active_operation_status
        if active_operation_mode is not None:
            self.active_operation_mode = active_operation_mode
        if active_fan_mode is not None:
            self.active_fan_mode = active_fan_mode
        if active_swing_mode is not None:
            self.active_swing_mode = active_swing_mode
        if filter is not None:
            self.filter = filter
        if enable_cool_mode is not None:
            self.enable_cool_mode = enable_cool_mode
        if enable_heat_mode is not None:
            self.enable_heat_mode = enable_heat_mode
        if enable_auto_mode is not None:
            self.enable_auto_mode = enable_auto_mode
        if is_half_c_degree_enabled is not None:
            self.is_half_c_degree_enabled = is_half_c_degree_enabled

    @property
    def id(self):
        """Gets the id of this UnitResponseData.  # noqa: E501

        unit ID  # noqa: E501

        :return: The id of this UnitResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UnitResponseData.

        unit ID  # noqa: E501

        :param id: The id of this UnitResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this UnitResponseData.  # noqa: E501

        system name  # noqa: E501

        :return: The name of this UnitResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UnitResponseData.

        system name  # noqa: E501

        :param name: The name of this UnitResponseData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def device(self):
        """Gets the device of this UnitResponseData.  # noqa: E501

        parent device id  # noqa: E501

        :return: The device of this UnitResponseData.  # noqa: E501
        :rtype: str
        """
        return self._device

    @device.setter
    def device(self, device):
        """Sets the device of this UnitResponseData.

        parent device id  # noqa: E501

        :param device: The device of this UnitResponseData.  # noqa: E501
        :type: str
        """

        self._device = device

    @property
    def is_connected(self):
        """Gets the is_connected of this UnitResponseData.  # noqa: E501

        Is unit connected  # noqa: E501

        :return: The is_connected of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._is_connected

    @is_connected.setter
    def is_connected(self, is_connected):
        """Sets the is_connected of this UnitResponseData.

        Is unit connected  # noqa: E501

        :param is_connected: The is_connected of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._is_connected = is_connected

    @property
    def supported_operation_statuses(self):
        """Gets the supported_operation_statuses of this UnitResponseData.  # noqa: E501

        Supported operation statuses  # noqa: E501

        :return: The supported_operation_statuses of this UnitResponseData.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_operation_statuses

    @supported_operation_statuses.setter
    def supported_operation_statuses(self, supported_operation_statuses):
        """Sets the supported_operation_statuses of this UnitResponseData.

        Supported operation statuses  # noqa: E501

        :param supported_operation_statuses: The supported_operation_statuses of this UnitResponseData.  # noqa: E501
        :type: list[int]
        """

        self._supported_operation_statuses = supported_operation_statuses

    @property
    def supported_operation_modes(self):
        """Gets the supported_operation_modes of this UnitResponseData.  # noqa: E501

        Supported operation modes  # noqa: E501

        :return: The supported_operation_modes of this UnitResponseData.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_operation_modes

    @supported_operation_modes.setter
    def supported_operation_modes(self, supported_operation_modes):
        """Sets the supported_operation_modes of this UnitResponseData.

        Supported operation modes  # noqa: E501

        :param supported_operation_modes: The supported_operation_modes of this UnitResponseData.  # noqa: E501
        :type: list[int]
        """

        self._supported_operation_modes = supported_operation_modes

    @property
    def supported_fan_modes(self):
        """Gets the supported_fan_modes of this UnitResponseData.  # noqa: E501

        Supported fan modes  # noqa: E501

        :return: The supported_fan_modes of this UnitResponseData.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_fan_modes

    @supported_fan_modes.setter
    def supported_fan_modes(self, supported_fan_modes):
        """Sets the supported_fan_modes of this UnitResponseData.

        Supported fan modes  # noqa: E501

        :param supported_fan_modes: The supported_fan_modes of this UnitResponseData.  # noqa: E501
        :type: list[int]
        """

        self._supported_fan_modes = supported_fan_modes

    @property
    def supported_swing_modes(self):
        """Gets the supported_swing_modes of this UnitResponseData.  # noqa: E501

        Supported swing modes  # noqa: E501

        :return: The supported_swing_modes of this UnitResponseData.  # noqa: E501
        :rtype: list[int]
        """
        return self._supported_swing_modes

    @supported_swing_modes.setter
    def supported_swing_modes(self, supported_swing_modes):
        """Sets the supported_swing_modes of this UnitResponseData.

        Supported swing modes  # noqa: E501

        :param supported_swing_modes: The supported_swing_modes of this UnitResponseData.  # noqa: E501
        :type: list[int]
        """

        self._supported_swing_modes = supported_swing_modes

    @property
    def temperature_limits(self):
        """Gets the temperature_limits of this UnitResponseData.  # noqa: E501


        :return: The temperature_limits of this UnitResponseData.  # noqa: E501
        :rtype: UnitResponseDataTemperatureLimits
        """
        return self._temperature_limits

    @temperature_limits.setter
    def temperature_limits(self, temperature_limits):
        """Sets the temperature_limits of this UnitResponseData.


        :param temperature_limits: The temperature_limits of this UnitResponseData.  # noqa: E501
        :type: UnitResponseDataTemperatureLimits
        """

        self._temperature_limits = temperature_limits

    @property
    def brand(self):
        """Gets the brand of this UnitResponseData.  # noqa: E501


        :return: The brand of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this UnitResponseData.


        :param brand: The brand of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._brand = brand

    @property
    def active_setpoint(self):
        """Gets the active_setpoint of this UnitResponseData.  # noqa: E501


        :return: The active_setpoint of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._active_setpoint

    @active_setpoint.setter
    def active_setpoint(self, active_setpoint):
        """Sets the active_setpoint of this UnitResponseData.


        :param active_setpoint: The active_setpoint of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._active_setpoint = active_setpoint

    @property
    def ambient_temperature(self):
        """Gets the ambient_temperature of this UnitResponseData.  # noqa: E501


        :return: The ambient_temperature of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._ambient_temperature

    @ambient_temperature.setter
    def ambient_temperature(self, ambient_temperature):
        """Sets the ambient_temperature of this UnitResponseData.


        :param ambient_temperature: The ambient_temperature of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._ambient_temperature = ambient_temperature

    @property
    def active_operation_status(self):
        """Gets the active_operation_status of this UnitResponseData.  # noqa: E501


        :return: The active_operation_status of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._active_operation_status

    @active_operation_status.setter
    def active_operation_status(self, active_operation_status):
        """Sets the active_operation_status of this UnitResponseData.


        :param active_operation_status: The active_operation_status of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._active_operation_status = active_operation_status

    @property
    def active_operation_mode(self):
        """Gets the active_operation_mode of this UnitResponseData.  # noqa: E501


        :return: The active_operation_mode of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._active_operation_mode

    @active_operation_mode.setter
    def active_operation_mode(self, active_operation_mode):
        """Sets the active_operation_mode of this UnitResponseData.


        :param active_operation_mode: The active_operation_mode of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._active_operation_mode = active_operation_mode

    @property
    def active_fan_mode(self):
        """Gets the active_fan_mode of this UnitResponseData.  # noqa: E501


        :return: The active_fan_mode of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._active_fan_mode

    @active_fan_mode.setter
    def active_fan_mode(self, active_fan_mode):
        """Sets the active_fan_mode of this UnitResponseData.


        :param active_fan_mode: The active_fan_mode of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._active_fan_mode = active_fan_mode

    @property
    def active_swing_mode(self):
        """Gets the active_swing_mode of this UnitResponseData.  # noqa: E501


        :return: The active_swing_mode of this UnitResponseData.  # noqa: E501
        :rtype: int
        """
        return self._active_swing_mode

    @active_swing_mode.setter
    def active_swing_mode(self, active_swing_mode):
        """Sets the active_swing_mode of this UnitResponseData.


        :param active_swing_mode: The active_swing_mode of this UnitResponseData.  # noqa: E501
        :type: int
        """

        self._active_swing_mode = active_swing_mode

    @property
    def filter(self):
        """Gets the filter of this UnitResponseData.  # noqa: E501


        :return: The filter of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        """Sets the filter of this UnitResponseData.


        :param filter: The filter of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._filter = filter

    @property
    def enable_cool_mode(self):
        """Gets the enable_cool_mode of this UnitResponseData.  # noqa: E501


        :return: The enable_cool_mode of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_cool_mode

    @enable_cool_mode.setter
    def enable_cool_mode(self, enable_cool_mode):
        """Sets the enable_cool_mode of this UnitResponseData.


        :param enable_cool_mode: The enable_cool_mode of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._enable_cool_mode = enable_cool_mode

    @property
    def enable_heat_mode(self):
        """Gets the enable_heat_mode of this UnitResponseData.  # noqa: E501


        :return: The enable_heat_mode of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_heat_mode

    @enable_heat_mode.setter
    def enable_heat_mode(self, enable_heat_mode):
        """Sets the enable_heat_mode of this UnitResponseData.


        :param enable_heat_mode: The enable_heat_mode of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._enable_heat_mode = enable_heat_mode

    @property
    def enable_auto_mode(self):
        """Gets the enable_auto_mode of this UnitResponseData.  # noqa: E501


        :return: The enable_auto_mode of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._enable_auto_mode

    @enable_auto_mode.setter
    def enable_auto_mode(self, enable_auto_mode):
        """Sets the enable_auto_mode of this UnitResponseData.


        :param enable_auto_mode: The enable_auto_mode of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._enable_auto_mode = enable_auto_mode

    @property
    def is_half_c_degree_enabled(self):
        """Gets the is_half_c_degree_enabled of this UnitResponseData.  # noqa: E501


        :return: The is_half_c_degree_enabled of this UnitResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._is_half_c_degree_enabled

    @is_half_c_degree_enabled.setter
    def is_half_c_degree_enabled(self, is_half_c_degree_enabled):
        """Sets the is_half_c_degree_enabled of this UnitResponseData.


        :param is_half_c_degree_enabled: The is_half_c_degree_enabled of this UnitResponseData.  # noqa: E501
        :type: bool
        """

        self._is_half_c_degree_enabled = is_half_c_degree_enabled

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
        if issubclass(UnitResponseData, dict):
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
        if not isinstance(other, UnitResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
