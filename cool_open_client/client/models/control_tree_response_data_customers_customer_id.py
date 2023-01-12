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

class ControlTreeResponseDataCustomersCustomerId(object):
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
        'id': 'str',
        'role': 'str',
        'sites': 'ControlTreeResponseDataCustomersCustomerIdSites'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'role': 'role',
        'sites': 'sites'
    }

    def __init__(self, name=None, id=None, role=None, sites=None):  # noqa: E501
        """ControlTreeResponseDataCustomersCustomerId - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._id = None
        self._role = None
        self._sites = None
        self.discriminator = None
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if role is not None:
            self.role = role
        if sites is not None:
            self.sites = sites

    @property
    def name(self):
        """Gets the name of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501

        customer name  # noqa: E501

        :return: The name of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ControlTreeResponseDataCustomersCustomerId.

        customer name  # noqa: E501

        :param name: The name of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def id(self):
        """Gets the id of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501

        customer id  # noqa: E501

        :return: The id of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ControlTreeResponseDataCustomersCustomerId.

        customer id  # noqa: E501

        :param id: The id of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def role(self):
        """Gets the role of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501

        user role for this customer  # noqa: E501

        :return: The role of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :rtype: str
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this ControlTreeResponseDataCustomersCustomerId.

        user role for this customer  # noqa: E501

        :param role: The role of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :type: str
        """

        self._role = role

    @property
    def sites(self):
        """Gets the sites of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501


        :return: The sites of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :rtype: ControlTreeResponseDataCustomersCustomerIdSites
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this ControlTreeResponseDataCustomersCustomerId.


        :param sites: The sites of this ControlTreeResponseDataCustomersCustomerId.  # noqa: E501
        :type: ControlTreeResponseDataCustomersCustomerIdSites
        """

        self._sites = sites

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
        if issubclass(ControlTreeResponseDataCustomersCustomerId, dict):
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
        if not isinstance(other, ControlTreeResponseDataCustomersCustomerId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
