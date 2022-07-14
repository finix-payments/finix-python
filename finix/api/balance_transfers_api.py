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
from finix.model.balance_transfer import BalanceTransfer
from finix.model.balance_transfer_list import BalanceTransferList
from finix.model.create_balance_transfer_request import CreateBalanceTransferRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error_generic import ErrorGeneric

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

class BalanceTransfersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (BalanceTransfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/balance_transfers',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_balance_transfer_request',
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
                    'create_balance_transfer_request':
                        (CreateBalanceTransferRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_balance_transfer_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [
                    'application/hal+json'
                ]
            },
            api_client=api_client
        )
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (BalanceTransfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/balance_transfers/{balance_transfers_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'balance_transfers_id',
                ],
                'required': [
                    'balance_transfers_id',
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
                    'balance_transfers_id':
                        (str,),
                },
                'attribute_map': {
                    'balance_transfers_id': 'balance_transfers_id',
                },
                'location_map': {
                    'balance_transfers_id': 'path',
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
                'response_type': (BalanceTransferList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/balance_transfers',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'offset',
                    'page_number',
                    'page_size',
                    'created_at_gte',
                    'created_at_lte',
                    'updated_at_gte',
                    'updated_at_lte',
                    'idempotency_id',
                    'amount',
                    'description',
                    'destination',
                    'external_reference_id',
                    'reference_id',
                    'source',
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
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                    'page_number':
                        (int,),
                    'page_size':
                        (int,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                    'idempotency_id':
                        (str,),
                    'amount':
                        (int,),
                    'description':
                        (str,),
                    'destination':
                        (str,),
                    'external_reference_id':
                        (str,),
                    'reference_id':
                        (str,),
                    'source':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'offset': 'offset',
                    'page_number': 'pageNumber',
                    'page_size': 'pageSize',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                    'idempotency_id': 'idempotency_id',
                    'amount': 'amount',
                    'description': 'description',
                    'destination': 'destination',
                    'external_reference_id': 'external_reference_id',
                    'reference_id': 'reference_id',
                    'source': 'source',
                },
                'location_map': {
                    'limit': 'query',
                    'offset': 'query',
                    'page_number': 'query',
                    'page_size': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'idempotency_id': 'query',
                    'amount': 'query',
                    'description': 'query',
                    'destination': 'query',
                    'external_reference_id': 'query',
                    'reference_id': 'query',
                    'source': 'query',
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

    def create(
        self,
        **kwargs
    ):
        """Create a Balance Transfer  # noqa: E501

        Create a `balance_transfer`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_balance_transfer_request (CreateBalanceTransferRequest): [optional]
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
            BalanceTransfer
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
        balance_transfers_id,
        **kwargs
    ):
        """Get a Balance Transfer  # noqa: E501

        Retrieve the details of a `balance_transfer`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(balance_transfers_id, async_req=True)
        >>> result = thread.get()

        Args:
            balance_transfers_id (str): ID of the `balance_transfer` resource.

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
            BalanceTransfer
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
        kwargs['balance_transfers_id'] = \
            balance_transfers_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Balance Transfers  # noqa: E501

        Retrieve a list of `balance_transfers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): The numbers of items to return. [optional]
            offset (int): The number of items to skip before starting to collect the result set. [optional]
            page_number (int): The page number to list. [optional]
            page_size (int): The size of the page. [optional]
            created_at_gte (str): Filter where created_at is after the given date.. [optional]
            created_at_lte (str): Filter where created_at is before the given date.. [optional]
            updated_at_gte (str): Filter where updated_at is after the given date. [optional]
            updated_at_lte (str): Filter where updated_at is before the given date. [optional]
            idempotency_id (str): Filter by idempotency_id. [optional]
            amount (int): Filter by an amount equal to the given value. [optional]
            description (str): Filter by the `description` value . [optional]
            destination (str): Filter by the `Payment Instrument` saved in `destination`. [optional]
            external_reference_id (str): Filter by the value saved in `external_reference_id`. [optional]
            reference_id (str): Filter by the value saved in `reference_id`. [optional]
            source (str): Filter by the `Payment Instrument` saved in `source`. [optional]
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
            BalanceTransferList
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
        return self._list_endpoint.call_with_http_info(**kwargs)

