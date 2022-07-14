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

class SiteResponseData(object):
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
        'country': 'str',
        'city': 'str',
        'postal_code': 'str',
        'address': 'str',
        'timezone': 'str',
        'customer': 'str',
        'devices': 'list[str]',
        'zones': 'list[str]',
        'systems': 'list[str]',
        'role': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'country': 'country',
        'city': 'city',
        'postal_code': 'postalCode',
        'address': 'address',
        'timezone': 'timezone',
        'customer': 'customer',
        'devices': 'devices',
        'zones': 'zones',
        'systems': 'systems',
        'role': 'role'
    }

    def __init__(self, id=None, name=None, description=None, country=None, city=None, postal_code=None, address=None, timezone=None, customer=None, devices=None, zones=None, systems=None, role=None):  # noqa: E501
        """SiteResponseData - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._description = None
        self._country = None
        self._city = None
        self._postal_code = None
        self._address = None
        self._timezone = None
        self._customer = None
        self._devices = None
        self._zones = None
        self._systems = None
        self._role = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if country is not None:
            self.country = country
        if city is not None:
            self.city = city
        if postal_code is not None:
            self.postal_code = postal_code
        if address is not None:
            self.address = address
        if timezone is not None:
            self.timezone = timezone
        if customer is not None:
            self.customer = customer
        if devices is not None:
            self.devices = devices
        if zones is not None:
            self.zones = zones
        if systems is not None:
            self.systems = systems
        if role is not None:
            self.role = role

    @property
    def id(self):
        """Gets the id of this SiteResponseData.  # noqa: E501

        site ID  # noqa: E501

        :return: The id of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SiteResponseData.

        site ID  # noqa: E501

        :param id: The id of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this SiteResponseData.  # noqa: E501

        site name  # noqa: E501

        :return: The name of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SiteResponseData.

        site name  # noqa: E501

        :param name: The name of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this SiteResponseData.  # noqa: E501

        site description  # noqa: E501

        :return: The description of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SiteResponseData.

        site description  # noqa: E501

        :param description: The description of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def country(self):
        """Gets the country of this SiteResponseData.  # noqa: E501

        site address - country  # noqa: E501

        :return: The country of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SiteResponseData.

        site address - country  # noqa: E501

        :param country: The country of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city(self):
        """Gets the city of this SiteResponseData.  # noqa: E501

        site address - city  # noqa: E501

        :return: The city of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SiteResponseData.

        site address - city  # noqa: E501

        :param city: The city of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this SiteResponseData.  # noqa: E501

        site address - postal code  # noqa: E501

        :return: The postal_code of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this SiteResponseData.

        site address - postal code  # noqa: E501

        :param postal_code: The postal_code of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def address(self):
        """Gets the address of this SiteResponseData.  # noqa: E501

        site address - freeform text  # noqa: E501

        :return: The address of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this SiteResponseData.

        site address - freeform text  # noqa: E501

        :param address: The address of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def timezone(self):
        """Gets the timezone of this SiteResponseData.  # noqa: E501

        site timezone  # noqa: E501

        :return: The timezone of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this SiteResponseData.

        site timezone  # noqa: E501

        :param timezone: The timezone of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._timezone = timezone

    @property
    def customer(self):
        """Gets the customer of this SiteResponseData.  # noqa: E501

        parent customer id  # noqa: E501

        :return: The customer of this SiteResponseData.  # noqa: E501
        :rtype: str
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this SiteResponseData.

        parent customer id  # noqa: E501

        :param customer: The customer of this SiteResponseData.  # noqa: E501
        :type: str
        """

        self._customer = customer

    @property
    def devices(self):
        """Gets the devices of this SiteResponseData.  # noqa: E501

        array of child device IDs  # noqa: E501

        :return: The devices of this SiteResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._devices

    @devices.setter
    def devices(self, devices):
        """Sets the devices of this SiteResponseData.

        array of child device IDs  # noqa: E501

        :param devices: The devices of this SiteResponseData.  # noqa: E501
        :type: list[str]
        """

        self._devices = devices

    @property
    def zones(self):
        """Gets the zones of this SiteResponseData.  # noqa: E501

        array of child zone IDs  # noqa: E501

        :return: The zones of this SiteResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._zones

    @zones.setter
    def zones(self, zones):
        """Sets the zones of this SiteResponseData.

        array of child zone IDs  # noqa: E501

        :param zones: The zones of this SiteResponseData.  # noqa: E501
        :type: list[str]
        """

        self._zones = zones

    @property
    def systems(self):
        """Gets the systems of this SiteResponseData.  # noqa: E501

        array of child system IDs  # noqa: E501

        :return: The systems of this SiteResponseData.  # noqa: E501
        :rtype: list[str]
        """
        return self._systems

    @systems.setter
    def systems(self, systems):
        """Sets the systems of this SiteResponseData.

        array of child system IDs  # noqa: E501

        :param systems: The systems of this SiteResponseData.  # noqa: E501
        :type: list[str]
        """

        self._systems = systems

    @property
    def role(self):
        """Gets the role of this SiteResponseData.  # noqa: E501

        caller permissions for this site  # noqa: E501

        :return: The role of this SiteResponseData.  # noqa: E501
        :rtype: object
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this SiteResponseData.

        caller permissions for this site  # noqa: E501

        :param role: The role of this SiteResponseData.  # noqa: E501
        :type: object
        """

        self._role = role

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
        if issubclass(SiteResponseData, dict):
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
        if not isinstance(other, SiteResponseData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other