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
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.split_transfer import SplitTransfer
from finix.model.split_transfers_list import SplitTransfersList
from finix.model.transfers_list import TransfersList
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

class SplitTransfersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._get_split_transfer_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SplitTransfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/split_transfers/{split_transfer_id}',
                'operation_id': 'get_split_transfer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'split_transfer_id',
                ],
                'required': [
                    'split_transfer_id',
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
                    'split_transfer_id':
                        (str,),
                },
                'attribute_map': {
                    'split_transfer_id': 'split_transfer_id',
                },
                'location_map': {
                    'split_transfer_id': 'path',
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
        self._get_split_transfer_fees_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (TransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/split_transfers/{split_transfer_id}/fees',
                'operation_id': 'get_split_transfer_fees',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'split_transfer_id',
                ],
                'required': [
                    'split_transfer_id',
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
                    'split_transfer_id':
                        (str,),
                },
                'attribute_map': {
                    'split_transfer_id': 'split_transfer_id',
                },
                'location_map': {
                    'split_transfer_id': 'path',
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
        self._list_split_transfer_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SplitTransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/split_transfers',
                'operation_id': 'list_split_transfer',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'parent_transfer_id',
                ],
                'required': [
                    'parent_transfer_id',
                ],
                'nullable': [
                ],
                'enum': [
                ],
                'validation': [
                    'parent_transfer_id',
                ]
            },
            root_map={
                'validations': {
                    ('parent_transfer_id',): {

                        'regex': {
                            'pattern': r'TRxxxxxxxxxxxxxxxxxxxxxx',  # noqa: E501
                        },
                    },
                },
                'allowed_values': {
                },
                'openapi_types': {
                    'parent_transfer_id':
                        (str,),
                },
                'attribute_map': {
                    'parent_transfer_id': 'parent_transfer_id',
                },
                'location_map': {
                    'parent_transfer_id': 'query',
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

    def get_split_transfer(
        self,
        split_transfer_id,
        **kwargs
    ):
        """Fetch a Split Transfer  # noqa: E501

        Fetch a `split_transfer` that was created from a split transaction.  For more information, see [Split a Transaction](/docs/guides/payments/modify/split-transactions/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_split_transfer(split_transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            split_transfer_id (str):

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
            SplitTransfer
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
        kwargs['split_transfer_id'] = \
            split_transfer_id
        return self._get_split_transfer_endpoint.call_with_http_info(**kwargs)

    def get_split_transfer_fees(
        self,
        split_transfer_id,
        **kwargs
    ):
        """Fetch Split Transfer Fees  # noqa: E501

        Fetch the fees associated with a `split_transfer`.   For more information, see [Split a Transaction](/docs/guides/payments/modify/split-transactions/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_split_transfer_fees(split_transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            split_transfer_id (str):

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
            TransfersList
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
        kwargs['split_transfer_id'] = \
            split_transfer_id
        return self._get_split_transfer_fees_endpoint.call_with_http_info(**kwargs)

    def list_split_transfer(
        self,
        parent_transfer_id,
        **kwargs
    ):
        """List Split Transfers  # noqa: E501

        Retireve a list of `split_transfers` created for a specifc split `Transfer`.  For more information, see [Split a Transaction](/docs/guides/payments/modify/split-transactions/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_split_transfer(parent_transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            parent_transfer_id (str): **ID** of the parent `Transfer` that was split.

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
            SplitTransfersList
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
        kwargs['parent_transfer_id'] = \
            parent_transfer_id
        ret = self._list_split_transfer_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_split_transfer,  **kwargs)
        return fl

