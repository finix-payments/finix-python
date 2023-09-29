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
from typing_extensions import Annotated
from pydantic import Field, StrictInt, StrictStr

from typing import Optional, Union

from finix.models.create_external_link_request import CreateExternalLinkRequest
from finix.models.create_file_request import CreateFileRequest
from finix.models.external_link import ExternalLink
from finix.models.external_links_list import ExternalLinksList
from finix.models.file import File
from finix.models.files_list import FilesList
from finix.models.upload_file_request import UploadFileRequest
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

class FilesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_external_link_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (ExternalLink,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}/external_links',
                'operation_id': 'create_external_link',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'accept',
                    'create_external_link_request',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'accept':
                        (str,),
                    'create_external_link_request':
                        (CreateExternalLinkRequest,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'file_id': 'path',
                    'accept': 'header',
                    'create_external_link_request': 'body',
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
                'response_type': (File,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files',
                'operation_id': 'create',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'create_file_request',
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
                    'create_file_request':
                        (CreateFileRequest,),
                },
                'attribute_map': {
                },
                'location_map': {
                    'create_file_request': 'body',
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
        self._download_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (bytearray,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}/download',
                'operation_id': 'download',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'accept',
                    'stream',
                ],
                'required': [
                    'file_id',
                ],
                'nullable': [
                ],
                'enum': [
                    'stream',
                ],
                'validation': [
                ]
            },
            root_map={
                'validations': {
                },
                'allowed_values': {
                    ('stream',): {

                        "&#39;true&#39;": 'true',
                        "&#39;false&#39;": 'false'
                    },
                },
                'openapi_types': {
                    'file_id':
                        (str,),
                    'accept':
                        (str,),
                    'stream':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'accept': 'Accept',
                    'stream': 'stream',
                },
                'location_map': {
                    'file_id': 'path',
                    'accept': 'header',
                    'stream': 'query',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/octet-stream',
                    'application/json'
                ],
                'content_type': [],
            },
            api_client=api_client
        )
        self._get_external_link_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (ExternalLink,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}/external_links/{external_link_id}',
                'operation_id': 'get_external_link',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'external_link_id',
                    'accept',
                ],
                'required': [
                    'file_id',
                    'external_link_id',
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
                    'file_id':
                        (str,),
                    'external_link_id':
                        (str,),
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'external_link_id': 'external_link_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'file_id': 'path',
                    'external_link_id': 'path',
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
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'accept',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'file_id': 'path',
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
        self._list_external_links_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (ExternalLinksList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}/external_links',
                'operation_id': 'list_external_links',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'accept',
                    'after_cursor',
                    'limit',
                    'id',
                    'created_at_gte',
                    'created_at_lte',
                    'updated_at_gte',
                    'updated_at_lte',
                    'before_cursor',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'accept':
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
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'accept': 'Accept',
                    'after_cursor': 'after_cursor',
                    'limit': 'limit',
                    'id': 'id',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'file_id': 'path',
                    'accept': 'header',
                    'after_cursor': 'query',
                    'limit': 'query',
                    'id': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'before_cursor': 'query',
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
        self._list_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (FilesList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'after_cursor',
                    'limit',
                    'id',
                    'created_at_gte',
                    'created_at_lte',
                    'updated_at_gte',
                    'updated_at_lte',
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
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'after_cursor': 'after_cursor',
                    'limit': 'limit',
                    'id': 'id',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'after_cursor': 'query',
                    'limit': 'query',
                    'id': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'before_cursor': 'query',
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
        self._upload_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (File,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/files/{file_id}/upload',
                'operation_id': 'upload',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'file_id',
                    'accept',
                    'upload_file_request',
                ],
                'required': [
                    'file_id',
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
                    'file_id':
                        (str,),
                    'accept':
                        (str,),
                    'upload_file_request':
                        (UploadFileRequest,),
                },
                'attribute_map': {
                    'file_id': 'file_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'file_id': 'path',
                    'accept': 'header',
                    'upload_file_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )

    def create_external_link(
        self,
        file_id,
        **kwargs
    ):
        """Create an External Link  # noqa: E501

        Create an `external_link` resource to share with users so they can upload files directly from their browser. For more info, see [Uploading files to Finix](/guides/onboarding/uploading-files-to-finix/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_external_link(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): Your `File` ID.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            create_external_link_request (CreateExternalLinkRequest): [optional]
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
            ExternalLink
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
        kwargs['file_id'] = \
            file_id
        return self._create_external_link_endpoint.call_with_http_info(**kwargs)

    def create(
        self,
        **kwargs
    ):
        """Create a File  # noqa: E501

        Before uploading a file, you need to create a `File` resource.   Once created, you can [upload](/guides/onboarding/uploading-files-to-finix/#how-to-upload-a-file-to-finix) your file to the new `File` resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            create_file_request (CreateFileRequest): [optional]
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
            File
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

    def download(
        self,
        file_id,
        **kwargs
    ):
        """Download a File  # noqa: E501

        Download a file that was uploaded to a `File` resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.download(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): The ID of the `File` that was created to upload the file.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            stream (str): Stream the contents of the `File` so it's displayed inline in the user's web browser.. [optional]
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
            bytearray
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
        kwargs['file_id'] = \
            file_id
        return self._download_endpoint.call_with_http_info(**kwargs)

    def get_external_link(
        self,
        file_id,
        external_link_id,
        **kwargs
    ):
        """Fetch an External LInk  # noqa: E501

        Fetch a previously created `external_link` resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_external_link(file_id, external_link_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): The ID of the `File` that has the links you want to retrieve.
            external_link_id (str): The ID of the `external_link` that you want to retireve.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
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
            ExternalLink
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
        kwargs['file_id'] = \
            file_id
        kwargs['external_link_id'] = \
            external_link_id
        return self._get_external_link_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        file_id,
        **kwargs
    ):
        """Fetch a File  # noqa: E501

        Retrieve the details of a `File` resource.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): Your `File` ID.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
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
            File
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
        kwargs['file_id'] = \
            file_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def list_external_links(
        self,
        file_id,
        **kwargs
    ):
        """List All External Links  # noqa: E501

        List the previously created `external_links` for a `File`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_external_links(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): Your `File` ID.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            limit (int): The numbers of items to return.. [optional]
            id (str): Filter by `id`.. [optional]
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]
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
            ExternalLinksList
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
        kwargs['file_id'] = \
            file_id
        ret = self._list_external_links_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_external_links,  **kwargs)
        return fl

    def list(
        self,
        **kwargs
    ):
        """List All Files  # noqa: E501

        List all the `File` resources you've created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            after_cursor (str): Return every resource created after the cursor value.. [optional]
            limit (int): The numbers of items to return.. [optional]
            id (str): Filter by `id`.. [optional]
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]
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
            FilesList
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

    def upload(
        self,
        file_id,
        **kwargs
    ):
        """Upload files Directly  # noqa: E501

        Upload files directly with a `multipart/form-data` request.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.upload(file_id, async_req=True)
        >>> result = thread.get()

        Args:
            file_id (str): The ID of the `File` that was created to upload the file.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            upload_file_request (UploadFileRequest): [optional]
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
            File
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
        kwargs['file_id'] = \
            file_id
        return self._upload_endpoint.call_with_http_info(**kwargs)

