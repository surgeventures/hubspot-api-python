# coding: utf-8

"""
    Accounting Extension

    These APIs allow you to interact with HubSpot's Accounting Extension. It allows you to: * Specify the URLs that HubSpot will use when making webhook requests to your external accounting system. * Respond to webhook calls made to your external accounting system by HubSpot   # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from hubspot.crm.extensions.accounting.configuration import Configuration


class AccountingExtensionCustomer(object):
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
        'email_address': 'str',
        'name': 'str',
        'id': 'str',
        'billing_address': 'Address',
        'currency_code': 'str'
    }

    attribute_map = {
        'email_address': 'emailAddress',
        'name': 'name',
        'id': 'id',
        'billing_address': 'billingAddress',
        'currency_code': 'currencyCode'
    }

    def __init__(self, email_address=None, name=None, id=None, billing_address=None, currency_code=None, local_vars_configuration=None):  # noqa: E501
        """AccountingExtensionCustomer - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._email_address = None
        self._name = None
        self._id = None
        self._billing_address = None
        self._currency_code = None
        self.discriminator = None

        if email_address is not None:
            self.email_address = email_address
        self.name = name
        self.id = id
        if billing_address is not None:
            self.billing_address = billing_address
        if currency_code is not None:
            self.currency_code = currency_code

    @property
    def email_address(self):
        """Gets the email_address of this AccountingExtensionCustomer.  # noqa: E501

        The customer's email address  # noqa: E501

        :return: The email_address of this AccountingExtensionCustomer.  # noqa: E501
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AccountingExtensionCustomer.

        The customer's email address  # noqa: E501

        :param email_address: The email_address of this AccountingExtensionCustomer.  # noqa: E501
        :type: str
        """

        self._email_address = email_address

    @property
    def name(self):
        """Gets the name of this AccountingExtensionCustomer.  # noqa: E501

        The customer's full name  # noqa: E501

        :return: The name of this AccountingExtensionCustomer.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AccountingExtensionCustomer.

        The customer's full name  # noqa: E501

        :param name: The name of this AccountingExtensionCustomer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and name is None:  # noqa: E501
            raise ValueError("Invalid value for `name`, must not be `None`")  # noqa: E501

        self._name = name

    @property
    def id(self):
        """Gets the id of this AccountingExtensionCustomer.  # noqa: E501

        The ID of the customer in the external accounting system.  # noqa: E501

        :return: The id of this AccountingExtensionCustomer.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AccountingExtensionCustomer.

        The ID of the customer in the external accounting system.  # noqa: E501

        :param id: The id of this AccountingExtensionCustomer.  # noqa: E501
        :type: str
        """
        if self.local_vars_configuration.client_side_validation and id is None:  # noqa: E501
            raise ValueError("Invalid value for `id`, must not be `None`")  # noqa: E501

        self._id = id

    @property
    def billing_address(self):
        """Gets the billing_address of this AccountingExtensionCustomer.  # noqa: E501


        :return: The billing_address of this AccountingExtensionCustomer.  # noqa: E501
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this AccountingExtensionCustomer.


        :param billing_address: The billing_address of this AccountingExtensionCustomer.  # noqa: E501
        :type: Address
        """

        self._billing_address = billing_address

    @property
    def currency_code(self):
        """Gets the currency_code of this AccountingExtensionCustomer.  # noqa: E501

        The ISO 4217 currency code that represents the currency the customer should be billed in.  # noqa: E501

        :return: The currency_code of this AccountingExtensionCustomer.  # noqa: E501
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this AccountingExtensionCustomer.

        The ISO 4217 currency code that represents the currency the customer should be billed in.  # noqa: E501

        :param currency_code: The currency_code of this AccountingExtensionCustomer.  # noqa: E501
        :type: str
        """

        self._currency_code = currency_code

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
        if not isinstance(other, AccountingExtensionCustomer):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, AccountingExtensionCustomer):
            return True

        return self.to_dict() != other.to_dict()
