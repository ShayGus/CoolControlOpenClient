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

class CreateDeviceRequestBody(object):
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
        'serial': 'str',
        'pin': 'str'
    }

    attribute_map = {
        'name': 'name',
        'serial': 'serial',
        'pin': 'pin'
    }

    def __init__(self, name=None, serial=None, pin=None):  # noqa: E501
        """CreateDeviceRequestBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._serial = None
        self._pin = None
        self.discriminator = None
        if name is not None:
            self.name = name
        self.serial = serial
        self.pin = pin

    @property
    def name(self):
        """Gets the name of this CreateDeviceRequestBody.  # noqa: E501

        device name  # noqa: E501

        :return: The name of this CreateDeviceRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateDeviceRequestBody.

        device name  # noqa: E501

        :param name: The name of this CreateDeviceRequestBody.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def serial(self):
        """Gets the serial of this CreateDeviceRequestBody.  # noqa: E501

        serial number of the device  # noqa: E501

        :return: The serial of this CreateDeviceRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._serial

    @serial.setter
    def serial(self, serial):
        """Sets the serial of this CreateDeviceRequestBody.

        serial number of the device  # noqa: E501

        :param serial: The serial of this CreateDeviceRequestBody.  # noqa: E501
        :type: str
        """
        if serial is None:
            raise ValueError("Invalid value for `serial`, must not be `None`")  # noqa: E501

        self._serial = serial

    @property
    def pin(self):
        """Gets the pin of this CreateDeviceRequestBody.  # noqa: E501

        device pin  # noqa: E501

        :return: The pin of this CreateDeviceRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._pin

    @pin.setter
    def pin(self, pin):
        """Sets the pin of this CreateDeviceRequestBody.

        device pin  # noqa: E501

        :param pin: The pin of this CreateDeviceRequestBody.  # noqa: E501
        :type: str
        """
        if pin is None:
            raise ValueError("Invalid value for `pin`, must not be `None`")  # noqa: E501

        self._pin = pin

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
        if issubclass(CreateDeviceRequestBody, dict):
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
        if not isinstance(other, CreateDeviceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
