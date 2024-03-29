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

class UserResponseData(object):
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
        'username': 'str',
        'email': 'str',
        'phone': 'str',
        'role': 'object',
        'permissions': 'object'
    }

    attribute_map = {
        'id': 'id',
        'username': 'username',
        'email': 'email',
        'phone': 'phone',
        'role': 'role',
        'permissions': 'permissions'
    }

    def __init__(self, id=None, username=None, email=None, phone=None, role=None, permissions=None):  # noqa: E501
        """UserResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._username = None
        self._email = None
        self._phone = None
        self._role = None
        self._permissions = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if username is not None:
            self.username = username
        if email is not None:
            self.email = email
        if phone is not None:
            self.phone = phone
        if role is not None:
            self.role = role
        if permissions is not None:
            self.permissions = permissions

    @property
    def id(self):
        """Gets the id of this UserResponseData.  # noqa: E501

        user ID  # noqa: E501

        :return: The id of this UserResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserResponseData.

        user ID  # noqa: E501

        :param id: The id of this UserResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def username(self):
        """Gets the username of this UserResponseData.  # noqa: E501

        user identifier  # noqa: E501

        :return: The username of this UserResponseData.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this UserResponseData.

        user identifier  # noqa: E501

        :param username: The username of this UserResponseData.  # noqa: E501
        :type: str
        """

        self._username = username

    @property
    def email(self):
        """Gets the email of this UserResponseData.  # noqa: E501

        user email  # noqa: E501

        :return: The email of this UserResponseData.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this UserResponseData.

        user email  # noqa: E501

        :param email: The email of this UserResponseData.  # noqa: E501
        :type: str
        """

        self._email = email

    @property
    def phone(self):
        """Gets the phone of this UserResponseData.  # noqa: E501

        user phone number  # noqa: E501

        :return: The phone of this UserResponseData.  # noqa: E501
        :rtype: str
        """
        return self._phone

    @phone.setter
    def phone(self, phone):
        """Sets the phone of this UserResponseData.

        user phone number  # noqa: E501

        :param phone: The phone of this UserResponseData.  # noqa: E501
        :type: str
        """

        self._phone = phone

    @property
    def role(self):
        """Gets the role of this UserResponseData.  # noqa: E501

        caller permissions for this user  # noqa: E501

        :return: The role of this UserResponseData.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserResponseData.

        caller permissions for this user  # noqa: E501

        :param role: The role of this UserResponseData.  # noqa: E501
        :type: object
        """

        self._role = role

    @property
    def permissions(self):
        """Gets the permissions of this UserResponseData.  # noqa: E501

        user permissions  # noqa: E501

        :return: The permissions of this UserResponseData.  # noqa: E501
        :rtype: object
        """
        return self._permissions

    @permissions.setter
    def permissions(self, permissions):
        """Sets the permissions of this UserResponseData.

        user permissions  # noqa: E501

        :param permissions: The permissions of this UserResponseData.  # noqa: E501
        :type: object
        """

        self._permissions = permissions

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
        if issubclass(UserResponseData, dict):
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
        if not isinstance(other, UserResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
