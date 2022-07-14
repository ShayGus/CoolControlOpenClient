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

class CreateSiteRequestBody(object):
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
        'description': 'str',
        'country': 'str',
        'city': 'str',
        'postal_code': 'str',
        'address': 'str',
        'timezone': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'country': 'country',
        'city': 'city',
        'postal_code': 'postalCode',
        'address': 'address',
        'timezone': 'timezone'
    }

    def __init__(self, name=None, description=None, country=None, city=None, postal_code=None, address=None, timezone=None):  # noqa: E501
        """CreateSiteRequestBody - a model defined in Swagger"""  # noqa: E501
        self._name = None
        self._description = None
        self._country = None
        self._city = None
        self._postal_code = None
        self._address = None
        self._timezone = None
        self.discriminator = None
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
        self.timezone = timezone

    @property
    def name(self):
        """Gets the name of this CreateSiteRequestBody.  # noqa: E501

        site name  # noqa: E501

        :return: The name of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CreateSiteRequestBody.

        site name  # noqa: E501

        :param name: The name of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def description(self):
        """Gets the description of this CreateSiteRequestBody.  # noqa: E501

        site description  # noqa: E501

        :return: The description of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateSiteRequestBody.

        site description  # noqa: E501

        :param description: The description of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def country(self):
        """Gets the country of this CreateSiteRequestBody.  # noqa: E501

        site country address  # noqa: E501

        :return: The country of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CreateSiteRequestBody.

        site country address  # noqa: E501

        :param country: The country of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """

        self._country = country

    @property
    def city(self):
        """Gets the city of this CreateSiteRequestBody.  # noqa: E501

        site city address  # noqa: E501

        :return: The city of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CreateSiteRequestBody.

        site city address  # noqa: E501

        :param city: The city of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """

        self._city = city

    @property
    def postal_code(self):
        """Gets the postal_code of this CreateSiteRequestBody.  # noqa: E501

        site postal code address  # noqa: E501

        :return: The postal_code of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this CreateSiteRequestBody.

        site postal code address  # noqa: E501

        :param postal_code: The postal_code of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

    @property
    def address(self):
        """Gets the address of this CreateSiteRequestBody.  # noqa: E501

        site freetext address  # noqa: E501

        :return: The address of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CreateSiteRequestBody.

        site freetext address  # noqa: E501

        :param address: The address of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """

        self._address = address

    @property
    def timezone(self):
        """Gets the timezone of this CreateSiteRequestBody.  # noqa: E501

        site timezone  # noqa: E501

        :return: The timezone of this CreateSiteRequestBody.  # noqa: E501
        :rtype: str
        """
        return self._timezone

    @timezone.setter
    def timezone(self, timezone):
        """Sets the timezone of this CreateSiteRequestBody.

        site timezone  # noqa: E501

        :param timezone: The timezone of this CreateSiteRequestBody.  # noqa: E501
        :type: str
        """
        if timezone is None:
            raise ValueError("Invalid value for `timezone`, must not be `None`")  # noqa: E501

        self._timezone = timezone

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
        if issubclass(CreateSiteRequestBody, dict):
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
        if not isinstance(other, CreateSiteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
