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

from finix.models.accept_dispute import AcceptDispute
from finix.models.adjustment_transfers_list import AdjustmentTransfersList
from finix.models.create_dispute_evidence_request import CreateDisputeEvidenceRequest
from finix.models.dispute import Dispute
from finix.models.dispute_evidence import DisputeEvidence
from finix.models.dispute_evidence_list import DisputeEvidenceList
from finix.models.disputes_list import DisputesList
from finix.models.submit_dispute_evidence import SubmitDisputeEvidence
from finix.models.update_dispute_evidence import UpdateDisputeEvidence
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

class DisputesApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = finix.api_client.FinixClient()
        self._api_client = api_client
        self._post_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Dispute,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/accept',
                'operation_id': 'post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'accept',
                    'accept_dispute',
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
                    'accept':
                        (str,),
                    'accept_dispute':
                        (AcceptDispute,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'accept_dispute': 'body',
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
                    'accept',
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
                    'accept':
                        (str,),
                    'create_dispute_evidence_request':
                        (CreateDisputeEvidenceRequest,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'create_dispute_evidence_request': 'body',
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
        self._get_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (bytearray,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/evidence/{evidence_id}/download',
                'operation_id': 'get',
                'http_method': 'GET',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'evidence_id',
                    'accept',
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
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'evidence_id': 'evidence_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'evidence_id': 'path',
                    'accept': 'header',
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
                    'accept',
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
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'dispute_id': 'path',
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
                    'accept',
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
                    'accept':
                        (str,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'evidence_id': 'evidence_id',
                    'accept': 'Accept',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'evidence_id': 'path',
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
                    'accept',
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
                    'accept':
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
                    'accept': 'Accept',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'limit': 'query',
                    'after_cursor': 'query',
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
                    'accept',
                    'limit',
                    'created_at_gte',
                    'created_at_lte',
                    'updated_at_gte',
                    'updated_at_lte',
                    'transfer_id',
                    'adjustment_transfer_id',
                    'amount',
                    'amount_gte',
                    'amount_gt',
                    'amount_lt',
                    'state',
                    'response_state',
                    'respond_by_lte',
                    'respond_by_gte',
                    'instrument_bin',
                    'instrument_brand_type',
                    'merchant_identity_id',
                    'merchant_identity_name',
                    'instrument_name',
                    'instrument_type',
                    'merchant_id',
                    'merchant_mid',
                    'instrument_card_last4',
                    'instrument_card_type',
                    'instrument_fingerprint',
                    'before_cursor',
                    'tags_key',
                    'tags_value',
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
                    'accept':
                        (str,),
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
                    'transfer_id':
                        (str,),
                    'adjustment_transfer_id':
                        (str,),
                    'amount':
                        (int,),
                    'amount_gte':
                        (int,),
                    'amount_gt':
                        (int,),
                    'amount_lt':
                        (int,),
                    'state':
                        (str,),
                    'response_state':
                        (str,),
                    'respond_by_lte':
                        (str,),
                    'respond_by_gte':
                        (str,),
                    'instrument_bin':
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
                    'instrument_card_type':
                        (str,),
                    'instrument_fingerprint':
                        (str,),
                    'before_cursor':
                        (str,),
                    'tags_key':
                        (str,),
                    'tags_value':
                        (str,),
                },
                'attribute_map': {
                    'accept': 'Accept',
                    'limit': 'limit',
                    'created_at_gte': 'created_at.gte',
                    'created_at_lte': 'created_at.lte',
                    'updated_at_gte': 'updated_at.gte',
                    'updated_at_lte': 'updated_at.lte',
                    'transfer_id': 'transfer_id',
                    'adjustment_transfer_id': 'adjustment_transfer_id',
                    'amount': 'amount',
                    'amount_gte': 'amount.gte',
                    'amount_gt': 'amount.gt',
                    'amount_lt': 'amount.lt',
                    'state': 'state',
                    'response_state': 'response_state',
                    'respond_by_lte': 'respond_by.lte',
                    'respond_by_gte': 'respond_by.gte',
                    'instrument_bin': 'instrument_bin',
                    'instrument_brand_type': 'instrument_brand_type',
                    'merchant_identity_id': 'merchant_identity_id',
                    'merchant_identity_name': 'merchant_identity_name',
                    'instrument_name': 'instrument_name',
                    'instrument_type': 'instrument_type',
                    'merchant_id': 'merchant_id',
                    'merchant_mid': 'merchant_mid',
                    'instrument_card_last4': 'instrument_card_last4',
                    'instrument_card_type': 'instrument_card_type',
                    'instrument_fingerprint': 'instrument_fingerprint',
                    'before_cursor': 'before_cursor',
                    'tags_key': 'tags.key',
                    'tags_value': 'tags.value',
                },
                'location_map': {
                    'accept': 'header',
                    'limit': 'query',
                    'created_at_gte': 'query',
                    'created_at_lte': 'query',
                    'updated_at_gte': 'query',
                    'updated_at_lte': 'query',
                    'transfer_id': 'query',
                    'adjustment_transfer_id': 'query',
                    'amount': 'query',
                    'amount_gte': 'query',
                    'amount_gt': 'query',
                    'amount_lt': 'query',
                    'state': 'query',
                    'response_state': 'query',
                    'respond_by_lte': 'query',
                    'respond_by_gte': 'query',
                    'instrument_bin': 'query',
                    'instrument_brand_type': 'query',
                    'merchant_identity_id': 'query',
                    'merchant_identity_name': 'query',
                    'instrument_name': 'query',
                    'instrument_type': 'query',
                    'merchant_id': 'query',
                    'merchant_mid': 'query',
                    'instrument_card_last4': 'query',
                    'instrument_card_type': 'query',
                    'instrument_fingerprint': 'query',
                    'before_cursor': 'query',
                    'tags_key': 'query',
                    'tags_value': 'query',
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
                    'accept',
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
                    'accept':
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
                    'accept': 'Accept',
                    'limit': 'limit',
                    'after_cursor': 'after_cursor',
                    'before_cursor': 'before_cursor',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'limit': 'query',
                    'after_cursor': 'query',
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
        self._post_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Dispute,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/submit',
                'operation_id': 'post',
                'http_method': 'POST',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'accept',
                    'finix_version',
                    'submit_dispute_evidence',
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
                    'accept':
                        (str,),
                    'finix_version':
                        (str,),
                    'submit_dispute_evidence':
                        (SubmitDisputeEvidence,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'accept': 'Accept',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'finix_version': 'header',
                    'submit_dispute_evidence': 'body',
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
        self._update_dispute_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (Dispute,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}',
                'operation_id': 'update_dispute',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'accept',
                    'finix_version',
                    'update_dispute_evidence',
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
                    'accept':
                        (str,),
                    'finix_version':
                        (str,),
                    'update_dispute_evidence':
                        (UpdateDisputeEvidence,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'accept': 'Accept',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'accept': 'header',
                    'finix_version': 'header',
                    'update_dispute_evidence': 'body',
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
        self._update_dispute_evidence_endpoint = finix.api_client.Endpoint(
            settings={
                'response_type': (DisputeEvidence,),
                'auth': [
                    'BasicAuth'
                ],
                'endpoint_path': '/disputes/{dispute_id}/evidence/{evidence_id}',
                'operation_id': 'update_dispute_evidence',
                'http_method': 'PUT',
                'servers': None,
            },
            params_map={
                'all': [
                    'dispute_id',
                    'evidence_id',
                    'accept',
                    'finix_version',
                    'update_dispute_evidence',
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
                    'accept':
                        (str,),
                    'finix_version':
                        (str,),
                    'update_dispute_evidence':
                        (UpdateDisputeEvidence,),
                },
                'attribute_map': {
                    'dispute_id': 'dispute_id',
                    'evidence_id': 'evidence_id',
                    'accept': 'Accept',
                    'finix_version': 'Finix-Version',
                },
                'location_map': {
                    'dispute_id': 'path',
                    'evidence_id': 'path',
                    'accept': 'header',
                    'finix_version': 'header',
                    'update_dispute_evidence': 'body',
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

    def post(
        self,
        dispute_id,
        **kwargs
    ):
        """Accept a Dispute  # noqa: E501

        You can accept a `Dispute` to prevent a long (and potentially expensive) process. When you accept a `Dispute`, you concede that the Dispute is not worth challenging or representing.  Related guides: [Accepting a Dispute](/guides/after-the-payment/disputes/accepting-disputes/)   # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to move forward and submit evidence.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            accept_dispute (AcceptDispute): [optional]
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
        return self._post_endpoint.call_with_http_info(**kwargs)

    def create_dispute_evidence(
        self,
        dispute_id,
        **kwargs
    ):
        """Upload Files as Dispute Evidence  # noqa: E501

        Upload a file as evidence for a `Dispute`.  - You can upload up to 8 files; the total size of the uploaded files combined cannot exceed 10 MB. - The allowed file formats include JPG, PNG, PDF, or TIFF. - Individual PNG and JPEG files can't exceed 50 KB; PDF and TIFF files can't exceed 1 MB.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.create_dispute_evidence(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to mange evidence for.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
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
        evidence_id,
        **kwargs
    ):
        """Download Dispute Evidence  # noqa: E501

        Download a file uploaded as `Dispute Evidence`.  **Note**: The file extension included in `output` must match the extension of the original uploaded file.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(dispute_id, evidence_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to download evidence from.
            evidence_id (str): ID of `evidence` to download.

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
        kwargs['dispute_id'] = \
            dispute_id
        kwargs['evidence_id'] = \
            evidence_id
        return self._get_endpoint.call_with_http_info(**kwargs)

    def get(
        self,
        dispute_id,
        **kwargs
    ):
        """Fetch a Dispute  # noqa: E501

        Retrieve the details of a previously created `Dispute`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.get(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute`.

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
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            limit (int): The numbers of items to return.. [optional]
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
        ret = self._list_dispute_evidence_by_dispute_id_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_dispute_evidence_by_dispute_id,  **kwargs)
        return fl

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
            accept (str): Body Header. [optional] if omitted the server will use the default value of 'application/hal+json'
            limit (int): The numbers of items to return.. [optional]
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]
            transfer_id (str): Filter by the ID of the `Transfer` that's being disputed. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]
            adjustment_transfer_id (str): Filter by the ID of the adjustment `Transfer`. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]
            amount (int): Filter by an amount equal to the given value.. [optional]
            amount_gte (int): Filter by an amount greater than or equal.. [optional]
            amount_gt (int): Filter by an amount greater than.. [optional]
            amount_lt (int): Filter by an amount less than.. [optional]
            state (str): Filter by the state of the `Dispute`.. [optional]
            response_state (str): Filter by the `response_state` of the `Dispute`.. [optional]
            respond_by_lte (str): Filter where `respond_by` is before the given date.. [optional]
            respond_by_gte (str): Filter where `respond_by` is after the given date.. [optional]
            instrument_bin (str): Filter by the Bank Identification Number (BIN). The BIN is the first 6 digits of the masked account number.. [optional]
            instrument_brand_type (str): Filter by the card brand used.. [optional]
            merchant_identity_id (str): Filter by the ID of the `Identity` used by the `Merchant`.. [optional]
            merchant_identity_name (str): Filter by the name used by the `Merchant`.. [optional]
            instrument_name (str): Filter by the name of the `Payment Instrument`.. [optional]
            instrument_type (str): Filter by `Payment Instrument` type.. [optional]
            merchant_id (str): Filter by the ID of the `Merchant`.. [optional]
            merchant_mid (str): Filter by the MID of the `Merchant`.. [optional]
            instrument_card_last4 (str): Filter by the last 4 digits of the card used.. [optional]
            instrument_card_type (str): Filter by the card type.. [optional]
            instrument_fingerprint (str): Filter by the fingerprint of the `Payment Instrument`.. [optional]
            before_cursor (str): Returns every `Dispute` created before the cursor value.. [optional]
            tags_key (str): Filter by the [`key` of a `Tag`](/api/overview/#section/Tags).. [optional]
            tags_value (str): Filter by the [value of a `Tag`](https://finix.com/docs/api/overview/#section/Tags).. [optional]
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
        ret = self._list_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list,  **kwargs)
        return fl

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
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            limit (int): The numbers of items to return.. [optional]
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
        ret = self._list_disputes_adjustments_endpoint.call_with_http_info(**kwargs)
        fl = FinixList(ret, self.list_disputes_adjustments,  **kwargs)
        return fl

    def post(
        self,
        dispute_id,
        **kwargs
    ):
        """Submit Dispute Evidence  # noqa: E501

        You can manually submit evidence to the issuing bank to manually move a dispute forward. Use the `/disputes/DISPUTE_ID/submit` endpoint to submit evidence. Making a POST request lets the issuing bank know the seller has completed submitting evidence and is prepared to move forward with the dispute.  Related guides: [Responding to Disputes](/guides/after-the-payment/disputes/responding-disputes/).  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.post(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to move forward and submit evidence.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of '2018-01-01'
            submit_dispute_evidence (SubmitDisputeEvidence): [optional]
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
        return self._post_endpoint.call_with_http_info(**kwargs)

    def update_dispute(
        self,
        dispute_id,
        **kwargs
    ):
        """Update a Dispute  # noqa: E501

        Update `tags` on `Disputes`.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dispute(dispute_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute`.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of '2018-01-01'
            update_dispute_evidence (UpdateDisputeEvidence): [optional]
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
        return self._update_dispute_endpoint.call_with_http_info(**kwargs)

    def update_dispute_evidence(
        self,
        dispute_id,
        evidence_id,
        **kwargs
    ):
        """Update Dispute Evidence  # noqa: E501

        Update tags on `Dispute` evidence.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.update_dispute_evidence(dispute_id, evidence_id, async_req=True)
        >>> result = thread.get()

        Args:
            dispute_id (str): ID of `Dispute` to fetch evidence for.
            evidence_id (str): ID of `evidence` to fetch.

        Keyword Args:
            accept (str): [optional] if omitted the server will use the default value of 'application/hal+json'
            finix_version (str): Specify the API version of your request. For more details, see [Versioning.](/guides/developers/versioning/). [optional] if omitted the server will use the default value of '2018-01-01'
            update_dispute_evidence (UpdateDisputeEvidence): [optional]
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
        return self._update_dispute_evidence_endpoint.call_with_http_info(**kwargs)

