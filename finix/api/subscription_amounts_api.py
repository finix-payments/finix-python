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
from finix.model.create_subscription_amount_request import CreateSubscriptionAmountRequest
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable
from finix.model.subscription_amount import SubscriptionAmount
from finix.model.subscription_amount_list import SubscriptionAmountList

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

class SubscriptionAmountsApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._lcreate_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SubscriptionAmount,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/subscription/subscription_schedules/{subscription_schedule_id}/subscription_amounts',
                'operation_id': 'lcreate',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'subscription_schedule_id',
                    'create_subscription_amount_request',
                ],
                'required': [
                    'subscription_schedule_id',
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
                    'subscription_schedule_id':
                        (str,),
                    'create_subscription_amount_request':
                        (CreateSubscriptionAmountRequest,),
                },
                'attribute_map': {
                    'subscription_schedule_id': 'subscription_schedule_id',
                },
                'location_map': {
                    'subscription_schedule_id': 'path',
                    'create_subscription_amount_request': 'body',
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
        self._delete_subscription_amount_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': None,
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/subscription/subscription_schedules/{subscription_schedule_id}/subscription_amounts/{subscription_amount_id}',
                'operation_id': 'delete_subscription_amount',
                'http_method': 'DELETE',
                'servers': None,
            },
            params_map={
                'all': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
                ],
                'required': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
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
                    'subscription_amount_id':
                        (str,),
                    'subscription_schedule_id':
                        (str,),
                },
                'attribute_map': {
                    'subscription_amount_id': 'subscription_amount_id',
                    'subscription_schedule_id': 'subscription_schedule_id',
                },
                'location_map': {
                    'subscription_amount_id': 'path',
                    'subscription_schedule_id': 'path',
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
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SubscriptionAmount,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/subscription/subscription_schedules/{subscription_schedule_id}/subscription_amounts/{subscription_amount_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
                ],
                'required': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
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
                    'subscription_amount_id':
                        (str,),
                    'subscription_schedule_id':
                        (str,),
                },
                'attribute_map': {
                    'subscription_amount_id': 'subscription_amount_id',
                    'subscription_schedule_id': 'subscription_schedule_id',
                },
                'location_map': {
                    'subscription_amount_id': 'path',
                    'subscription_schedule_id': 'path',
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
        self._list_by_subscription_schedule_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SubscriptionAmountList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/subscription/subscription_schedules/{subscription_schedule_id}/subscription_amounts',
                'operation_id': 'list_by_subscription_schedule',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'subscription_schedule_id',
                    'limit',
                    'after_cursor',
                    'before_cursor',
                ],
                'required': [
                    'subscription_schedule_id',
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
                    'subscription_schedule_id':
                        (str,),
                    'limit':
                        (int,),
                    'after_cursor':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'subscription_schedule_id': 'subscription_schedule_id',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'subscription_schedule_id': 'path',
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
        self._patch_subscription_amount_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (SubscriptionAmount,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/subscription/subscription_schedules/{subscription_schedule_id}/subscription_amounts/{subscription_amount_id}',
                'operation_id': 'patch_subscription_amount',
                'http_method': 'PATCH',
                'servers': None,
            },
            params_map={
                'all': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
                    'create_subscription_amount_request',
                ],
                'required': [
                    'subscription_amount_id',
                    'subscription_schedule_id',
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
                    'subscription_amount_id':
                        (str,),
                    'subscription_schedule_id':
                        (str,),
                    'create_subscription_amount_request':
                        (CreateSubscriptionAmountRequest,),
                },
                'attribute_map': {
                    'subscription_amount_id': 'subscription_amount_id',
                    'subscription_schedule_id': 'subscription_schedule_id',
                },
                'location_map': {
                    'subscription_amount_id': 'path',
                    'subscription_schedule_id': 'path',
                    'create_subscription_amount_request': 'body',
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

    def lcreate(
        self,
        subscription_schedule_id,
        **kwargs
    ):
        """Create a Subscription Amount  # noqa: E501

        Create a `subscription_amount`.  The `Subscription Amount` is the amount to be charged to a `Merchant`. The `Subscription Amount` must be associated to a `Subscription Schedule`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.lcreate(subscription_schedule_id, async_req=True)
        >>> result = thread.get()

        Args:
            subscription_schedule_id (str): The ID of the `Subscription Schedule`.

        Keyword Args:
            create_subscription_amount_request (CreateSubscriptionAmountRequest): [optional]
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
            SubscriptionAmount
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
        kwargs['subscription_schedule_id'] = \
            subscription_schedule_id
        return self._lcreate_endpoint.call_with_http_info(**kwargs)

    def delete_subscription_amount(
        self,
        subscription_amount_id,
        subscription_schedule_id,
        **kwargs
    ):
        """Delete a Subscription Amount  # noqa: E501

        Delete a previously created `Subscription Amount`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.delete_subscription_amount(subscription_amount_id, subscription_schedule_id, async_req=True)
        >>> result = thread.get()

        Args:
            subscription_amount_id (str): The ID of the `Subscription Amount`.
            subscription_schedule_id (str): The ID of the `Subscription Schedule`.

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
        kwargs['subscription_amount_id'] = \
            subscription_amount_id
        kwargs['subscription_schedule_id'] = \
            subscription_schedule_id
        return self._delete_subscription_amount_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        subscription_amount_id,
        subscription_schedule_id,
        **kwargs
    ):
        """Get a Subscription Amount  # noqa: E501

        Retrieve the details of a `subscription_amount`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(subscription_amount_id, subscription_schedule_id, async_req=True)
        >>> result = thread.get()

        Args:
            subscription_amount_id (str): The ID of the `Subscription Amount`.
            subscription_schedule_id (str): The ID of the `Subscription Schedule`.

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
            SubscriptionAmount
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
        kwargs['subscription_amount_id'] = \
            subscription_amount_id
        kwargs['subscription_schedule_id'] = \
            subscription_schedule_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list_by_subscription_schedule(
        self,
        subscription_schedule_id,
        **kwargs
    ):
        """List Subscription Amounts  # noqa: E501

        Retrive a list of `Subscription Amounts`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_by_subscription_schedule(subscription_schedule_id, async_req=True)
        >>> result = thread.get()

        Args:
            subscription_schedule_id (str): The ID of the `Subscription Schedule`.

        Keyword Args:
            limit (int): The numbers of items to return. [optional]
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
            SubscriptionAmountList
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
        kwargs['subscription_schedule_id'] = \
            subscription_schedule_id
        return self._list_by_subscription_schedule_endpoint.call_with_http_info(**kwargs)

    def patch_subscription_amount(
        self,
        subscription_amount_id,
        subscription_schedule_id,
        **kwargs
    ):
        """Update a Subscription Amount  # noqa: E501

        Update the details of a `subscription_amount`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.patch_subscription_amount(subscription_amount_id, subscription_schedule_id, async_req=True)
        >>> result = thread.get()

        Args:
            subscription_amount_id (str): The ID of the `Subscription Amount`.
            subscription_schedule_id (str): The ID of the `Subscription Schedule`.

        Keyword Args:
            create_subscription_amount_request (CreateSubscriptionAmountRequest): [optional]
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
            SubscriptionAmount
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
        kwargs['subscription_amount_id'] = \
            subscription_amount_id
        kwargs['subscription_schedule_id'] = \
            subscription_schedule_id
        return self._patch_subscription_amount_endpoint.call_with_http_info(**kwargs)

