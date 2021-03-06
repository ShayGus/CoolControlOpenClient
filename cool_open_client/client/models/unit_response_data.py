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
        'role': 'object',
        'device': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'role': 'role',
        'device': 'device'
    }

    def __init__(self, id=None, name=None, role=None, device=None):  # noqa: E501
        """UnitResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._role = None
        self._device = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if role is not None:
            self.role = role
        if device is not None:
            self.device = device

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
    def role(self):
        """Gets the role of this UnitResponseData.  # noqa: E501

        caller permissions for this unit  # noqa: E501

        :return: The role of this UnitResponseData.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UnitResponseData.

        caller permissions for this unit  # noqa: E501

        :param role: The role of this UnitResponseData.  # noqa: E501
        :type: object
        """

        self._role = role

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
