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
from finix.model.close_settlement import CloseSettlement
from finix.model.create_settlement_request import CreateSettlementRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error422_invalid_field_list import Error422InvalidFieldList
from finix.model.error_generic import ErrorGeneric
from finix.model.remove_settlement_transfer import RemoveSettlementTransfer
from finix.model.settlement import Settlement
from finix.model.settlements_list import SettlementsList
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

class SettlementsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._put_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Settlement,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements/{settlement_id}',
                'operation_id': 'put',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_id',
                    'finix_version',
                    'close_settlement',
                ],
                'required': [
                    'settlement_id',
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
                    'settlement_id':
                        (str,),
                    'finix_version':
                        (str,),
                    'close_settlement':
                        (CloseSettlement,),
                },
                'attribute_map': {
                    'settlement_id': 'settlement_id',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'settlement_id': 'path',
                    'finix_version': 'header',
                    'close_settlement': 'body',
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
                'response_type': (Settlement,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}/settlements',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'create_settlement_request',
                ],
                'required': [
                    'identity_id',
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
                    'identity_id':
                        (str,),
                    'create_settlement_request':
                        (CreateSettlementRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                },
                'location_map': {
                    'identity_id': 'path',
                    'create_settlement_request': 'body',
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
                'response_type': (Settlement,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements/{settlement_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_id',
                ],
                'required': [
                    'settlement_id',
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
                    'settlement_id':
                        (str,),
                },
                'attribute_map': {
                    'settlement_id': 'settlement_id',
                },
                'location_map': {
                    'settlement_id': 'path',
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
        self._list_funding_transfers_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (TransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements/{settlement_id}/funding_transfers',
                'operation_id': 'list_funding_transfers',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_id',
                    'limit',
                ],
                'required': [
                    'settlement_id',
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
                    'settlement_id':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'settlement_id': 'settlement_id',
                    'limit': 'limit',
                },
                'location_map': {
                    'settlement_id': 'path',
                    'limit': 'query',
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
        self._list_transfers_by_settlement_id_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (TransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements/{settlement_id}/transfers',
                'operation_id': 'list_transfers_by_settlement_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_id',
                    'limit',
                ],
                'required': [
                    'settlement_id',
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
                    'settlement_id':
                        (str,),
                    'limit':
                        (int,),
                },
                'attribute_map': {
                    'settlement_id': 'settlement_id',
                    'limit': 'limit',
                },
                'location_map': {
                    'settlement_id': 'path',
                    'limit': 'query',
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
                'response_type': (SettlementsList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'created_at_gte',
                    'created_at_lte',
                    'amount',
                    'amount_gt',
                    'amount_gte',
                    'amount_lt',
                    'amount_lte',
                    'status',
                    'transfer_id',
                    'funding_transfer_id',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'status',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('status',): {

                        "PENDING": "PENDING",
                        "AWAITING_APPROVAL": "AWAITING_APPROVAL",
                        "APPROVED": "APPROVED"
                    },
                },
                'openapi_types': {
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
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
                    'status':
                        (str,),
                    'transfer_id':
                        (str,),
                    'funding_transfer_id':
                        (str,),
                },
                'attribute_map': {
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'amount': 'amount',
                    'amount_gt': 'amount.gt',
                    'amount_gte': 'amount.gte',
                    'amount_lt': 'amount.lt',
                    'amount_lte': 'amount.lte',
                    'status': 'status',
                    'transfer_id': 'transfer_id',
                    'funding_transfer_id': 'funding_transfer_id',
                },
                'location_map': {
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'amount': 'query',
                    'amount_gt': 'query',
                    'amount_gte': 'query',
                    'amount_lt': 'query',
                    'amount_lte': 'query',
                    'status': 'query',
                    'transfer_id': 'query',
                    'funding_transfer_id': 'query',
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
        self._remove_transfers_from_settlement_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/settlements/{settlement_id}/transfers',
                'operation_id': 'remove_transfers_from_settlement',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'settlement_id',
                    'remove_settlement_transfer',
                ],
                'required': [
                    'settlement_id',
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
                    'settlement_id':
                        (str,),
                    'remove_settlement_transfer':
                        (RemoveSettlementTransfer,),
                },
                'attribute_map': {
                    'settlement_id': 'settlement_id',
                },
                'location_map': {
                    'settlement_id': 'path',
                    'remove_settlement_transfer': 'body',
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

    def put(
        self,
        settlement_id,
        **kwargs
    ):
        """Close a Settlement  # noqa: E501

        Close an accruing `settlement`.  Finix, by default, creates accruing `settlements` then closes them based on your payout configurations. Use this endpoint to manually close a specific `settlement`.  The closed `Settlement` will not accrue any further transactions and gets immediately submitted for approval. - This endpoint is only available to Finix Core customers. If you have any questions, please contact the [Finix Support Team](mailto:support@finixpayments.com). - Any refunded `Transfers` get included in `Settlements` as a deduction.  - **PENDING** `Transfers` don't get included in `Settlements`. - The `total_amount` minus the `total_fee` equals the `net_amount`. The `net_amount` is the amount in cents that gets deposited into the seller's bank account.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.put(settlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_id (str): ID of `Settlement` object.

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            close_settlement (CloseSettlement): [optional]
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
            Settlement
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
        kwargs['settlement_id'] = \
            settlement_id
        return self._put_endpoint.call_with_http_info(**kwargs)

    def create(
        self,
        identity_id,
        **kwargs
    ):
        """Close Current Active Settlement  # noqa: E501

        Close the currently accruing `settlement`.   Finix, by default, creates accruing `settlements` then closes them based on your payout configurations. Use this endpoint to manually close the currently accruing settlement.  The closed `Settlement` will not accrue any further transactions and gets immediately submitted for approval. - This endpoint is only available to Finix Core customers. If you have any questions, please contact the [Finix Support Team.](mailto:support@finixpayments.com) - Any refunded `Transfers` get included in `Settlements` as a deduction. - **PENDING** `Transfers` don't get included in `Settlements`.  - The `total_amount` minus the `total_fee` equals the `net_amount`. The `net_amount` is the amount in cents that gets deposited into the seller's bank account.  Related Guides: [Accruing Settlements](/guides/payouts/accruing-settlements/#closing-an-accruing-settlement)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of the `Identity` for the merchant you want to settle. 

        Keyword Args:
            create_settlement_request (CreateSettlementRequest): [optional]
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
            Settlement
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
        kwargs['identity_id'] = \
            identity_id
        return self._create_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        settlement_id,
        **kwargs
    ):
        """Fetch a Settlement  # noqa: E501

        Retreive the details of a `Settlement`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(settlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_id (str): ID of `Settlement` object.

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
            Settlement
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
        kwargs['settlement_id'] = \
            settlement_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list_funding_transfers(
        self,
        settlement_id,
        **kwargs
    ):
        """List Settlement Funding Transfers  # noqa: E501

        List the funding `Transfers` that were created when a `Settlement` was approved that have `type` **CREDIT** or **DEBIT**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_funding_transfers(settlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_id (str): ID of `Settlement` object.

        Keyword Args:
            limit (int): The numbers of items to return.. [optional]
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
        kwargs['settlement_id'] = \
            settlement_id
        ret = self._list_funding_transfers_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_funding_transfers,  **kwargs)
        return fl

    def list_transfers_by_settlement_id(
        self,
        settlement_id,
        **kwargs
    ):
        """List all Transfers in a Settlement  # noqa: E501

        Retrieve a list of every `Transfer` in a `Settlement` that has `type` **DEBIT** or **REFUND**.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_transfers_by_settlement_id(settlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_id (str): ID of `Settlement` object.

        Keyword Args:
            limit (int): The numbers of items to return.. [optional]
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
        kwargs['settlement_id'] = \
            settlement_id
        ret = self._list_transfers_by_settlement_id_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_transfers_by_settlement_id,  **kwargs)
        return fl

    def list(
        self,
        **kwargs
    ):
        """List All Settlements  # noqa: E501

        Retrieve a list of `Settlements`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            amount (int): Filter by an amount equal to the given value.. [optional]
            amount_gt (int): Filter by an amount greater than.. [optional]
            amount_gte (int): Filter by an amount greater than or equal.. [optional]
            amount_lt (int): Filter by an amount less than.. [optional]
            amount_lte (int): Filter by an amount less than or equal.. [optional]
            status (str): Filter by the status of the `Settlement`. Available values include:<ul><li>**PENDING**<li>**STAGED**<li>**AWAITING_APPROVAL**<li>**APPROVED**.</ul> Merchants only receive payouts when `Settlements` are **APPROVED**. For more information, see [Payouts](/docs/guides/payouts/payouts/).. [optional]
            transfer_id (str): Filter by a `transfer_id` a `Settlement` has accrued. Please note this filter is only available for non-versioned requests, or requests using `-H 'Finix-Version: 2018-01-01'`. We're actively working on making this filter available for later versions. For more details, see [Versioning](/guides/developers/versioning/).. [optional]
            funding_transfer_id (str): Filter by a `funding_transfer` a `Settlement` has created.. [optional]
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
            SettlementsList
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

    def remove_transfers_from_settlement(
        self,
        settlement_id,
        **kwargs
    ):
        """Delete Settlement Transfers  # noqa: E501

        Remove a `Transfer` that makes up a `Settlement`.  As long as the `Settlement` hasn't been funded, you can remove the `Transfer` or an array of `Transfers`, along with its corresponding `fee` from the encompassing `Settlement`. - Funding `transfers` can't be deleted.   > Per the JSON API for deleting a resource, our API doesn't have a response body when removing a `Transfer` from a `Settlement`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.remove_transfers_from_settlement(settlement_id, async_req=True)
        >>> result = thread.get()

        Args:
            settlement_id (str): ID of `Settlement` object.

        Keyword Args:
            remove_settlement_transfer (RemoveSettlementTransfer): [optional]
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
            None
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
        kwargs['settlement_id'] = \
            settlement_id
        return self._remove_transfers_from_settlement_endpoint.call_with_http_info(**kwargs)

