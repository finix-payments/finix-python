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



class OnboardingFormOnboardingDataPaymentInstruments(ModelNormal):
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
        ('attempt_bank_account_validation_check',): {
            '&#39;CHECKING&#39;': 'CHECKING',
            '&#39;SAVINGS&#39;': 'SAVINGS',
            '&#39;PERSONAL_CHECKING&#39;': 'PERSONAL_CHECKING',
            '&#39;PERSONAL_SAVINGS&#39;': 'PERSONAL_SAVINGS',
            '&#39;BUSINESS_CHECKING&#39;': 'BUSINESS_CHECKING',
            '&#39;BUSINESS_SAVINGS&#39;': 'BUSINESS_SAVINGS',
            '&#39;CORPORATE&#39;': 'CORPORATE',
            '&#39;CORP_SAVINGS&#39;': 'CORP_SAVINGS',
        },
        ('type',): {
            '&#39;BANK_ACCOUNT&#39;': 'BANK_ACCOUNT',
        },
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
        return {
            'account_number': (str,),  # noqa: E501
            'acount_type': (str,),  # noqa: E501
            'attempt_bank_account_validation_check': (str,),  # noqa: E501
            'bank_code': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'type': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'account_number': 'account_number',  # noqa: E501
        'acount_type': 'acount_type',  # noqa: E501
        'attempt_bank_account_validation_check': 'attempt_bank_account_validation_check',  # noqa: E501
        'bank_code': 'bank_code',  # noqa: E501
        'name': 'name',  # noqa: E501
        'type': 'type',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """OnboardingFormOnboardingDataPaymentInstruments - a model defined in OpenAPI

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
            account_number (str): The bank account number (no dashes in between numbers).. [optional]  # noqa: E501
            acount_type (str): The type of bank account. Use the following respective enum when creating a `Payment Instrument` for:<ul><li><strong>CHECKING: </strong>The checking account of your buyer.</li><li><strong>SAVINGS: </strong>The savings account of your buyer.</li><li><strong>CORPORATE: </strong>A corporate checking account.</li><li><strong>CORP_SAVINGS: </strong>A corporate savings account.</li><li><strong>BUSINESS_CHECKING: </strong>A checking account primarily owned by a business.</li><li><strong>BUSINESS_SAVINGS: </strong>A savings account primarily owned by a business</li><li><strong>PERSONAL_CHECKING: </strong>Seller's using their personal checking account.</li><li><strong>PERSONAL_SAVINGS: </strong>Seller's using their personal savings account.</li></ul>. [optional]  # noqa: E501
            attempt_bank_account_validation_check (str): [optional]  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            name (str): The name of the bank account owner.. [optional]  # noqa: E501
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
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
        """OnboardingFormOnboardingDataPaymentInstruments - a model defined in OpenAPI

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
            account_number (str): The bank account number (no dashes in between numbers).. [optional]  # noqa: E501
            acount_type (str): The type of bank account. Use the following respective enum when creating a `Payment Instrument` for:<ul><li><strong>CHECKING: </strong>The checking account of your buyer.</li><li><strong>SAVINGS: </strong>The savings account of your buyer.</li><li><strong>CORPORATE: </strong>A corporate checking account.</li><li><strong>CORP_SAVINGS: </strong>A corporate savings account.</li><li><strong>BUSINESS_CHECKING: </strong>A checking account primarily owned by a business.</li><li><strong>BUSINESS_SAVINGS: </strong>A savings account primarily owned by a business</li><li><strong>PERSONAL_CHECKING: </strong>Seller's using their personal checking account.</li><li><strong>PERSONAL_SAVINGS: </strong>Seller's using their personal savings account.</li></ul>. [optional]  # noqa: E501
            attempt_bank_account_validation_check (str): [optional]  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            name (str): The name of the bank account owner.. [optional]  # noqa: E501
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
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
