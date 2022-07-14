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
from finix.model.apple_pay_session import ApplePaySession
from finix.model.apple_pay_session_request import ApplePaySessionRequest
from finix.model.create_payment_instrument_request import CreatePaymentInstrumentRequest
from finix.model.create_verification_request import CreateVerificationRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error422_invalid_field_list import Error422InvalidFieldList
from finix.model.error_generic import ErrorGeneric
from finix.model.payment_instrument import PaymentInstrument
from finix.model.payment_instruments_list import PaymentInstrumentsList
from finix.model.update_payment_instrument_request import UpdatePaymentInstrumentRequest
from finix.model.verification import Verification

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

class PaymentInstrumentsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_apple_pay_session_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (ApplePaySession,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/apple_pay_sessions',
                'operation_id': 'create_apple_pay_session',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'apple_pay_session_request',
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
                    'apple_pay_session_request':
                        (ApplePaySessionRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'apple_pay_session_request': 'body',
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
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (PaymentInstrument,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/payment_instruments',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_payment_instrument_request',
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
                    'create_payment_instrument_request':
                        (CreatePaymentInstrumentRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_payment_instrument_request': 'body',
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
        self._create_payment_instrument_verification_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Verification,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/payment_instruments/{payment_instrument_id}/verifications',
                'operation_id': 'create_payment_instrument_verification',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_instrument_id',
                    'create_verification_request',
                ],
                'required': [
                    'payment_instrument_id',
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
                    'payment_instrument_id':
                        (str,),
                    'create_verification_request':
                        (CreateVerificationRequest,),
                },
                'attribute_map': {
                    'payment_instrument_id': 'payment_instrument_id',
                },
                'location_map': {
                    'payment_instrument_id': 'path',
                    'create_verification_request': 'body',
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
                'response_type': (PaymentInstrument,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/payment_instruments/{payment_instrument_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_instrument_id',
                ],
                'required': [
                    'payment_instrument_id',
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
                    'payment_instrument_id':
                        (str,),
                },
                'attribute_map': {
                    'payment_instrument_id': 'payment_instrument_id',
                },
                'location_map': {
                    'payment_instrument_id': 'path',
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
                'response_type': (PaymentInstrumentsList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/payment_instruments',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'limit',
                    'after_cursor',
                    'account_last4',
                    'account_routing_number',
                    'application',
                    'bin',
                    'created_at_gte',
                    'created_at_lte',
                    'expiration_month',
                    'expiration_year',
                    'last_four',
                    'name',
                    'owner_identity_id',
                    'type',
                    'before_cursor',
                ],
                'required': [],
                'nullable': [
                ],
                'enum': [
                    'type',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('type',): {

                        "ALL": "ALL",
                        "BANK_ACCOUNT": "BANK_ACCOUNT",
                        "PAYMENT_CARD": "PAYMENT_CARD"
                    },
                },
                'openapi_types': {
                    'limit':
                        (int,),
                    'after_cursor':
                        (str,),
                    'account_last4':
                        (str,),
                    'account_routing_number':
                        (str,),
                    'application':
                        (str,),
                    'bin':
                        (str,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'expiration_month':
                        (str,),
                    'expiration_year':
                        (str,),
                    'last_four':
                        (str,),
                    'name':
                        (str,),
                    'owner_identity_id':
                        (str,),
                    'type':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'account_last4': 'account_last4',
                    'account_routing_number': 'account_routing_number',
                    'application': 'application',
                    'bin': 'bin',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'expiration_month': 'expiration_month',
                    'expiration_year': 'expiration_year',
                    'last_four': 'last_four',
                    'name': 'name',
                    'owner_identity_id': 'owner_identity_id',
                    'type': 'type',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'limit': 'query',
                    'after_cursor': 'query',
                    'account_last4': 'query',
                    'account_routing_number': 'query',
                    'application': 'query',
                    'bin': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'expiration_month': 'query',
                    'expiration_year': 'query',
                    'last_four': 'query',
                    'name': 'query',
                    'owner_identity_id': 'query',
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
                'response_type': (PaymentInstrument,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/payment_instruments/{payment_instrument_id}',
                'operation_id': 'update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'payment_instrument_id',
                    'update_payment_instrument_request',
                ],
                'required': [
                    'payment_instrument_id',
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
                    'payment_instrument_id':
                        (str,),
                    'update_payment_instrument_request':
                        (UpdatePaymentInstrumentRequest,),
                },
                'attribute_map': {
                    'payment_instrument_id': 'payment_instrument_id',
                },
                'location_map': {
                    'payment_instrument_id': 'path',
                    'update_payment_instrument_request': 'body',
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

    def create_apple_pay_session(
        self,
        **kwargs
    ):
        """Create an Apple Pay Session  # noqa: E501

        Create an `apple_pay_session` to process Apple Pay transactions on the web.  To create an Apple Pay Session, pass the unique `validation_url` (provided by Apple) while creating an `apple_pay_sessions` resource. Finix returns a `merchantSession` object that you can use to create a payment. For more information, see [Apple Pay](/docs/guides/payments/alternative-payment-methods/apple-pay/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_apple_pay_session(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            apple_pay_session_request (ApplePaySessionRequest): [optional]
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
            ApplePaySession
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
        return self._create_apple_pay_session_endpoint.call_with_http_info(**kwargs)

    def create(
        self,
        **kwargs
    ):
        """Create a Payment Instrument  # noqa: E501

        Create a `Payment Instrument` resource using a card or bank account.  To accept payment details, review our guide on how to [tokenize cards using hosted fields](/guides/payments/tokenization-with-hosted-fields).  > The creation of `Payment Instruments` using cards directly via Finix's API should only be done for testing purposes. You must use the Hosted Tokenization fields or javascript client to remain out of PCI scope.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_payment_instrument_request (CreatePaymentInstrumentRequest): [optional]
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
            PaymentInstrument
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

    def create_payment_instrument_verification(
        self,
        payment_instrument_id,
        **kwargs
    ):
        """Verify a Payment Instrument  # noqa: E501

        Verify a `Payment Instrument` to determine if it's elligable for Push To Card transactions.   > Only verify `Payment Instruments` for [Push To Card](/guides/push-to-card) customers.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_payment_instrument_verification(payment_instrument_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_instrument_id (str): ID of object

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
        kwargs['payment_instrument_id'] = \
            payment_instrument_id
        return self._create_payment_instrument_verification_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        payment_instrument_id,
        **kwargs
    ):
        """Get a Payment Instrument  # noqa: E501

        Retrieve the details of a `Payment Instrument`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(payment_instrument_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_instrument_id (str): ID of object

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
            PaymentInstrument
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
        kwargs['payment_instrument_id'] = \
            payment_instrument_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Payment Instruments  # noqa: E501

        Retrieve a list of `Payment Instruments`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            limit (int): The numbers of items to return. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            account_last4 (str): Filter by the last 4 digits of the account if available.. [optional]
            account_routing_number (str): Filter by the account routing number if available.. [optional]
            application (str): Filter by application id. [optional]
            bin (str): Filter by Bank Identification Number (BIN). The BIN is the first 6 digits of the masked number. [optional]
            created_at_gte (str): Filter where created_at is after the given date.. [optional]
            created_at_lte (str): Filter where created_at is before the given date.. [optional]
            expiration_month (str): Filter by the expiration month associated with the `Payment Instrument` if applicable. This filter only applies to payment cards.. [optional]
            expiration_year (str): Filter by the 4 digit expiration year associated with the Payment Instrument if applicable. This filter only applies to payment cards. [optional]
            last_four (str): Filter by the last 4 digits of the Payment Instrument card. This filter only applies to payment cards.. [optional]
            name (str): Filter by the name.. [optional]
            owner_identity_id (str): Filter by the owner id of the associated identity.. [optional]
            type (str): Filter by the payment instrument type.. [optional]
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
            PaymentInstrumentsList
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
        payment_instrument_id,
        **kwargs
    ):
        """Update a Payment Instrument  # noqa: E501

        Update a `Payment Instrument`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(payment_instrument_id, async_req=True)
        >>> result = thread.get()

        Args:
            payment_instrument_id (str): ID of object

        Keyword Args:
            update_payment_instrument_request (UpdatePaymentInstrumentRequest): [optional]
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
            PaymentInstrument
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
        kwargs['payment_instrument_id'] = \
            payment_instrument_id
        return self._update_endpoint.call_with_http_info(**kwargs)

