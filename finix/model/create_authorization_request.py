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
    from finix.model.additional_buyer_charges import AdditionalBuyerCharges
    from finix.model.additional_purchase_data import AdditionalPurchaseData
    from finix.model.create_authorization_request3d_secure_authentication import CreateAuthorizationRequest3dSecureAuthentication
    from finix.model.currency import Currency
    from finix.model.l3_additional_purchase_data import L3AdditionalPurchaseData
    from finix.model.operation_key import OperationKey
    globals()['AdditionalBuyerCharges'] = AdditionalBuyerCharges
    globals()['AdditionalPurchaseData'] = AdditionalPurchaseData
    globals()['CreateAuthorizationRequest3dSecureAuthentication'] = CreateAuthorizationRequest3dSecureAuthentication
    globals()['Currency'] = Currency
    globals()['L3AdditionalPurchaseData'] = L3AdditionalPurchaseData
    globals()['OperationKey'] = OperationKey


class CreateAuthorizationRequest(ModelNormal):
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
            'additional_buyer_charges': (AdditionalBuyerCharges,),  # noqa: E501
            'additional_purchase_data': (AdditionalPurchaseData,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'device': (str,),  # noqa: E501
            'fraud_session_id': (str,),  # noqa: E501
            'hsa_fsa_payment': (bool, none_type,),  # noqa: E501
            'idempotency_id': (str, none_type,),  # noqa: E501
            'merchant': (str,),  # noqa: E501
            'operation_key': (OperationKey,),  # noqa: E501
            'security_code': (str,),  # noqa: E501
            'source': (str,),  # noqa: E501
            'tags': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            '_3d_secure_authentication': (CreateAuthorizationRequest3dSecureAuthentication,),  # noqa: E501
            'additional_purchase_data_': (L3AdditionalPurchaseData,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'additional_buyer_charges': 'additional_buyer_charges',  # noqa: E501
        'additional_purchase_data': 'additional_purchase_data',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'device': 'device',  # noqa: E501
        'fraud_session_id': 'fraud_session_id',  # noqa: E501
        'hsa_fsa_payment': 'hsa_fsa_payment',  # noqa: E501
        'idempotency_id': 'idempotency_id',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'operation_key': 'operation_key',  # noqa: E501
        'security_code': 'security_code',  # noqa: E501
        'source': 'source',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        '_3d_secure_authentication': '3d_secure_authentication',  # noqa: E501
        'additional_purchase_data_': 'additional_purchase_data ',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CreateAuthorizationRequest - a model defined in OpenAPI

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
            additional_buyer_charges (AdditionalBuyerCharges): [optional]  # noqa: E501
            additional_purchase_data (AdditionalPurchaseData): [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            device (str): The ID of the `Device` that the `Authorization` was created under.. [optional]  # noqa: E501
            fraud_session_id (str): The `fraud_session_session` ID you want to review for fraud. For more info, see [Fraud Detection](/guides/payments/fraud-detection/).. [optional]  # noqa: E501
            hsa_fsa_payment (bool, none_type): Set to to **true** to process a payment using a `Payment Instrument` [created from a health savings account (HSA) or flexible spending account (FSA)](/guides/making-a-payment/hsa-fsa/).. [optional]  # noqa: E501
            idempotency_id (str, none_type): A randomly generated value that gets tied with the request.. [optional]  # noqa: E501
            merchant (str): The ID of the `Merchant` that the `Authorization` was created under.. [optional]  # noqa: E501
            operation_key (OperationKey): [optional]  # noqa: E501
            security_code (str): The 3-4 digit security code for the card (i.e. CVV code). Include the CVV code of the card to include [Card Verification Checks](/guides/payments/making-a-payment/card-verification-checks/) with the created `Authorization`.. [optional]  # noqa: E501
            source (str): The ID of the `Payment Instrument` that will be debited and performing the `Authorization`.. [optional]  # noqa: E501
            tags ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            _3d_secure_authentication (CreateAuthorizationRequest3dSecureAuthentication): [optional]  # noqa: E501
            additional_purchase_data_ (L3AdditionalPurchaseData): [optional]  # noqa: E501
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
        """CreateAuthorizationRequest - a model defined in OpenAPI

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
            additional_buyer_charges (AdditionalBuyerCharges): [optional]  # noqa: E501
            additional_purchase_data (AdditionalPurchaseData): [optional]  # noqa: E501
            amount (int): The total amount that will be debited in cents (e.g. 100 cents to debit $1.00).. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            device (str): The ID of the `Device` that the `Authorization` was created under.. [optional]  # noqa: E501
            fraud_session_id (str): The `fraud_session_session` ID you want to review for fraud. For more info, see [Fraud Detection](/guides/payments/fraud-detection/).. [optional]  # noqa: E501
            hsa_fsa_payment (bool, none_type): Set to to **true** to process a payment using a `Payment Instrument` [created from a health savings account (HSA) or flexible spending account (FSA)](/guides/making-a-payment/hsa-fsa/).. [optional]  # noqa: E501
            idempotency_id (str, none_type): A randomly generated value that gets tied with the request.. [optional]  # noqa: E501
            merchant (str): The ID of the `Merchant` that the `Authorization` was created under.. [optional]  # noqa: E501
            operation_key (OperationKey): [optional]  # noqa: E501
            security_code (str): The 3-4 digit security code for the card (i.e. CVV code). Include the CVV code of the card to include [Card Verification Checks](/guides/payments/making-a-payment/card-verification-checks/) with the created `Authorization`.. [optional]  # noqa: E501
            source (str): The ID of the `Payment Instrument` that will be debited and performing the `Authorization`.. [optional]  # noqa: E501
            tags ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            _3d_secure_authentication (CreateAuthorizationRequest3dSecureAuthentication): [optional]  # noqa: E501
            additional_purchase_data_ (L3AdditionalPurchaseData): [optional]  # noqa: E501
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
