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

class CustomerResponseData(object):
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
        'description': 'str',
        'role': 'object',
        'sites': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'role': 'role',
        'sites': 'sites'
    }

    def __init__(self, id=None, name=None, description=None, role=None, sites=None):  # noqa: E501
        """CustomerResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._role = None
        self._sites = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if role is not None:
            self.role = role
        if sites is not None:
            self.sites = sites

    @property
    def id(self):
        """Gets the id of this CustomerResponseData.  # noqa: E501

        customer ID  # noqa: E501

        :return: The id of this CustomerResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerResponseData.

        customer ID  # noqa: E501

        :param id: The id of this CustomerResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this CustomerResponseData.  # noqa: E501

        customer name  # noqa: E501

        :return: The name of this CustomerResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CustomerResponseData.

        customer name  # noqa: E501

        :param name: The name of this CustomerResponseData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this CustomerResponseData.  # noqa: E501

        customer descriptions  # noqa: E501

        :return: The description of this CustomerResponseData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomerResponseData.

        customer descriptions  # noqa: E501

        :param description: The description of this CustomerResponseData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def role(self):
        """Gets the role of this CustomerResponseData.  # noqa: E501

        caller permissions for this customer  # noqa: E501

        :return: The role of this CustomerResponseData.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this CustomerResponseData.

        caller permissions for this customer  # noqa: E501

        :param role: The role of this CustomerResponseData.  # noqa: E501
        :type: object
        """

        self._role = role

    @property
    def sites(self):
        """Gets the sites of this CustomerResponseData.  # noqa: E501

        array of child site IDs  # noqa: E501

        :return: The sites of this CustomerResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._sites

    @sites.setter
    def sites(self, sites):
        """Sets the sites of this CustomerResponseData.

        array of child site IDs  # noqa: E501

        :param sites: The sites of this CustomerResponseData.  # noqa: E501
        :type: list[str]
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
        if issubclass(CustomerResponseData, dict):
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
        if not isinstance(other, CustomerResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
