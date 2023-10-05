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
from finix.model.create_merchant_underwriting_request import CreateMerchantUnderwritingRequest
from finix.model.create_verification_request import CreateVerificationRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error_generic import ErrorGeneric
from finix.model.merchant import Merchant
from finix.model.merchants_list import MerchantsList
from finix.model.update_merchant_request import UpdateMerchantRequest
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

class MerchantsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Merchant,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}/merchants',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'finix_version',
                    'create_merchant_underwriting_request',
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
                    'finix_version':
                        (str,),
                    'create_merchant_underwriting_request':
                        (CreateMerchantUnderwritingRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'identity_id': 'path',
                    'finix_version': 'header',
                    'create_merchant_underwriting_request': 'body',
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
        self._create_merchant_verification_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Verification,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/merchants/{merchant_id}/verifications',
                'operation_id': 'create_merchant_verification',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_id',
                    'finix_version',
                    'create_verification_request',
                ],
                'required': [
                    'merchant_id',
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
                    'merchant_id':
                        (str,),
                    'finix_version':
                        (str,),
                    'create_verification_request':
                        (CreateVerificationRequest,),
                },
                'attribute_map': {
                    'merchant_id': 'merchant_id',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'merchant_id': 'path',
                    'finix_version': 'header',
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
                    'application/json'
                ]
            },
            api_client=api_client
        )
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Merchant,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/merchants/{merchant_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_id',
                ],
                'required': [
                    'merchant_id',
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
                    'merchant_id':
                        (str,),
                },
                'attribute_map': {
                    'merchant_id': 'merchant_id',
                },
                'location_map': {
                    'merchant_id': 'path',
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
                'response_type': (MerchantsList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/merchants',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'id',
                    'after_cursor',
                    'before_cursor',
                    'created_at_gte',
                    'created_at_lte',
                    'limit',
                    'updated_at_gte',
                    'updated_at_lte',
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
                    'id':
                        (str,),
                    'after_cursor':
                        (str,),
                    'before_cursor':
                        (str,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'limit':
                        (int,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                },
                'attribute_map': {
                    'id': 'id',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'limit': 'limit',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                },
                'location_map': {
                    'id': 'query',
                    'after_cursor': 'query',
                    'before_cursor': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'limit': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
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
                'response_type': (Merchant,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/merchants/{merchant_id}',
                'operation_id': 'update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'merchant_id',
                    'finix_version',
                    'update_merchant_request',
                ],
                'required': [
                    'merchant_id',
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
                    'merchant_id':
                        (str,),
                    'finix_version':
                        (str,),
                    'update_merchant_request':
                        (UpdateMerchantRequest,),
                },
                'attribute_map': {
                    'merchant_id': 'merchant_id',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'merchant_id': 'path',
                    'finix_version': 'header',
                    'update_merchant_request': 'body',
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

    def create(
        self,
        identity_id,
        **kwargs
    ):
        """Create a Merchant  # noqa: E501

        Create a `Merchant` to start the underwriting (also called provisioning) process for your seller. `Merchants` must be created under an [`Identity`](/api/tag/Identities).  A bank account must be associated with the previously created `Identity` before a `Merchant` can be successfully onboarded and verified.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of `Identity` to fetch.

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            create_merchant_underwriting_request (CreateMerchantUnderwritingRequest): [optional]
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
            Merchant
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

    def create_merchant_verification(
        self,
        merchant_id,
        **kwargs
    ):
        """Verify a Merchant  # noqa: E501

        Verify a `Merchant` if the `onboarding_state` for a `Merchant` returns **FAILED**, or if the correct the seller needs to update the saved in their information `Identity`.  Related Guides: [Onboarding Process](/guides/onboarding/onboarding-process/#reverify-a-merchant)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_merchant_verification(merchant_id, async_req=True)
        >>> result = thread.get()

        Args:
            merchant_id (str): ID of `Merchant` object.

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
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
        kwargs['merchant_id'] = \
            merchant_id
        return self._create_merchant_verification_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        merchant_id,
        **kwargs
    ):
        """Fetch a Merchant  # noqa: E501

        Retrieve the details of a `Merchant`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(merchant_id, async_req=True)
        >>> result = thread.get()

        Args:
            merchant_id (str): ID of `Merchant`.

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
            Merchant
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
        kwargs['merchant_id'] = \
            merchant_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Merchants  # noqa: E501

        Retrieve a list of `Merchants`.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            id (str): Filter by `id`.. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            before_cursor (str): Return every resource created before the cursor value.. [optional]
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            limit (int): The numbers of items to return.. [optional]
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]
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
            MerchantsList
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

    def update(
        self,
        merchant_id,
        **kwargs
    ):
        """Update a Merchant  # noqa: E501

        Update a `Merchant` to:  - Change the `Identity` information saved with the underlying processor - [Enable Level 2/3 processing](/guides/payments/making-a-payment/level-2-and-level-3-processing/) - Enable [buyer charges](/guides/payments/making-a-payment/buyer-charges/) - Disable a `Merchant` so the seller can't create new `Transfers` and `Authorizations`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(merchant_id, async_req=True)
        >>> result = thread.get()

        Args:
            merchant_id (str): ID of `Merchant`.

        Keyword Args:
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of "2018-01-01"
            update_merchant_request (UpdateMerchantRequest): [optional]
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
            Merchant
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
        kwargs['merchant_id'] = \
            merchant_id
        return self._update_endpoint.call_with_http_info(**kwargs)

