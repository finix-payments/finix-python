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
from finix.model.application import Application
from finix.model.create_application_request import CreateApplicationRequest
from finix.model.create_settlement_request import CreateSettlementRequest
from finix.model.create_verification_request import CreateVerificationRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error422_invalid_field_list import Error422InvalidFieldList
from finix.model.error_generic import ErrorGeneric
from finix.model.settlement import Settlement
from finix.model.split_transfers_list import SplitTransfersList
from finix.model.verification import Verification
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

class DefaultApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Application,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/applications',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_application_request',
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
                    'create_application_request':
                        (CreateApplicationRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_application_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
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
                    'accept',
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
                    'accept':
                        (str,),
                    'create_settlement_request':
                        (CreateSettlementRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'identity_id': 'path',
                    'accept': 'header',
                    'create_settlement_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Verification,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/verifications',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_verification_request',
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
                    'create_verification_request':
                        (CreateVerificationRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_verification_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'application/json'
                ]
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
                    'accept',
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
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'parent_transfer_id': 'parent_transfer_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'parent_transfer_id': 'query',
                    'accept': 'header',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )

    def create(
        self,
        **kwargs
    ):
        """Create an Application  # noqa: E501

        If created successfully, a 201 response gets returned and adds a location header to the response which refers to the new created `Application`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_application_request (CreateApplicationRequest): [optional]
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
            Application
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
            accept (str): [optional] if omitted the server will use the default value of "application/hal+json"
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

    def create(
        self,
        **kwargs
    ):
        """Create a Merchant Verification  # noqa: E501

        Create a `Verification` to verify a seller's `Identity`.  Verifications can also be created directly on the resources you want to verify. For example: - `POST /merchants/{merchant_id}/verifications` - `POST /payment_instruments/{payment_instrument_id}/verifications`  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_verification_request (CreateVerificationRequest): [optional]
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
            Verification
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
            accept (str): [optional] if omitted the server will use the default value of "application/hal+json"
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

