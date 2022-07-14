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
from finix.model.create_identity_request import CreateIdentityRequest
from finix.model.create_verification_request import CreateVerificationRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.error_generic import ErrorGeneric
from finix.model.identities_list import IdentitiesList
from finix.model.identity import Identity
from finix.model.update_identity_request import UpdateIdentityRequest
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

class IdentitiesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_associated_identity_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Identity,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}/associated_identities',
                'operation_id': 'create_associated_identity',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'create_identity_request',
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
                    'create_identity_request':
                        (CreateIdentityRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                },
                'location_map': {
                    'identity_id': 'path',
                    'create_identity_request': 'body',
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
                'response_type': (Identity,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_identity_request',
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
                    'create_identity_request':
                        (CreateIdentityRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_identity_request': 'body',
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
        self._create_identity_verification_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Verification,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}/verifications',
                'operation_id': 'create_identity_verification',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'create_verification_request',
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
                    'create_verification_request':
                        (CreateVerificationRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                },
                'location_map': {
                    'identity_id': 'path',
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
                'response_type': (Identity,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
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
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                },
                'location_map': {
                    'identity_id': 'path',
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
                'response_type': (IdentitiesList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sort',
                    'after_cursor',
                    'limit',
                    'id',
                    'created_at_gte',
                    'created_at_lte',
                    'default_statement_descriptor',
                    'business_name',
                    'business_type',
                    'email',
                    'first_name',
                    'last_name',
                    'title',
                    'before_cursor',
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
                    'sort':
                        (str,),
                    'after_cursor':
                        (str,),
                    'limit':
                        (int,),
                    'id':
                        (str,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'default_statement_descriptor':
                        (str,),
                    'business_name':
                        (str,),
                    'business_type':
                        (str,),
                    'email':
                        (str,),
                    'first_name':
                        (str,),
                    'last_name':
                        (str,),
                    'title':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'sort': 'sort',
                    'after_cursor': 'after_cursor',
                    'limit': 'limit',
                    'id': 'id',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'default_statement_descriptor': 'default_statement_descriptor',
                    'business_name': 'business_name',
                    'business_type': 'business_type',
                    'email': 'email',
                    'first_name': 'first_name',
                    'last_name': 'last_name',
                    'title': 'title',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'sort': 'query',
                    'after_cursor': 'query',
                    'limit': 'query',
                    'id': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'default_statement_descriptor': 'query',
                    'business_name': 'query',
                    'business_type': 'query',
                    'email': 'query',
                    'first_name': 'query',
                    'last_name': 'query',
                    'title': 'query',
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
        self._list_assocaiated_identities_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (IdentitiesList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}/associated_identities',
                'operation_id': 'list_assocaiated_identities',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'limit',
                    'after_cursor',
                    'before_cursor',
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
                    'limit':
                        (int,),
                    'after_cursor':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'identity_id': 'path',
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
        self._update_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Identity,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/identities/{identity_id}',
                'operation_id': 'update',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'identity_id',
                    'update_identity_request',
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
                    'update_identity_request':
                        (UpdateIdentityRequest,),
                },
                'attribute_map': {
                    'identity_id': 'identity_id',
                },
                'location_map': {
                    'identity_id': 'path',
                    'update_identity_request': 'body',
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

    def create_associated_identity(
        self,
        identity_id,
        **kwargs
    ):
        """Create an Associated Identity  # noqa: E501

        Create an associated `Identity` for [every owner with 25% or more ownership](/guides/onboarding/#step-3-add-associated-identities) over the merchant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_associated_identity(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of `Identity` to associate object with.

        Keyword Args:
            create_identity_request (CreateIdentityRequest): [optional]
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
            Identity
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
        return self._create_associated_identity_endpoint.call_with_http_info(**kwargs)

    def create(
        self,
        **kwargs
    ):
        """Create an Identity  # noqa: E501

        Create an `Identity` for your merchant or buyer.  Creating `Identities` for merchants requires they provide [KYC details](/docs/guides/getting-started/).  Related Guides: [Getting Started](/docs/guides/getting-started/), [Onboarding](/docs/guides/onboarding/)  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_identity_request (CreateIdentityRequest): [optional]
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
            Identity
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

    def create_identity_verification(
        self,
        identity_id,
        **kwargs
    ):
        """Verify an Identity  # noqa: E501

        Verify an `Identity`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_identity_verification(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of identity to fetch

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
        kwargs['identity_id'] = \
            identity_id
        return self._create_identity_verification_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        identity_id,
        **kwargs
    ):
        """Fetch an Identity  # noqa: E501

        Retrieve the details of a previously created `Identity`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of the `identity` to fetch

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
            Identity
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
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Identities  # noqa: E501

        Retrieves a list of `Identities`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sort (str): Specify key to be used for sorting the collection. [optional]
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            limit (int): The numbers of items to return. [optional]
            id (str): Filter by id. [optional]
            created_at_gte (str): Filter where created_at is after the given date.. [optional]
            created_at_lte (str): Filter where created_at is before the given date.. [optional]
            default_statement_descriptor (str): Filter by the default_statement_descriptor. [optional]
            business_name (str): Filter by the full business name. Partial business names are not supported.. [optional]
            business_type (str): Filter by the business type. Partial business types are not supported. [optional]
            email (str): Filter by the email address or email domain. Partial emails are not supported.. [optional]
            first_name (str): Filter by the first name of the person associated to the Identity.. [optional]
            last_name (str): Filter by the last name of the person associated to the identity.. [optional]
            title (str): Filter by the title if available.. [optional]
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
            IdentitiesList
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

    def list_assocaiated_identities(
        self,
        identity_id,
        **kwargs
    ):
        """List Associated Identities  # noqa: E501

        Retrieve a list of `Associated Identities` for an `Identity`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_assocaiated_identities(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of `Identity` to associate object with.

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
            IdentitiesList
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
        return self._list_assocaiated_identities_endpoint.call_with_http_info(**kwargs)

    def update(
        self,
        identity_id,
        **kwargs
    ):
        """Update an Identity  # noqa: E501

        Update an existing `Identity`.  If you are updating the `Identity` of a `Merchant` that’s already been onboarded, you need to [verify the merchant again](#operation/createMerchantVerification).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update(identity_id, async_req=True)
        >>> result = thread.get()

        Args:
            identity_id (str): ID of the `identity` to fetch

        Keyword Args:
            update_identity_request (UpdateIdentityRequest): [optional]
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
            Identity
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
        return self._update_endpoint.call_with_http_info(**kwargs)

