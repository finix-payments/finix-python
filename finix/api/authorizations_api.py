"""
    Finix API

    The version of the OpenAPI document: 2022-02-01
    Contact: support@finixpayments.com
"""


import re  # noqa: F401
import sys  # noqa: F401

import finix.api_client
from finix.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types
)
from finix.model.authorization import Authorization
from finix.model.authorization_captured import AuthorizationCaptured
from finix.model.authorizations_list import AuthorizationsList
from finix.model.create_authorization_request import CreateAuthorizationRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error422_invalid_field_list import Error422InvalidFieldList
from finix.model.error_generic import ErrorGeneric
from finix.model.update_authorization_request import UpdateAuthorizationRequest
from finix.model.void_authorization import VoidAuthorization
from finix.model.finix_utils import FinixList

from functools import wraps

def operation_decorator(func):
    @wraps(func)
    def response_convert(*args, **kwargs):
        ret = func(*args, **kwargs)
        if hasattr(ret, 'embedded'):
            tmp = ret.embedded
            if isinstance(tmp, dict):
                if len(tmp) == 1:
                    ret_0 = ''
                    ret_1 = ''
                    ret_2 = ''
                    for key in tmp:
                        ret_0 = tmp[key]
                        break
                    if hasattr(ret, 'page'):
                        ret_1 = ret.page
                    if hasattr(ret, 'links'):
                        ret_2 = ret.links
                    return (ret_0, ret_1, ret_2)

        else:
            return ret
    
    return response_convert

class AuthorizationsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._update_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (AuthorizationCaptured,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/authorizations/{authorization_id}',
                'operation_id': 'update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorization_id',
                    'finix_version',
                    'update_authorization_request',
                ],
                'required': [
                    'authorization_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'authorization_id':
                        (str,),
                    'finix_version':
                        (str,),
                    'update_authorization_request':
                        (UpdateAuthorizationRequest,),
                },
                'attribute_map': {
                    'authorization_id': 'authorization_id',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'authorization_id': 'path',
                    'finix_version': 'header',
                    'update_authorization_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Authorization,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/authorizations',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'finix_version',
                    'create_authorization_request',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'finix_version':
                        (str,),
                    'create_authorization_request':
                        (CreateAuthorizationRequest,),
                },
                'attribute_map': {
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'finix_version': 'header',
                    'create_authorization_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Authorization,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/authorizations/{authorization_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorization_id',
                ],
                'required': [
                    'authorization_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'authorization_id':
                        (str,),
                },
                'attribute_map': {
                    'authorization_id': 'authorization_id',
                },
                'location_map': {
                    'authorization_id': 'path',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self._list_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (AuthorizationsList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/authorizations',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'amount',
                    'amount_gt',
                    'amount_gte',
                    'amount_lt',
                    'amount_lte',
                    'before_cursor',
                    'after_cursor',
                    'created_at_gte',
                    'created_at_lte',
                    'idempotency_id',
                    'limit',
                    'tags_key',
                    'tags_value',
                    'state',
                    'updated_at_gte',
                    'updated_at_lte',
                    'trace_id',
                    'is_void',
                    'instrument_bin',
                    'instrument_account_last4',
                    'instrument_brand_type',
                    'merchant_identity_id',
                    'merchant_identity_name',
                    'instrument_name',
                    'instrument_type',
                    'merchant_id',
                    'merchant_mid',
                    'instrument_card_last4',
                    'merchant_processor_id',
                    'type',
                    'finix_version',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'state',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('state',): {

                        "SUCCEEDED": "SUCCEEDED",
                        "FAILED": "FAILED",
                        "PENDING": "PENDING",
                        "CANCELED": "CANCELED"
                    },
                },
                'openapi_types': {
                    'amount':
                        (int,),
                    'amount_gt':
                        (int,),
                    'amount_gte':
                        (int,),
                    'amount_lt':
                        (int,),
                    'amount_lte':
                        (int,),
                    'before_cursor':
                        (str,),
                    'after_cursor':
                        (str,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'idempotency_id':
                        (str,),
                    'limit':
                        (int,),
                    'tags_key':
                        (str,),
                    'tags_value':
                        (str,),
                    'state':
                        (str,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                    'trace_id':
                        (str,),
                    'is_void':
                        (str,),
                    'instrument_bin':
                        (str,),
                    'instrument_account_last4':
                        (str,),
                    'instrument_brand_type':
                        (str,),
                    'merchant_identity_id':
                        (str,),
                    'merchant_identity_name':
                        (str,),
                    'instrument_name':
                        (str,),
                    'instrument_type':
                        (str,),
                    'merchant_id':
                        (str,),
                    'merchant_mid':
                        (str,),
                    'instrument_card_last4':
                        (str,),
                    'merchant_processor_id':
                        (str,),
                    'type':
                        (str,),
                    'finix_version':
                        (str,),
                },
                'attribute_map': {
                    'amount': 'amount',
                    'amount_gt': 'amount.gt',
                    'amount_gte': 'amount.gte',
                    'amount_lt': 'amount.lt',
                    'amount_lte': 'amount.lte',
                    'before_cursor': 'before_cursor',
                    'after_cursor': 'after_cursor',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'idempotency_id': 'idempotency_id',
                    'limit': 'limit',
                    'tags_key': 'tags.key',
                    'tags_value': 'tags.value',
                    'state': 'state',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                    'trace_id': 'trace_id',
                    'is_void': 'is_void',
                    'instrument_bin': 'instrument_bin',
                    'instrument_account_last4': 'instrument_account_last4',
                    'instrument_brand_type': 'instrument_brand_type',
                    'merchant_identity_id': 'merchant_identity_id',
                    'merchant_identity_name': 'merchant_identity_name',
                    'instrument_name': 'instrument_name',
                    'instrument_type': 'instrument_type',
                    'merchant_id': 'merchant_id',
                    'merchant_mid': 'merchant_mid',
                    'instrument_card_last4': 'instrument_card_last4',
                    'merchant_processor_id': 'merchant_processor_id',
                    'type': 'type',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'amount': 'query',
                    'amount_gt': 'query',
                    'amount_gte': 'query',
                    'amount_lt': 'query',
                    'amount_lte': 'query',
                    'before_cursor': 'query',
                    'after_cursor': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'idempotency_id': 'query',
                    'limit': 'query',
                    'tags_key': 'query',
                    'tags_value': 'query',
                    'state': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'trace_id': 'query',
                    'is_void': 'query',
                    'instrument_bin': 'query',
                    'instrument_account_last4': 'query',
                    'instrument_brand_type': 'query',
                    'merchant_identity_id': 'query',
                    'merchant_identity_name': 'query',
                    'instrument_name': 'query',
                    'instrument_type': 'query',
                    'merchant_id': 'query',
                    'merchant_mid': 'query',
                    'instrument_card_last4': 'query',
                    'merchant_processor_id': 'query',
                    'type': 'query',
                    'finix_version': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self._update_authorization_void_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (AuthorizationCaptured,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/authorizations/{authorization_id_void_to}',
                'operation_id': 'update_authorization_void',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'authorization_id_void_to',
                    'finix_version',
                    'void_authorization',
                ],
                'required': [
                    'authorization_id_void_to',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'authorization_id_void_to':
                        (str,),
                    'finix_version':
                        (str,),
                    'void_authorization':
                        (VoidAuthorization,),
                },
                'attribute_map': {
                    'authorization_id_void_to': 'authorization_id_void_to',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'authorization_id_void_to': 'path',
                    'finix_version': 'header',
                    'void_authorization': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )

    def update(
        self,
        authorization_id,
        **kwargs
    ):
        """Capture an Authorization  # noqa: E501

        Use a PUT request to capture an `Authorization`. If captured successfully, the `transfer` field of the `Authorization` will contain the ID of the `Transfer` resource that moves funds.  Related Guides: [Creating and Capturing an Authorization](/guides/payments/making-a-payment/creating-and-capturing-an-authorization/), [Level 2 and 3 Processing](/guides/payments/making-a-payment/level-2-and-level-3-processing/), [In-Person Cloud Payments](/guides/payments/in-person-payments/cloud/in-person-cloud-payments/), [Buyer Charges](/guides/payments/making-a-payment/buyer-charges/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(authorization_id, async_req=True)
        >>> result = thread.get()

        Args:
            authorization_id (str): ID of `Authorization` to fetch.

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            update_authorization_request (UpdateAuthorizationRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthorizationCaptured
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', False
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['authorization_id'] = \
            authorization_id
        return self._update_endpoint.call_with_http_info(**kwargs)

    def create(
        self,
        **kwargs
    ):
        """Create an Authorization  # noqa: E501

        Create an `Authorization` to process a transaction.  Related Guides: [Creating and Capturing an Authorization](/guides/payments/making-a-payment/creating-and-capturing-an-authorization/), [Level 2 and 3 Processing](/guides/payments/making-a-payment/level-2-and-level-3-processing/), [In-Person Cloud Payments](/guides/payments/in-person-payments/cloud/in-person-cloud-payments/), [Buyer Charges](/guides/payments/making-a-payment/buyer-charges/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            create_authorization_request (CreateAuthorizationRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Authorization
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', False
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        return self._create_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        authorization_id,
        **kwargs
    ):
        """Fetch an Authorization  # noqa: E501

        Retrieve the details of a previously created `Authorization`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(authorization_id, async_req=True)
        >>> result = thread.get()

        Args:
            authorization_id (str): ID of `Authorization` to fetch.

        Keyword Args:
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            Authorization
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', False
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['authorization_id'] = \
            authorization_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Authorizations  # noqa: E501

        Retrieve a list of `Authorizations`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            amount (int): Filter by an amount equal to the given value.. [optional]
            amount_gt (int): Filter by an amount greater than.. [optional]
            amount_gte (int): Filter by an amount greater than or equal.. [optional]
            amount_lt (int): Filter by an amount less than.. [optional]
            amount_lte (int): Filter by an amount less than or equal.. [optional]
            before_cursor (str): Return every resource created before the cursor value.. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            idempotency_id (str): Filter by `idempotency_id`.. [optional]
            limit (int): The numbers of items to return.. [optional]
            tags_key (str): Filter by the [`key` of a `Tag`](/api/overview/#section/Tags).. [optional]
            tags_value (str): Filter by the [value of a `Tag`](https://finix.com/docs/api/overview/#section/Tags).. [optional]
            state (str): Filter by Transaction state.. [optional]
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]
            trace_id (str): Filter by `trace_id`.. [optional]
            is_void (str): Filter by `idempotency_id`.. [optional]
            instrument_bin (str): Filter by Bank Identification Number (BIN). The BIN is the first 6 digits of the masked number.. [optional]
            instrument_account_last4 (str): Filter Transactions by the last 4 digits of the bank account. The bank account last 4 are the last 4 digits of the masked number instrument_account_last4=9444 BIN.. [optional]
            instrument_brand_type (str): Filter by card brand. Available card brand types can be found in the drop-down.. [optional]
            merchant_identity_id (str): Filter by `Identity` ID.. [optional]
            merchant_identity_name (str): Filter Transactions by `Identity` name. The name is not case-sensitive.. [optional]
            instrument_name (str): Filter Transactions by `Payment Instrument` name.. [optional]
            instrument_type (str): Filter Transactions by `Payment Instrument` type. Available instrument types include: Bank Account or Payment Card.. [optional]
            merchant_id (str): Filter by `Merchant` ID.. [optional]
            merchant_mid (str): Filter by Merchant Identification Number (MID).. [optional]
            instrument_card_last4 (str): Filter by the payment card last 4 digits.. [optional]
            merchant_processor_id (str): Filter by `Processor` ID.. [optional]
            type (str): Type of the `Authorization`.. [optional]
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthorizationsList
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', False
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        ret = self._list_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list,  **kwargs)
        return fl

    def update_authorization_void(
        self,
        authorization_id_void_to,
        **kwargs
    ):
        """Void an Authorization  # noqa: E501

        Use a PUT request to void an `Authorization`. If voided successfully, funds get released and the transaction stops from completing. Additionally, voided `Authorization` can no longer be captured.  Related Guides: [Creating and Capturing an Authorization](/guides/payments/making-a-payment/creating-and-capturing-an-authorization/), [Level 2 and 3 Processing](/guides/payments/making-a-payment/level-2-and-level-3-processing/), [In-Person Cloud Payments](/guides/payments/in-person-payments/cloud/in-person-cloud-payments/), [Buyer Charges](/guides/payments/making-a-payment/buyer-charges/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_authorization_void(authorization_id_void_to, async_req=True)
        >>> result = thread.get()

        Args:
            authorization_id_void_to (str):

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            void_authorization (VoidAuthorization): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            AuthorizationCaptured
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs['async_req'] = kwargs.get(
            'async_req', False
        )
        kwargs['_return_http_data_only'] = kwargs.get(
            '_return_http_data_only', True
        )
        kwargs['_preload_content'] = kwargs.get(
            '_preload_content', True
        )
        kwargs['_request_timeout'] = kwargs.get(
            '_request_timeout', None
        )
        kwargs['_check_input_type'] = kwargs.get(
            '_check_input_type', False
        )
        kwargs['_check_return_type'] = kwargs.get(
            '_check_return_type', False
        )
        kwargs['_spec_property_naming'] = kwargs.get(
            '_spec_property_naming', False
        )
        kwargs['_content_type'] = kwargs.get(
            '_content_type')
        kwargs['_host_index'] = kwargs.get('_host_index')
        kwargs['authorization_id_void_to'] = \
            authorization_id_void_to
        return self._update_authorization_void_endpoint.call_with_http_info(**kwargs)

