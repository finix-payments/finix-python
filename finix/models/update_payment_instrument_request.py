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
    Address


class UpdatePaymentInstrumentRequest(ModelNormal):
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

    additional_properties_type = None

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
            'address': (Address,),  # noqa: E501
            'merchant': (str,),  # noqa: E501
            'verify_payment_card': (bool,),  # noqa: E501
            'tags': (object,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'attempt_bank_account_validation_check': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'address': 'address',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'verify_payment_card': 'verify_payment_card',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'name': 'name',  # noqa: E501
        'attempt_bank_account_validation_check': 'attempt_bank_account_validation_check',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """UpdatePaymentInstrumentRequest - a model defined in OpenAPI

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
            address (Address): [optional]  # noqa: E501
            merchant (str): The ID of the `Merchant` that the `Payment Instrument` will be created under.. [optional] if omitted the server will use the default value of 'false'  # noqa: E501
            verify_payment_card (bool): - Set to **true** to verify card details with the card issuer. - Must be set to **true** to update the CVV or security code of a card. - When set to **true**, `merchant` must also be included with your request.. [optional] if omitted the server will use the default value of False  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            enabled (bool): Details if the `Payment Instrument` resource is enabled. Default value is **true**; set to **false** to disable the `Payment Instrument`.. [optional]  # noqa: E501
            name (str): The name of the bank account or card owner. This value can get truncated to comply with processor requirements.. [optional] if omitted the server will use the default value of 'false'  # noqa: E501
            attempt_bank_account_validation_check (bool): Verify and validate the `Payment Instrument` to confirm it can be used for [ACH Direct Debits.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/) - Set to **True** to verify the `Payment Instrument` can be used for ACH payments.  - Only `Payment Instruments` created from bank accounts can be used for ACH payments.. [optional] if omitted the server will use the default value of False  # noqa: E501
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
        """UpdatePaymentInstrumentRequest - a model defined in OpenAPI

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
            address (Address): [optional]  # noqa: E501
            merchant (str): The ID of the `Merchant` that the `Payment Instrument` will be created under.. [optional] if omitted the server will use the default value of 'false'  # noqa: E501
            verify_payment_card (bool): - Set to **true** to verify card details with the card issuer. - Must be set to **true** to update the CVV or security code of a card. - When set to **true**, `merchant` must also be included with your request.. [optional] if omitted the server will use the default value of False  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            enabled (bool): Details if the `Payment Instrument` resource is enabled. Default value is **true**; set to **false** to disable the `Payment Instrument`.. [optional]  # noqa: E501
            name (str): The name of the bank account or card owner. This value can get truncated to comply with processor requirements.. [optional] if omitted the server will use the default value of 'false'  # noqa: E501
            attempt_bank_account_validation_check (bool): Verify and validate the `Payment Instrument` to confirm it can be used for [ACH Direct Debits.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/) - Set to **True** to verify the `Payment Instrument` can be used for ACH payments.  - Only `Payment Instruments` created from bank accounts can be used for ACH payments.. [optional] if omitted the server will use the default value of False  # noqa: E501
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
