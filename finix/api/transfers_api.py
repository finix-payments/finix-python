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
from finix.model.create_reversal_request import CreateReversalRequest
from finix.model.create_transfer_request import CreateTransferRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error402_payment_required import Error402PaymentRequired
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error422_invalid_field_list import Error422InvalidFieldList
from finix.model.error_generic import ErrorGeneric
from finix.model.transfer import Transfer
from finix.model.transfers_list import TransfersList
from finix.model.update_transfer_request import UpdateTransferRequest

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

class TransfersApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Transfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_transfer_request',
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
                    'create_transfer_request':
                        (CreateTransferRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_transfer_request': 'body',
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
        self._create_transfer_reversal_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Transfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers/{transfer_id}/reversals',
                'operation_id': 'create_transfer_reversal',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_id',
                    'create_reversal_request',
                ],
                'required': [
                    'transfer_id',
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
                    'transfer_id':
                        (str,),
                    'create_reversal_request':
                        (CreateReversalRequest,),
                },
                'attribute_map': {
                    'transfer_id': 'transfer_id',
                },
                'location_map': {
                    'transfer_id': 'path',
                    'create_reversal_request': 'body',
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
                'response_type': (Transfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers/{transfer_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_id',
                ],
                'required': [
                    'transfer_id',
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
                    'transfer_id':
                        (str,),
                },
                'attribute_map': {
                    'transfer_id': 'transfer_id',
                },
                'location_map': {
                    'transfer_id': 'path',
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
        self._list_transfers_reversals_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (TransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers/{transfer_id}/reversals',
                'operation_id': 'list_transfers_reversals',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_id',
                    'limit',
                    'after_cursor',
                    'before_cursor',
                ],
                'required': [
                    'transfer_id',
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
                    'transfer_id':
                        (str,),
                    'limit':
                        (int,),
                    'after_cursor':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'transfer_id': 'transfer_id',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'transfer_id': 'path',
                    'limit': 'query',
                    'after_cursor': 'query',
                    'before_cursor': 'query',
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
                'response_type': (TransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sort',
                    'after_cursor',
                    'limit',
                    'amount',
                    'amount_gte',
                    'amount_gt',
                    'amount_lte',
                    'amount_lt',
                    'created_at_gte',
                    'created_at_lte',
                    'idempotency_id',
                    'id',
                    'state',
                    'ready_to_settle_at_gte',
                    'ready_to_settle_at_lte',
                    'statement_descriptor',
                    'trace_id',
                    'updated_at_gte',
                    'updated_at_lte',
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
                    'before_cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'state',
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('state',): {

                        "ALL": "ALL",
                        "SUCCEEDED": "SUCCEEDED",
                        "FAILED": "FAILED",
                        "PENDING": "PENDING",
                        "CANCELED": "CANCELED"
                    },
                    ('type',): {

                        "ALL": "ALL",
                        "DEBITS": "DEBITS",
                        "CREDITS": "CREDITS",
                        "REVERSAL": "REVERSAL",
                        "SETTLEMENT": "SETTLEMENT"
                    },
                },
                'openapi_types': {
                    'sort':
                        (str,),
                    'after_cursor':
                        (str,),
                    'limit':
                        (int,),
                    'amount':
                        (int,),
                    'amount_gte':
                        (int,),
                    'amount_gt':
                        (int,),
                    'amount_lte':
                        (int,),
                    'amount_lt':
                        (int,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'idempotency_id':
                        (str,),
                    'id':
                        (str,),
                    'state':
                        (str,),
                    'ready_to_settle_at_gte':
                        (str,),
                    'ready_to_settle_at_lte':
                        (str,),
                    'statement_descriptor':
                        (int,),
                    'trace_id':
                        (str,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
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
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'sort': 'sort',
                    'after_cursor': 'after_cursor',
                    'limit': 'limit',
                    'amount': 'amount',
                    'amount_gte': 'amount.gte',
                    'amount_gt': 'amount.gt',
                    'amount_lte': 'amount.lte',
                    'amount_lt': 'amount.lt',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'idempotency_id': 'idempotency_id',
                    'id': 'id',
                    'state': 'state',
                    'ready_to_settle_at_gte': 'ready_to_settle_at.gte',
                    'ready_to_settle_at_lte': 'ready_to_settle_at.lte',
                    'statement_descriptor': 'statement_descriptor',
                    'trace_id': 'trace_id',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
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
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'sort': 'query',
                    'after_cursor': 'query',
                    'limit': 'query',
                    'amount': 'query',
                    'amount_gte': 'query',
                    'amount_gt': 'query',
                    'amount_lte': 'query',
                    'amount_lt': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'idempotency_id': 'query',
                    'id': 'query',
                    'state': 'query',
                    'ready_to_settle_at_gte': 'query',
                    'ready_to_settle_at_lte': 'query',
                    'statement_descriptor': 'query',
                    'trace_id': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
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
                    'before_cursor': 'query',
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
        self._update_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Transfer,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/transfers/{transfer_id}',
                'operation_id': 'update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'transfer_id',
                    'update_transfer_request',
                ],
                'required': [
                    'transfer_id',
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
                    'transfer_id':
                        (str,),
                    'update_transfer_request':
                        (UpdateTransferRequest,),
                },
                'attribute_map': {
                    'transfer_id': 'transfer_id',
                },
                'location_map': {
                    'transfer_id': 'path',
                    'update_transfer_request': 'body',
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

    def create(
        self,
        **kwargs
    ):
        """Create a Transfer  # noqa: E501

        Create a `Transfer`.   > By default, Finix implements a 3 (business) day delay when debiting bank accounts (i.e. eChecks).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_transfer_request (CreateTransferRequest): [optional]
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
            Transfer
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

    def create_transfer_reversal(
        self,
        transfer_id,
        **kwargs
    ):
        """Refund or Reverse a Transfer  # noqa: E501

        Reverse a transfer with a `type` of **DEBIT**. This reversal creates a new `Transfer` resource with a `type` of **REVERSAL**.   The refund can get delivered in most cases without the physical card. The card only needs to be swiped (to receive the refund) when:  - The payment type is **DEBIT**, and the transaction is no longer in the batch. - The payment type is **CREDIT**, and the transaction is no longer in the batch and is older than 45 days.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_transfer_reversal(transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_id (str): ID of `transfer` object

        Keyword Args:
            create_reversal_request (CreateReversalRequest): [optional]
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
            Transfer
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
        kwargs['transfer_id'] = \
            transfer_id
        return self._create_transfer_reversal_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        transfer_id,
        **kwargs
    ):
        """Get a Transfer  # noqa: E501

        Retrieve a `transfer`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_id (str): ID of `transfer` object.

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
            Transfer
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
        kwargs['transfer_id'] = \
            transfer_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list_transfers_reversals(
        self,
        transfer_id,
        **kwargs
    ):
        """List Reversals on a Transfer  # noqa: E501

        Retrieve a list of reversals for a `Transfer`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_transfers_reversals(transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_id (str): ID of `transfer` object

        Keyword Args:
            limit (int): The number of entries to return.. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            before_cursor (str): Return every resource created before the cursor value.. [optional]
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
        kwargs['transfer_id'] = \
            transfer_id
        return self._list_transfers_reversals_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Transfers  # noqa: E501

        Retrieve a list of `Transfers`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sort (str): Specify key to be used for sorting the collection. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            limit (int): The numbers of items to return. [optional]
            amount (int): Filter by an amount equal to the given value. [optional]
            amount_gte (int): Filter by an amount greater than or equal. [optional]
            amount_gt (int): Filter by an amount greater than. [optional]
            amount_lte (int): Filter by an amount less than or equal. [optional]
            amount_lt (int): Filter by an amount less than. [optional]
            created_at_gte (str): Filter where created_at is after the given date.. [optional]
            created_at_lte (str): Filter where created_at is before the given date.. [optional]
            idempotency_id (str): Filter by idempotency_id. [optional]
            id (str): Filter by id. [optional]
            state (str): Filter by Transaction state.. [optional]
            ready_to_settle_at_gte (str): Filter by ready_to_settle_at. [optional]
            ready_to_settle_at_lte (str): Filter by ready_to_settle_at. [optional]
            statement_descriptor (int): Filter by statement_descriptor. [optional]
            trace_id (str): Filter by trace_id. [optional]
            updated_at_gte (str): Filter where updated_at is after the given date. [optional]
            updated_at_lte (str): Filter where updated_at is before the given date. [optional]
            instrument_bin (str): Filter by Bank Identification Number (BIN). The BIN is the first 6 digits of the masked number. [optional]
            instrument_account_last4 (str): Filter Transactions by the last 4 digits of the bank account. The bank account last 4 are the last 4 digits of the masked number instrument_account_last4=9444 BIN . [optional]
            instrument_brand_type (str): Filter by card brand. Available card brand types can be found in the drop-down. [optional]
            merchant_identity_id (str): Filter by Identity ID. [optional]
            merchant_identity_name (str): Filter Transactions by Identity name. The name is not case-sensitive. [optional]
            instrument_name (str): Filter Transactions by payment instrument name. [optional]
            instrument_type (str): Filter Transactions by payment instrument type. Available instrument types include: Bank Account or Payment Card. [optional]
            merchant_id (str): Filter by Merchant ID. [optional]
            merchant_mid (str): Filter by Merchant Identification Number (MID). [optional]
            instrument_card_last4 (str): Filter by the payment card last 4 digits. [optional]
            merchant_processor_id (str): Filter by Processor ID. [optional]
            type (str): Filter by Transfer type. Available type filters include: All, Debits, Refunds, or Credits.. [optional]
            before_cursor (str): Return every resource created before the cursor value.. [optional]
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
        return self._list_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        transfer_id,
        **kwargs
    ):
        """Update a Transfer  # noqa: E501

        Update a `Transfer`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(transfer_id, async_req=True)
        >>> result = thread.get()

        Args:
            transfer_id (str): ID of `transfer` object.

        Keyword Args:
            update_transfer_request (UpdateTransferRequest): [optional]
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
            Transfer
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
        kwargs['transfer_id'] = \
            transfer_id
        return self._update_endpoint.call_with_http_info(**kwargs)

