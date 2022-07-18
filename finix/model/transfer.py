"""
    Finix API

    The version of the OpenAPI document: 2022-02-01
    Contact: support@finixpayments.com
"""


import re  # noqa: F401
import sys  # noqa: F401

from finix.model_utils import (  # noqa: F401
    ApiTypeError,
    ModelComposed,
    ModelNormal,
    ModelSimple,
    cached_property,
    change_keys_js_to_python,
    convert_js_args_to_python_args,
    date,
    datetime,
    file_type,
    none_type,
    validate_get_composed_info,
    OpenApiModel
)
from finix.exceptions import ApiAttributeError


def lazy_import():
    from finix.model.card_present_details import CardPresentDetails
    from finix.model.currency import Currency
    from finix.model.fee_type import FeeType
    from finix.model.messages import Messages
    from finix.model.tags import Tags
    globals()['CardPresentDetails'] = CardPresentDetails
    globals()['Currency'] = Currency
    globals()['FeeType'] = FeeType
    globals()['Messages'] = Messages
    globals()['Tags'] = Tags


class Transfer(ModelNormal):
    """

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      attribute_map (dict): The key is attribute name
          and the value is json key in definition.
      discriminator_value_class_map (dict): A dict to go from the discriminator
          variable value to the discriminator class name.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('type',): {
            'DEBIT': "DEBIT",
            'CREDIT': "CREDIT",
            'REVERSAL': "REVERSAL",
            'FEE': "FEE",
            'ADJUSTMENT': "ADJUSTMENT",
            'DISPUTE': "DISPUTE",
            'RESERVE': "RESERVE",
            'SETTLEMENT': "SETTLEMENT",
            'UNKNOWN': "UNKNOWN",
        },
        ('state',): {
            'CANCELED': "CANCELED",
            'PENDING': "PENDING",
            'FAILED': "FAILED",
            'SUCCEEDED': "SUCCEEDED",
            'UNKNOWN': "UNKNOWN",
        },
        ('subtype',): {
            'API': "API",
            'APPLICATION_FEE': "APPLICATION_FEE",
            'DISPUTE': "DISPUTE",
            'MERCHANT_CREDIT': "MERCHANT_CREDIT",
            'MERCHANT_CREDIT_ADJUSTMENT': "MERCHANT_CREDIT_ADJUSTMENT",
            'MERCHANT_DEBIT': "MERCHANT_DEBIT",
            'MERCHANT_DEBIT_ADJUSTMENT': "MERCHANT_DEBIT_ADJUSTMENT",
            'PLATFORM_CREDIT': "PLATFORM_CREDIT",
            'PLATFORM_CREDIT_ADJUSTMENT': "PLATFORM_CREDIT_ADJUSTMENT",
            'PLATFORM_DEBIT': "PLATFORM_DEBIT",
            'PLATFORM_DEBIT_ADJUSTMENT': "PLATFORM_DEBIT_ADJUSTMENT",
            'PLATFORM_FEE': "PLATFORM_FEE",
            'SETTLEMENT_MERCHANT': "SETTLEMENT_MERCHANT",
            'SETTLEMENT_NOOP': "SETTLEMENT_NOOP",
            'SETTLEMENT_PARTNER': "SETTLEMENT_PARTNER",
            'SETTLEMENT_PLATFORM': "SETTLEMENT_PLATFORM",
            'SPLIT_PAYOUT': "SPLIT_PAYOUT",
            'SPLIT_PAYOUT_ADJUSTMENT': "SPLIT_PAYOUT_ADJUSTMENT",
            'SYSTEM': "SYSTEM",
        },
    }

    validations = {
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = False

    @cached_property
    def openapi_types():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded

        Returns
            openapi_types (dict): The key is attribute name
                and the value is attribute type.
        """
        lazy_import()
        return {
            'tags': (Tags,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'id': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'application': (str, none_type,),  # noqa: E501
            'card_present_details': (CardPresentDetails,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'destination': (str, none_type,),  # noqa: E501
            'device': (str, none_type,),  # noqa: E501
            'fee': (int,),  # noqa: E501
            'fee_type': (FeeType,),  # noqa: E501
            'idempotency_id': (str, none_type,),  # noqa: E501
            'identity': (str,),  # noqa: E501
            'merchant_identity': (str, none_type,),  # noqa: E501
            'messages': (Messages,),  # noqa: E501
            'raw': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'ready_to_settle_at': (datetime, none_type,),  # noqa: E501
            'source': (str, none_type,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'statement_descriptor': (str, none_type,),  # noqa: E501
            'subtype': (str,),  # noqa: E501
            'trace_id': (str, none_type,),  # noqa: E501
            'externally_funded': (str,),  # noqa: E501
            'failure_code': (str, none_type,),  # noqa: E501
            'failure_message': (str, none_type,),  # noqa: E501
            'links': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)},),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tags': 'tags',  # noqa: E501
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'application': 'application',  # noqa: E501
        'card_present_details': 'card_present_details',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'destination': 'destination',  # noqa: E501
        'device': 'device',  # noqa: E501
        'fee': 'fee',  # noqa: E501
        'fee_type': 'fee_type',  # noqa: E501
        'idempotency_id': 'idempotency_id',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'merchant_identity': 'merchant_identity',  # noqa: E501
        'messages': 'messages',  # noqa: E501
        'raw': 'raw',  # noqa: E501
        'ready_to_settle_at': 'ready_to_settle_at',  # noqa: E501
        'source': 'source',  # noqa: E501
        'state': 'state',  # noqa: E501
        'statement_descriptor': 'statement_descriptor',  # noqa: E501
        'subtype': 'subtype',  # noqa: E501
        'trace_id': 'trace_id',  # noqa: E501
        'externally_funded': 'externally_funded',  # noqa: E501
        'failure_code': 'failure_code',  # noqa: E501
        'failure_message': 'failure_message',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Transfer - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            tags (Tags): [optional]  # noqa: E501
            type (str): Type of `Transfer`.. [optional]  # noqa: E501
            id (str): The ID of the `Transfer` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            application (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            card_present_details (CardPresentDetails): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): The ID of the destination.. [optional]  # noqa: E501
            device (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            fee (int): The amount of the `Transfer` you'd like to collect as your fee in cents. Defaults to zero (must be less than or equal to the `amount`).. [optional]  # noqa: E501
            fee_type (FeeType): [optional]  # noqa: E501
            idempotency_id (str, none_type): ID to [idempotently](#section/Idempotency-Requests) identifty the transfer.. [optional]  # noqa: E501
            identity (str): The ID of the identity.. [optional]  # noqa: E501
            merchant_identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            messages (Messages): [optional]  # noqa: E501
            raw ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Raw response from the processor. [optional]  # noqa: E501
            ready_to_settle_at (datetime, none_type): Timestamp of when the `Transfer` is ready to be settled at.. [optional]  # noqa: E501
            source (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            state (str): The stauts of the `Transfer`.. [optional]  # noqa: E501
            statement_descriptor (str, none_type): The description of the merchant that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            subtype (str): Additional information describing the `payment_type`.. [optional]  # noqa: E501
            trace_id (str, none_type): Trace ID of the `Transfer`. The processor sends back the `trace_id` so you can track the `transfer` end-to-end.. [optional]  # noqa: E501
            externally_funded (str): Details if the Transfer will be settled externally by card processors.. [optional]  # noqa: E501
            failure_code (str, none_type): The code of the failure so the decline can be handled programmatically. For more info on how to handle the failure, see [Failure Codes](/docs/guides/developers/errors/#failure-codes).. [optional]  # noqa: E501
            failure_message (str, none_type): A human-readable description of why the transaction was declined. This will also include a suggestion on how to complete the payment.. [optional]  # noqa: E501
            links ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): For your convenience, every response includes several URLs which link to resources relevant to the request. You can use these `_links` to make your follow-up requests and quickly access relevant IDs.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
        return self

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):  # noqa: E501
        """Transfer - a model defined in OpenAPI

        Keyword Args:
            _check_type (bool): if True, values for parameters in openapi_types
                                will be type checked and a TypeError will be
                                raised if the wrong type is input.
                                Defaults to True
            _path_to_item (tuple/list): This is a list of keys or values to
                                drill down to the model in received_data
                                when deserializing a response
            _spec_property_naming (bool): True if the variable names in the input data
                                are serialized names, as specified in the OpenAPI document.
                                False if the variable names in the input data
                                are pythonic names, e.g. snake case (default)
            _configuration (Configuration): the instance to use when
                                deserializing a file_type parameter.
                                If passed, type conversion is attempted
                                If omitted no type conversion is done.
            _visited_composed_classes (tuple): This stores a tuple of
                                classes that we have traveled through so that
                                if we see that class again we will not use its
                                discriminator again.
                                When traveling through a discriminator, the
                                composed schema that is
                                is traveled through is added to this set.
                                For example if Animal has a discriminator
                                petType and we pass in "Dog", and the class Dog
                                allOf includes Animal, we move through Animal
                                once using the discriminator, and pick Dog.
                                Then in Dog, we will make an instance of the
                                Animal class but this time we won't travel
                                through its discriminator because we passed in
                                _visited_composed_classes = (Animal,)
            tags (Tags): [optional]  # noqa: E501
            type (str): Type of `Transfer`.. [optional]  # noqa: E501
            id (str): The ID of the `Transfer` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            application (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            card_present_details (CardPresentDetails): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): The ID of the destination.. [optional]  # noqa: E501
            device (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            fee (int): The amount of the `Transfer` you'd like to collect as your fee in cents. Defaults to zero (must be less than or equal to the `amount`).. [optional]  # noqa: E501
            fee_type (FeeType): [optional]  # noqa: E501
            idempotency_id (str, none_type): ID to [idempotently](#section/Idempotency-Requests) identifty the transfer.. [optional]  # noqa: E501
            identity (str): The ID of the identity.. [optional]  # noqa: E501
            merchant_identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            messages (Messages): [optional]  # noqa: E501
            raw ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Raw response from the processor. [optional]  # noqa: E501
            ready_to_settle_at (datetime, none_type): Timestamp of when the `Transfer` is ready to be settled at.. [optional]  # noqa: E501
            source (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            state (str): The stauts of the `Transfer`.. [optional]  # noqa: E501
            statement_descriptor (str, none_type): The description of the merchant that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            subtype (str): Additional information describing the `payment_type`.. [optional]  # noqa: E501
            trace_id (str, none_type): Trace ID of the `Transfer`. The processor sends back the `trace_id` so you can track the `transfer` end-to-end.. [optional]  # noqa: E501
            externally_funded (str): Details if the Transfer will be settled externally by card processors.. [optional]  # noqa: E501
            failure_code (str, none_type): The code of the failure so the decline can be handled programmatically. For more info on how to handle the failure, see [Failure Codes](/docs/guides/developers/errors/#failure-codes).. [optional]  # noqa: E501
            failure_message (str, none_type): A human-readable description of why the transaction was declined. This will also include a suggestion on how to complete the payment.. [optional]  # noqa: E501
            links ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}): For your convenience, every response includes several URLs which link to resources relevant to the request. You can use these `_links` to make your follow-up requests and quickly access relevant IDs.. [optional]  # noqa: E501
        """

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
        _path_to_item = kwargs.pop('_path_to_item', ())
        _configuration = kwargs.pop('_configuration', None)
        _visited_composed_classes = kwargs.pop('_visited_composed_classes', ())

        if args:
            raise ApiTypeError(
                "Invalid positional arguments=%s passed to %s. Remove those invalid positional arguments." % (
                    args,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        self._data_store = {}
        self._check_type = _check_type
        self._spec_property_naming = _spec_property_naming
        self._path_to_item = _path_to_item
        self._configuration = _configuration
        self._visited_composed_classes = _visited_composed_classes + (self.__class__,)

        for var_name, var_value in kwargs.items():
            if var_name not in self.attribute_map and \
                        self._configuration is not None and \
                        self._configuration.discard_unknown_keys and \
                        self.additional_properties_type is None:
                # discard variable.
                continue
            setattr(self, var_name, var_value)
            if var_name in self.read_only_vars:
                raise ApiAttributeError(f"`{var_name}` is a read-only attribute. Use `from_openapi_data` to instantiate "
                                     f"class with read only attributes.")
