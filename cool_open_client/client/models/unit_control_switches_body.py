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

class UnitControlSwitchesBody(object):
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
        'operation_status': 'int'
    }

    attribute_map = {
        'operation_status': 'operationStatus'
    }

    def __init__(self, operation_status=None):  # noqa: E501
        """UnitControlSwitchesBody - a model defined in Swagger"""  # noqa: E501
        self._operation_status = None
        self.discriminator = None
        self.operation_status = operation_status

    @property
    def operation_status(self):
        """Gets the operation_status of this UnitControlSwitchesBody.  # noqa: E501

        requested operation status from the operation status enumeration  # noqa: E501

        :return: The operation_status of this UnitControlSwitchesBody.  # noqa: E501
        :rtype: int
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """Sets the operation_status of this UnitControlSwitchesBody.

        requested operation status from the operation status enumeration  # noqa: E501

        :param operation_status: The operation_status of this UnitControlSwitchesBody.  # noqa: E501
        :type: int
        """
        if operation_status is None:
            raise ValueError("Invalid value for `operation_status`, must not be `None`")  # noqa: E501
        allowed_values = [1, 2]  # noqa: E501
        if operation_status not in allowed_values:
            raise ValueError(
                "Invalid value for `operation_status` ({0}), must be one of {1}"  # noqa: E501
                .format(operation_status, allowed_values)
            )

        self._operation_status = operation_status

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
        if issubclass(UnitControlSwitchesBody, dict):
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
        if not isinstance(other, UnitControlSwitchesBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
