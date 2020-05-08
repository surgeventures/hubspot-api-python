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


class IntegratorCardPayloadResponse(object):
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
        "total_count": "int",
        "all_items_link_url": "str",
        "card_label": "str",
        "top_level_actions": "TopLevelActions",
        "sections": "list[IntegratorObjectResult]",
        "response_version": "str",
    }

    attribute_map = {
        "total_count": "totalCount",
        "all_items_link_url": "allItemsLinkUrl",
        "card_label": "cardLabel",
        "top_level_actions": "topLevelActions",
        "sections": "sections",
        "response_version": "responseVersion",
    }

    def __init__(
        self,
        total_count=None,
        all_items_link_url=None,
        card_label=None,
        top_level_actions=None,
        sections=None,
        response_version=None,
        local_vars_configuration=None,
    ):  # noqa: E501
        """IntegratorCardPayloadResponse - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._total_count = None
        self._all_items_link_url = None
        self._card_label = None
        self._top_level_actions = None
        self._sections = None
        self._response_version = None
        self.discriminator = None

        self.total_count = total_count
        if all_items_link_url is not None:
            self.all_items_link_url = all_items_link_url
        if card_label is not None:
            self.card_label = card_label
        if top_level_actions is not None:
            self.top_level_actions = top_level_actions
        if sections is not None:
            self.sections = sections
        if response_version is not None:
            self.response_version = response_version

    @property
    def total_count(self):
        """Gets the total_count of this IntegratorCardPayloadResponse.  # noqa: E501

        The total number of card properties that will be sent in this response.  # noqa: E501

        :return: The total_count of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this IntegratorCardPayloadResponse.

        The total number of card properties that will be sent in this response.  # noqa: E501

        :param total_count: The total_count of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: int
        """
        if (
            self.local_vars_configuration.client_side_validation and total_count is None
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `total_count`, must not be `None`"
            )  # noqa: E501

        self._total_count = total_count

    @property
    def all_items_link_url(self):
        """Gets the all_items_link_url of this IntegratorCardPayloadResponse.  # noqa: E501

        URL to a page the integrator has built that displays all details for this card. This URL will be displayed to users under a `See more [x]` link if there are more than five items in your response, where `[x]` is the value of `itemLabel`.  # noqa: E501

        :return: The all_items_link_url of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: str
        """
        return self._all_items_link_url

    @all_items_link_url.setter
    def all_items_link_url(self, all_items_link_url):
        """Sets the all_items_link_url of this IntegratorCardPayloadResponse.

        URL to a page the integrator has built that displays all details for this card. This URL will be displayed to users under a `See more [x]` link if there are more than five items in your response, where `[x]` is the value of `itemLabel`.  # noqa: E501

        :param all_items_link_url: The all_items_link_url of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: str
        """

        self._all_items_link_url = all_items_link_url

    @property
    def card_label(self):
        """Gets the card_label of this IntegratorCardPayloadResponse.  # noqa: E501

        The label to be used for the `allItemsLinkUrl` link (e.g. 'See more tickets'). If not provided, this falls back to the card's title.  # noqa: E501

        :return: The card_label of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: str
        """
        return self._card_label

    @card_label.setter
    def card_label(self, card_label):
        """Sets the card_label of this IntegratorCardPayloadResponse.

        The label to be used for the `allItemsLinkUrl` link (e.g. 'See more tickets'). If not provided, this falls back to the card's title.  # noqa: E501

        :param card_label: The card_label of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: str
        """

        self._card_label = card_label

    @property
    def top_level_actions(self):
        """Gets the top_level_actions of this IntegratorCardPayloadResponse.  # noqa: E501


        :return: The top_level_actions of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: TopLevelActions
        """
        return self._top_level_actions

    @top_level_actions.setter
    def top_level_actions(self, top_level_actions):
        """Sets the top_level_actions of this IntegratorCardPayloadResponse.


        :param top_level_actions: The top_level_actions of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: TopLevelActions
        """

        self._top_level_actions = top_level_actions

    @property
    def sections(self):
        """Gets the sections of this IntegratorCardPayloadResponse.  # noqa: E501

        A list of up to five valid card sub categories.  # noqa: E501

        :return: The sections of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: list[IntegratorObjectResult]
        """
        return self._sections

    @sections.setter
    def sections(self, sections):
        """Sets the sections of this IntegratorCardPayloadResponse.

        A list of up to five valid card sub categories.  # noqa: E501

        :param sections: The sections of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: list[IntegratorObjectResult]
        """

        self._sections = sections

    @property
    def response_version(self):
        """Gets the response_version of this IntegratorCardPayloadResponse.  # noqa: E501


        :return: The response_version of this IntegratorCardPayloadResponse.  # noqa: E501
        :rtype: str
        """
        return self._response_version

    @response_version.setter
    def response_version(self, response_version):
        """Sets the response_version of this IntegratorCardPayloadResponse.


        :param response_version: The response_version of this IntegratorCardPayloadResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["v1", "v3"]  # noqa: E501
        if (
            self.local_vars_configuration.client_side_validation
            and response_version not in allowed_values
        ):  # noqa: E501
            raise ValueError(
                "Invalid value for `response_version` ({0}), must be one of {1}".format(  # noqa: E501
                    response_version, allowed_values
                )
            )

        self._response_version = response_version

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (item[0], item[1].to_dict())
                        if hasattr(item[1], "to_dict")
                        else item,
                        value.items(),
                    )
                )
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
        if not isinstance(other, IntegratorCardPayloadResponse):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, IntegratorCardPayloadResponse):
            return True

        return self.to_dict() != other.to_dict()