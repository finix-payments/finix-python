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
    from finix.model.configuration_details_cashback_options import ConfigurationDetailsCashbackOptions
    from finix.model.configuration_details_tip_options import ConfigurationDetailsTipOptions
    globals()['ConfigurationDetailsCashbackOptions'] = ConfigurationDetailsCashbackOptions
    globals()['ConfigurationDetailsTipOptions'] = ConfigurationDetailsTipOptions


class ConfigurationDetails(ModelNormal):
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
            'allow_debit': (bool,),  # noqa: E501
            'allow_partial_approvals': (bool,),  # noqa: E501
            'bypass_device_on_capture': (bool,),  # noqa: E501
            'cashback_options': (ConfigurationDetailsCashbackOptions,),  # noqa: E501
            'check_for_duplicate_transactions': (bool,),  # noqa: E501
            'is_cash_back_allowed': (bool,),  # noqa: E501
            'is_gift_supported': (str,),  # noqa: E501
            'is_manual_entry_allowed': (bool,),  # noqa: E501
            'market_code': (str,),  # noqa: E501
            'prompt_amount_confirmation': (bool,),  # noqa: E501
            'prompt_manual_entry': (bool,),  # noqa: E501
            'prompt_signature': (str,),  # noqa: E501
            'signature_threshold_amount': (int,),  # noqa: E501
            'tip_options': (ConfigurationDetailsTipOptions,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'allow_debit': 'allow_debit',  # noqa: E501
        'allow_partial_approvals': 'allow_partial_approvals',  # noqa: E501
        'bypass_device_on_capture': 'bypass_device_on_capture',  # noqa: E501
        'cashback_options': 'cashback_options',  # noqa: E501
        'check_for_duplicate_transactions': 'check_for_duplicate_transactions',  # noqa: E501
        'is_cash_back_allowed': 'is_cash_back_allowed',  # noqa: E501
        'is_gift_supported': 'is_gift_supported',  # noqa: E501
        'is_manual_entry_allowed': 'is_manual_entry_allowed',  # noqa: E501
        'market_code': 'market_code',  # noqa: E501
        'prompt_amount_confirmation': 'prompt_amount_confirmation',  # noqa: E501
        'prompt_manual_entry': 'prompt_manual_entry',  # noqa: E501
        'prompt_signature': 'prompt_signature',  # noqa: E501
        'signature_threshold_amount': 'signature_threshold_amount',  # noqa: E501
        'tip_options': 'tip_options',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ConfigurationDetails - a model defined in OpenAPI

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
            allow_debit (bool): Allow transaction to be processed on Debit rails. If `false`, Debit card transactions will be processed on Credit rails.. [optional]  # noqa: E501
            allow_partial_approvals (bool): Determines if a transaction can be partially approved (Usually **null**).. [optional]  # noqa: E501
            bypass_device_on_capture (bool): Sets whether or not the device will be used to capture transactions. This field must be set to true (defaults to false).. [optional]  # noqa: E501
            cashback_options (ConfigurationDetailsCashbackOptions): [optional]  # noqa: E501
            check_for_duplicate_transactions (bool): Sets whether the device will check for duplicate transactions.. [optional]  # noqa: E501
            is_cash_back_allowed (bool): Sets whether the device will allow cash back.. [optional]  # noqa: E501
            is_gift_supported (str): Sets whether the device will allow gifting funds.. [optional]  # noqa: E501
            is_manual_entry_allowed (bool): Sets whether the device will process payment details entered manually.. [optional]  # noqa: E501
            market_code (str): Used by the processor to handle the `transfer`. Usually **null**.. [optional]  # noqa: E501
            prompt_amount_confirmation (bool): Sets if the card holder needs to confirm the amount they will pay (defaults to **true**).. [optional]  # noqa: E501
            prompt_manual_entry (bool): Sets if the device defaults to manual entry as the default card input method. (defaults to **false**).. [optional]  # noqa: E501
            prompt_signature (str): Sets if the device will prompt the card holder for a signature by default. Available values include:<ul><li><strong>ALWAYS</strong><li><strong>NEVER</strong><li><strong>AMOUNT</strong>: Used in conjunction with `signature_threshold_amount` so when the threshold is reached the signature form appears on the device.. [optional]  # noqa: E501
            signature_threshold_amount (int): The threshold to prompt a signature when `prompt_signature` is set to **AMOUNT** (defaults to 0).. [optional]  # noqa: E501
            tip_options (ConfigurationDetailsTipOptions): [optional]  # noqa: E501
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
        """ConfigurationDetails - a model defined in OpenAPI

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
            allow_debit (bool): Allow transaction to be processed on Debit rails. If `false`, Debit card transactions will be processed on Credit rails.. [optional]  # noqa: E501
            allow_partial_approvals (bool): Determines if a transaction can be partially approved (Usually **null**).. [optional]  # noqa: E501
            bypass_device_on_capture (bool): Sets whether or not the device will be used to capture transactions. This field must be set to true (defaults to false).. [optional]  # noqa: E501
            cashback_options (ConfigurationDetailsCashbackOptions): [optional]  # noqa: E501
            check_for_duplicate_transactions (bool): Sets whether the device will check for duplicate transactions.. [optional]  # noqa: E501
            is_cash_back_allowed (bool): Sets whether the device will allow cash back.. [optional]  # noqa: E501
            is_gift_supported (str): Sets whether the device will allow gifting funds.. [optional]  # noqa: E501
            is_manual_entry_allowed (bool): Sets whether the device will process payment details entered manually.. [optional]  # noqa: E501
            market_code (str): Used by the processor to handle the `transfer`. Usually **null**.. [optional]  # noqa: E501
            prompt_amount_confirmation (bool): Sets if the card holder needs to confirm the amount they will pay (defaults to **true**).. [optional]  # noqa: E501
            prompt_manual_entry (bool): Sets if the device defaults to manual entry as the default card input method. (defaults to **false**).. [optional]  # noqa: E501
            prompt_signature (str): Sets if the device will prompt the card holder for a signature by default. Available values include:<ul><li><strong>ALWAYS</strong><li><strong>NEVER</strong><li><strong>AMOUNT</strong>: Used in conjunction with `signature_threshold_amount` so when the threshold is reached the signature form appears on the device.. [optional]  # noqa: E501
            signature_threshold_amount (int): The threshold to prompt a signature when `prompt_signature` is set to **AMOUNT** (defaults to 0).. [optional]  # noqa: E501
            tip_options (ConfigurationDetailsTipOptions): [optional]  # noqa: E501
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
