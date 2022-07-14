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
from finix.model.adjustment_transfers_list import AdjustmentTransfersList
from finix.model.create_dispute_evidence_request import CreateDisputeEvidenceRequest
from finix.model.dispute import Dispute
from finix.model.dispute_evidence import DisputeEvidence
from finix.model.dispute_evidence_list import DisputeEvidenceList
from finix.model.disputes_list import DisputesList
from finix.model.error401_unauthorized import Error401Unauthorized
from finix.model.error403_forbidden_list import Error403ForbiddenList
from finix.model.error404_not_found_list import Error404NotFoundList
from finix.model.error406_not_acceptable import Error406NotAcceptable

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

class DisputesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._create_dispute_evidence_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (DisputeEvidence,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/evidence',
                'operation_id': 'create_dispute_evidence',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'create_dispute_evidence_request',
                ],
                'required': [
                    'dispute_id',
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
                    'dispute_id':
                        (str,),
                    'create_dispute_evidence_request':
                        (CreateDisputeEvidenceRequest,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'create_dispute_evidence_request': 'body',
                },
                'collection_format_map': {
                }
            },
            headers_map={
                'accept': [
                    'application/hal+json'
                ],
                'content_type': [
                    'multipart/form-data'
                ]
            },
            api_client=api_client
        )
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Dispute,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                ],
                'required': [
                    'dispute_id',
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
                    'dispute_id':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                },
                'location_map': {
                    'dispute_id': 'path',
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
        self._get_dispute_evidence_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (DisputeEvidence,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/evidence/{evidence_id}',
                'operation_id': 'get_dispute_evidence',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'evidence_id',
                ],
                'required': [
                    'dispute_id',
                    'evidence_id',
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
                    'dispute_id':
                        (str,),
                    'evidence_id':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'evidence_id': 'evidence_id',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'evidence_id': 'path',
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
        self._list_dispute_evidence_by_dispute_id_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (DisputeEvidenceList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/evidence',
                'operation_id': 'list_dispute_evidence_by_dispute_id',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'limit',
                    'after_cursor',
                    'before_cursor',
                ],
                'required': [
                    'dispute_id',
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
                    'dispute_id':
                        (str,),
                    'limit':
                        (int,),
                    'after_cursor':
                        (str,),
                    'before_cursor':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'dispute_id': 'path',
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
                'response_type': (DisputesList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes',
                'operation_id': 'list',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'sort',
                    'offset',
                    'limit',
                    'created_at_gte',
                    'created_at_lte',
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
                    'sort':
                        (str,),
                    'offset':
                        (int,),
                    'limit':
                        (int,),
                    'created_at_gte':
                        (str,),
                    'created_at_lte':
                        (str,),
                    'updated_at_gte':
                        (str,),
                    'updated_at_lte':
                        (str,),
                },
                'attribute_map': {
                    'sort': 'sort',
                    'offset': 'offset',
                    'limit': 'limit',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                },
                'location_map': {
                    'sort': 'query',
                    'offset': 'query',
                    'limit': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
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
        self._list_disputes_adjustments_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (AdjustmentTransfersList,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/adjustment_transfers',
                'operation_id': 'list_disputes_adjustments',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'limit',
                    'offset',
                ],
                'required': [
                    'dispute_id',
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
                    'dispute_id':
                        (str,),
                    'limit':
                        (int,),
                    'offset':
                        (int,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'limit': 'limit',
                    'offset': 'offset',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'limit': 'query',
                    'offset': 'query',
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

    def create_dispute_evidence(
        self,
        dispute_id,
        **kwargs
    ):
        """Create Dispute Evidence  # noqa: E501

        Upload dispute evidence for a `Dispute`.  There are four values available for `state` that details the status of the evidence upload:  * **PENDING**: The evidence file has not yet been submitted to the `Processor`. No user action is required. * **SUCCEEDED**: The evidence file has been successfully sent to the `Processor`. No further user action is required. * **CANCELED**: The evidence file upload was not completed due to user action. * **FAILED**: An issue occurred. User action is required. Any of the following issues could have occurred:     * There was an error in the system and the user should retry uploading their evidence file.     * There is an issue with the file and the user should retry uploading a different file.     * There is an issue and the user should contact Support.   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dispute_evidence(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to mange evidence for.

        Keyword Args:
            create_dispute_evidence_request (CreateDisputeEvidenceRequest): [optional]
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
            DisputeEvidence
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
        kwargs['dispute_id'] = \
            dispute_id
        return self._create_dispute_evidence_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        dispute_id,
        **kwargs
    ):
        """Get Dispute  # noqa: E501

        Retrieve the details of a previously created `Dispute`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to fetch.

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
            Dispute
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
        kwargs['dispute_id'] = \
            dispute_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def get_dispute_evidence(
        self,
        dispute_id,
        evidence_id,
        **kwargs
    ):
        """Fetch Dispute Evidence  # noqa: E501

        Fetch evidence uploaded for a `Dispute`.   If you don't have the Finix Dashboard available, you can fetch the evidence to review the `status` of the upload to confirm the evidence got sent to the processor.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get_dispute_evidence(dispute_id, evidence_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to fetch evidence for.
            evidence_id (str): ID of `evidence` to fetch.

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
            DisputeEvidence
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
        kwargs['dispute_id'] = \
            dispute_id
        kwargs['evidence_id'] = \
            evidence_id
        return self._get_dispute_evidence_endpoint.call_with_http_info(**kwargs)

    def list_dispute_evidence_by_dispute_id(
        self,
        dispute_id,
        **kwargs
    ):
        """List Dispute Evidence  # noqa: E501

        Retrieve a list of dispute evidence for a `Dispute`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_dispute_evidence_by_dispute_id(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to mange evidence for.

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
            DisputeEvidenceList
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
        kwargs['dispute_id'] = \
            dispute_id
        return self._list_dispute_evidence_by_dispute_id_endpoint.call_with_http_info(**kwargs)

    def list(
        self,
        **kwargs
    ):
        """List Disputes  # noqa: E501

        Retrieve a list of `Disputes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            sort (str): Specify key to be used for sorting the collection. [optional]
            offset (int): The number of items to skip before starting to collect the result set. [optional]
            limit (int): The numbers of items to return. [optional]
            created_at_gte (str): Filter where created_at is after the given date.. [optional]
            created_at_lte (str): Filter where created_at is before the given date.. [optional]
            updated_at_gte (str): Filter where updated_at is after the given date. [optional]
            updated_at_lte (str): Filter where updated_at is before the given date. [optional]
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
            DisputesList
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

    def list_disputes_adjustments(
        self,
        dispute_id,
        **kwargs
    ):
        """Fetch Dispute Adjustment Transfers  # noqa: E501

        List the adjustment `Transfers` for a `Dispute`. Depending on the stage of the `Dispute`, different adjustment `Transfer` subtypes can be applied.  There are four available subtypes for adjustment `Transfers` in `Disputes`: <ul><li><strong>PLATFORM\\_CREDIT</strong><li><strong>MERCHANT\\_DEBIT</strong><li><strong>MERCHANT\\_CREDIT</strong><li><strong>PLATFORM\\_DEBIT</strong></ul>  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.list_disputes_adjustments(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of the `Dispute` resource.

        Keyword Args:
            limit (int): The numbers of items to return. [optional]
            offset (int): The number of items to skip before starting to collect the result set. [optional]
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
            AdjustmentTransfersList
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
        kwargs['dispute_id'] = \
            dispute_id
        return self._list_disputes_adjustments_endpoint.call_with_http_info(**kwargs)

