# coding: utf-8

# flake8: noqa

"""
    HubSpot Events API

    API for accessing CRM object events.  # noqa: E501

    The version of the OpenAPI document: v3
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from hubspot.events.api.events_api import EventsApi

# import ApiClient
from hubspot.events.api_client import ApiClient
from hubspot.events.configuration import Configuration
from hubspot.events.exceptions import OpenApiException
from hubspot.events.exceptions import ApiTypeError
from hubspot.events.exceptions import ApiValueError
from hubspot.events.exceptions import ApiKeyError
from hubspot.events.exceptions import ApiException
# import models into sdk package
from hubspot.events.models.collection_response_external_unified_event import CollectionResponseExternalUnifiedEvent
from hubspot.events.models.error import Error
from hubspot.events.models.error_detail import ErrorDetail
from hubspot.events.models.external_unified_event import ExternalUnifiedEvent
from hubspot.events.models.next_page import NextPage
from hubspot.events.models.paging import Paging

