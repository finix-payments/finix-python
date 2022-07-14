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
    from finix.model.additional_purchase_data import AdditionalPurchaseData
    from finix.model.card_present_instrument_form import CardPresentInstrumentForm
    from finix.model.configuration_details import ConfigurationDetails
    from finix.model.create_authorization_request3d_secure_authentication import CreateAuthorizationRequest3dSecureAuthentication
    from finix.model.currency import Currency
    from finix.model.tags import Tags
    globals()['AdditionalPurchaseData'] = AdditionalPurchaseData
    globals()['CardPresentInstrumentForm'] = CardPresentInstrumentForm
    globals()['ConfigurationDetails'] = ConfigurationDetails
    globals()['CreateAuthorizationRequest3dSecureAuthentication'] = CreateAuthorizationRequest3dSecureAuthentication
    globals()['Currency'] = Currency
    globals()['Tags'] = Tags


class CreateTransferRequest(ModelNormal):
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
        ('gateway',): {
            'None': None,
            'CLOUD_V1': "TRIPOS_CLOUD_V1",
            'MOBILE_V1': "TRIPOS_MOBILE_V1",
        },
        ('input_method',): {
            'None': None,
            'UNKNOWN': "UNKNOWN",
            'SWIPED': "SWIPED",
            'MANUAL_KEY_ENTRY': "MANUAL_KEY_ENTRY",
            'CONTACTLESS_MSD': "CONTACTLESS_MSD",
            'CONTACTLESS_EMV': "CONTACTLESS_EMV",
            'SWIPED_FALLBACK': "SWIPED_FALLBACK",
            'KEYED_FALLBACK': "KEYED_FALLBACK",
            'CONTACTLESS': "CONTACTLESS",
            'DIGITAL_WALLET': "DIGITAL_WALLET",
            'CHIP_ENTRY': "CHIP_ENTRY",
        },
        ('operation_key',): {
            'None': None,
            'PUSH_TO_CARD': "PUSH_TO_CARD",
            'PULL_FROM_CARD': "PULL_FROM_CARD",
            'CARD_PRESENT_DEBIT': "CARD_PRESENT_DEBIT",
            'CARD_PRESENT_UNREFERENCED_REFUND': "CARD_PRESENT_UNREFERENCED_REFUND",
            'SALE': "SALE",
            'UNREFERENCED_REFUND': "UNREFERENCED_REFUND",
            'MERCHANT_CREDIT_ADJUSTMENT': "MERCHANT_CREDIT_ADJUSTMENT",
            'MERCHANT_DEBIT_ADJUSTMENT': "MERCHANT_DEBIT_ADJUSTMENT",
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
            'adjustment_request': (bool, none_type,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'config_override': ({str: (str,)}, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'destination': (str, none_type,),  # noqa: E501
            'device': (str, none_type,),  # noqa: E501
            'device_configuration': (ConfigurationDetails,),  # noqa: E501
            'fee': (int,),  # noqa: E501
            'gateway': (str, none_type,),  # noqa: E501
            '_3d_secure_authentication': (CreateAuthorizationRequest3dSecureAuthentication,),  # noqa: E501
            'idempotency_id': (str, none_type,),  # noqa: E501
            'input_method': (str, none_type,),  # noqa: E501
            'merchant': (str, none_type,),  # noqa: E501
            'merchant_identity': (str, none_type,),  # noqa: E501
            'operation_key': (str, none_type,),  # noqa: E501
            'payment_instrument': (CardPresentInstrumentForm,),  # noqa: E501
            'processor': (str,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'statement_descriptor': (str, none_type,),  # noqa: E501
            'fraud_session_id': (str,),  # noqa: E501
            'additional_purchase_data': (AdditionalPurchaseData,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tags': 'tags',  # noqa: E501
        'adjustment_request': 'adjustment_request',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'config_override': 'config_override',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'destination': 'destination',  # noqa: E501
        'device': 'device',  # noqa: E501
        'device_configuration': 'device_configuration',  # noqa: E501
        'fee': 'fee',  # noqa: E501
        'gateway': 'gateway',  # noqa: E501
        '_3d_secure_authentication': '3d_secure_authentication',  # noqa: E501
        'idempotency_id': 'idempotency_id',  # noqa: E501
        'input_method': 'input_method',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'merchant_identity': 'merchant_identity',  # noqa: E501
        'operation_key': 'operation_key',  # noqa: E501
        'payment_instrument': 'payment_instrument',  # noqa: E501
        'processor': 'processor',  # noqa: E501
        'source': 'source',  # noqa: E501
        'statement_descriptor': 'statement_descriptor',  # noqa: E501
        'fraud_session_id': 'fraud_session_id',  # noqa: E501
        'additional_purchase_data': 'additional_purchase_data',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CreateTransferRequest - a model defined in OpenAPI

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
            adjustment_request (bool, none_type): Details if the `transfer` was created to adjust funds.. [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            config_override ({str: (str,)}, none_type): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): ID of the `Payment Instrument` where funds will be sent.. [optional]  # noqa: E501
            device (str, none_type): The ID of the activated device.. [optional]  # noqa: E501
            device_configuration (ConfigurationDetails): [optional]  # noqa: E501
            fee (int): The amount of the `Transfer` you'd like to collect as your fee in cents. Defaults to zero (must be less than or equal to the `amount`).. [optional]  # noqa: E501
            gateway (str, none_type): Name of the gateway that processed this `transfer`. (Finix Core only).. [optional]  # noqa: E501
            _3d_secure_authentication (CreateAuthorizationRequest3dSecureAuthentication): [optional]  # noqa: E501
            idempotency_id (str, none_type): A randomly generated value that'll be associated with the request.. [optional]  # noqa: E501
            input_method (str, none_type): Details how the card details were entered.. [optional]  # noqa: E501
            merchant (str, none_type): ID of the `Merchant` the `Transfer` was created under.. [optional]  # noqa: E501
            merchant_identity (str, none_type): ID of the `Identity` the `Merchant` was created under and the `Transfer` was submitted with.. [optional]  # noqa: E501
            operation_key (str, none_type): Details the operation that'll be performed in the transaction.. [optional]  # noqa: E501
            payment_instrument (CardPresentInstrumentForm): [optional]  # noqa: E501
            processor (str): Name of the transaction processor.. [optional]  # noqa: E501
            source (str): ID of the `Payment Instrument` where funds get debited.. [optional]  # noqa: E501
            statement_descriptor (str, none_type): The description of the transaction that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            fraud_session_id (str): The `fraud_session_session` ID you want to review for fraud. For more info, see [Fraud Detection](/docs/guides/payments/fraud-detection/).. [optional]  # noqa: E501
            additional_purchase_data (AdditionalPurchaseData): [optional]  # noqa: E501
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
        """CreateTransferRequest - a model defined in OpenAPI

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
            adjustment_request (bool, none_type): Details if the `transfer` was created to adjust funds.. [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            config_override ({str: (str,)}, none_type): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): ID of the `Payment Instrument` where funds will be sent.. [optional]  # noqa: E501
            device (str, none_type): The ID of the activated device.. [optional]  # noqa: E501
            device_configuration (ConfigurationDetails): [optional]  # noqa: E501
            fee (int): The amount of the `Transfer` you'd like to collect as your fee in cents. Defaults to zero (must be less than or equal to the `amount`).. [optional]  # noqa: E501
            gateway (str, none_type): Name of the gateway that processed this `transfer`. (Finix Core only).. [optional]  # noqa: E501
            _3d_secure_authentication (CreateAuthorizationRequest3dSecureAuthentication): [optional]  # noqa: E501
            idempotency_id (str, none_type): A randomly generated value that'll be associated with the request.. [optional]  # noqa: E501
            input_method (str, none_type): Details how the card details were entered.. [optional]  # noqa: E501
            merchant (str, none_type): ID of the `Merchant` the `Transfer` was created under.. [optional]  # noqa: E501
            merchant_identity (str, none_type): ID of the `Identity` the `Merchant` was created under and the `Transfer` was submitted with.. [optional]  # noqa: E501
            operation_key (str, none_type): Details the operation that'll be performed in the transaction.. [optional]  # noqa: E501
            payment_instrument (CardPresentInstrumentForm): [optional]  # noqa: E501
            processor (str): Name of the transaction processor.. [optional]  # noqa: E501
            source (str): ID of the `Payment Instrument` where funds get debited.. [optional]  # noqa: E501
            statement_descriptor (str, none_type): The description of the transaction that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            fraud_session_id (str): The `fraud_session_session` ID you want to review for fraud. For more info, see [Fraud Detection](/docs/guides/payments/fraud-detection/).. [optional]  # noqa: E501
            additional_purchase_data (AdditionalPurchaseData): [optional]  # noqa: E501
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
