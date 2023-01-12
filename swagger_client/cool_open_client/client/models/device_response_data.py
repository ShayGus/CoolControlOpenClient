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

class DeviceResponseData(object):
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
        'serial': 'str',
        'role': 'object',
        'site': 'str',
        'units': 'list[str]',
        'is_connected': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'serial': 'serial',
        'role': 'role',
        'site': 'site',
        'units': 'units',
        'is_connected': 'isConnected'
    }

    def __init__(self, id=None, serial=None, role=None, site=None, units=None, is_connected=None):  # noqa: E501
        """DeviceResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._serial = None
        self._role = None
        self._site = None
        self._units = None
        self._is_connected = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if serial is not None:
            self.serial = serial
        if role is not None:
            self.role = role
        if site is not None:
            self.site = site
        if units is not None:
            self.units = units
        if is_connected is not None:
            self.is_connected = is_connected

    @property
    def id(self):
        """Gets the id of this DeviceResponseData.  # noqa: E501

        device ID  # noqa: E501

        :return: The id of this DeviceResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeviceResponseData.

        device ID  # noqa: E501

        :param id: The id of this DeviceResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def serial(self):
        """Gets the serial of this DeviceResponseData.  # noqa: E501

        device serial number  # noqa: E501

        :return: The serial of this DeviceResponseData.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this DeviceResponseData.

        device serial number  # noqa: E501

        :param serial: The serial of this DeviceResponseData.  # noqa: E501
        :type: str
        """

        self._serial = serial

    @property
    def role(self):
        """Gets the role of this DeviceResponseData.  # noqa: E501

        caller permissions for this device  # noqa: E501

        :return: The role of this DeviceResponseData.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this DeviceResponseData.

        caller permissions for this device  # noqa: E501

        :param role: The role of this DeviceResponseData.  # noqa: E501
        :type: object
        """

        self._role = role

    @property
    def site(self):
        """Gets the site of this DeviceResponseData.  # noqa: E501

        parent site id  # noqa: E501

        :return: The site of this DeviceResponseData.  # noqa: E501
        :rtype: str
        """
        return self._site

    @site.setter
    def site(self, site):
        """Sets the site of this DeviceResponseData.

        parent site id  # noqa: E501

        :param site: The site of this DeviceResponseData.  # noqa: E501
        :type: str
        """

        self._site = site

    @property
    def units(self):
        """Gets the units of this DeviceResponseData.  # noqa: E501

        array of child unit IDs  # noqa: E501

        :return: The units of this DeviceResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._units

    @units.setter
    def units(self, units):
        """Sets the units of this DeviceResponseData.

        array of child unit IDs  # noqa: E501

        :param units: The units of this DeviceResponseData.  # noqa: E501
        :type: list[str]
        """

        self._units = units

    @property
    def is_connected(self):
        """Gets the is_connected of this DeviceResponseData.  # noqa: E501

        defines whether device connected  # noqa: E501

        :return: The is_connected of this DeviceResponseData.  # noqa: E501
        :rtype: bool
        """
        return self._is_connected

    @is_connected.setter
    def is_connected(self, is_connected):
        """Sets the is_connected of this DeviceResponseData.

        defines whether device connected  # noqa: E501

        :param is_connected: The is_connected of this DeviceResponseData.  # noqa: E501
        :type: bool
        """

        self._is_connected = is_connected

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
        if issubclass(DeviceResponseData, dict):
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
        if not isinstance(other, DeviceResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
