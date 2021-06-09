# coding: utf-8

"""
    CRM cards

    Allows an app to extend the CRM UI by surfacing custom cards in the sidebar of record pages. These cards are defined up-front as part of app configuration, then populated by external data fetch requests when the record page is accessed by a user.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.cards.configuration import Configuration


class IFrameActionBody(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'type': 'str',
        'width': 'int',
        'height': 'int',
        'url': 'str',
        'label': 'str',
        'property_names_included': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'width': 'width',
        'height': 'height',
        'url': 'url',
        'label': 'label',
        'property_names_included': 'propertyNamesIncluded'
    }

    def __init__(self, type='IFRAME', width=None, height=None, url=None, label=None, property_names_included=None, local_vars_configuration=None):  # noqa: E501
        """IFrameActionBody - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._type = None
        self._width = None
        self._height = None
        self._url = None
        self._label = None
        self._property_names_included = None
        self.discriminator = None

        self.type = type
        self.width = width
        self.height = height
        self.url = url
        if label is not None:
            self.label = label
        self.property_names_included = property_names_included

    @property
    def type(self):
        """Gets the type of this IFrameActionBody.  # noqa: E501


        :return: The type of this IFrameActionBody.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this IFrameActionBody.


        :param type: The type of this IFrameActionBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and type is None:  # noqa: E501
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        allowed_values = ["IFRAME"]  # noqa: E501
        if self.local_vars_configuration.client_side_validation and type not in allowed_values:  # noqa: E501
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def width(self):
        """Gets the width of this IFrameActionBody.  # noqa: E501


        :return: The width of this IFrameActionBody.  # noqa: E501
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this IFrameActionBody.


        :param width: The width of this IFrameActionBody.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and width is None:  # noqa: E501
            raise ValueError("Invalid value for `width`, must not be `None`")  # noqa: E501

        self._width = width

    @property
    def height(self):
        """Gets the height of this IFrameActionBody.  # noqa: E501


        :return: The height of this IFrameActionBody.  # noqa: E501
        :rtype: int
        """
        return self._height

    @height.setter
    def height(self, height):
        """Sets the height of this IFrameActionBody.


        :param height: The height of this IFrameActionBody.  # noqa: E501
        :type: int
        """
        if self.local_vars_configuration.client_side_validation and height is None:  # noqa: E501
            raise ValueError("Invalid value for `height`, must not be `None`")  # noqa: E501

        self._height = height

    @property
    def url(self):
        """Gets the url of this IFrameActionBody.  # noqa: E501


        :return: The url of this IFrameActionBody.  # noqa: E501
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this IFrameActionBody.


        :param url: The url of this IFrameActionBody.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and url is None:  # noqa: E501
            raise ValueError("Invalid value for `url`, must not be `None`")  # noqa: E501

        self._url = url

    @property
    def label(self):
        """Gets the label of this IFrameActionBody.  # noqa: E501


        :return: The label of this IFrameActionBody.  # noqa: E501
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this IFrameActionBody.


        :param label: The label of this IFrameActionBody.  # noqa: E501
        :type: str
        """

        self._label = label

    @property
    def property_names_included(self):
        """Gets the property_names_included of this IFrameActionBody.  # noqa: E501


        :return: The property_names_included of this IFrameActionBody.  # noqa: E501
        :rtype: list[str]
        """
        return self._property_names_included

    @property_names_included.setter
    def property_names_included(self, property_names_included):
        """Sets the property_names_included of this IFrameActionBody.


        :param property_names_included: The property_names_included of this IFrameActionBody.  # noqa: E501
        :type: list[str]
        """
        if self.local_vars_configuration.client_side_validation and property_names_included is None:  # noqa: E501
            raise ValueError("Invalid value for `property_names_included`, must not be `None`")  # noqa: E501

        self._property_names_included = property_names_included

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, IFrameActionBody):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IFrameActionBody):
            return True

        return self.to_dict() != other.to_dict()
