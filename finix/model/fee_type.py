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



class FeeType(ModelSimple):
    """

    Attributes:
      allowed_values (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          with a capitalized key describing the allowed value and an allowed
          value. These dicts store the allowed enum values.
      validations (dict): The key is the tuple path to the attribute
          and the for var_name this is (var_name,). The value is a dict
          that stores validations for max_length, min_length, max_items,
          min_items, exclusive_maximum, inclusive_maximum, exclusive_minimum,
          inclusive_minimum, and regex.
      additional_properties_type (tuple): A tuple of classes accepted
          as additional properties values.
    """

    allowed_values = {
        ('value',): {
            'APPLICATION_FEE': "APPLICATION_FEE",
            'ACH_BASIS_POINTS': "ACH_BASIS_POINTS",
            'ACH_FIXED': "ACH_FIXED",
            'CARD_BASIS_POINTS': "CARD_BASIS_POINTS",
            'CARD_FIXED': "CARD_FIXED",
            'CARD_INTERCHANGE': "CARD_INTERCHANGE",
            'VISA_BASIS_POINTS': "VISA_BASIS_POINTS",
            'VISA_FIXED': "VISA_FIXED",
            'VISA_INTERCHANGE': "VISA_INTERCHANGE",
            'VISA_ASSESSMENT_BASIS_POINTS': "VISA_ASSESSMENT_BASIS_POINTS",
            'VISA_ACQUIRER_PROCESSING_FIXED': "VISA_ACQUIRER_PROCESSING_FIXED",
            'VISA_CREDIT_VOUCHER_FIXED': "VISA_CREDIT_VOUCHER_FIXED",
            'VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED': "VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED",
            'VISA_BASE_II_CREDIT_VOUCHER_FIXED': "VISA_BASE_II_CREDIT_VOUCHER_FIXED",
            'VISA_KILOBYTE_ACCESS_FIXED': "VISA_KILOBYTE_ACCESS_FIXED",
            'DISCOVER_BASIS_POINTS': "DISCOVER_BASIS_POINTS",
            'DISCOVER_FIXED': "DISCOVER_FIXED",
            'DISCOVER_INTERCHANGE': "DISCOVER_INTERCHANGE",
            'DISCOVER_ASSESSMENT_BASIS_POINTS': "DISCOVER_ASSESSMENT_BASIS_POINTS",
            'DISCOVER_DATA_USAGE_FIXED': "DISCOVER_DATA_USAGE_FIXED",
            'DISCOVER_NETWORK_AUTHORIZATION_FIXED': "DISCOVER_NETWORK_AUTHORIZATION_FIXED",
            'DINERS_CLUB_BASIS_POINTS': "DINERS_CLUB_BASIS_POINTS",
            'DINERS_CLUB_FIXED': "DINERS_CLUB_FIXED",
            'DINERS_CLUB_INTERCHANGE': "DINERS_CLUB_INTERCHANGE",
            'MASTERCARD_BASIS_POINTS': "MASTERCARD_BASIS_POINTS",
            'MASTERCARD_FIXED': "MASTERCARD_FIXED",
            'MASTERCARD_INTERCHANGE': "MASTERCARD_INTERCHANGE",
            'MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS': "MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS",
            'MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS': "MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS",
            'MASTERCARD_ACQUIRER_FEE_BASIS_POINTS': "MASTERCARD_ACQUIRER_FEE_BASIS_POINTS",
            'JCB_BASIS_POINTS': "JCB_BASIS_POINTS",
            'JCB_FIXED': "JCB_FIXED",
            'JCB_INTERCHANGE': "JCB_INTERCHANGE",
            'AMERICAN_EXPRESS_BASIS_POINTS': "AMERICAN_EXPRESS_BASIS_POINTS",
            'AMERICAN_EXPRESS_FIXED': "AMERICAN_EXPRESS_FIXED",
            'AMERICAN_EXPRESS_INTERCHANGE': "AMERICAN_EXPRESS_INTERCHANGE",
            'AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS': "AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS",
            'DISPUTE_INQUIRY_FIXED_FEE': "DISPUTE_INQUIRY_FIXED_FEE",
            'DISPUTE_FIXED_FEE': "DISPUTE_FIXED_FEE",
            'QUALIFIED_TIER_BASIS_POINTS_FEE': "QUALIFIED_TIER_BASIS_POINTS_FEE",
            'QUALIFIED_TIER_FIXED_FEE': "QUALIFIED_TIER_FIXED_FEE",
            'CUSTOM': "CUSTOM",
            'ACH_DEBIT_RETURN_FIXED_FEE': "ACH_DEBIT_RETURN_FIXED_FEE",
            'ACH_CREDIT_RETURN_FIXED_FEE': "ACH_CREDIT_RETURN_FIXED_FEE",
            'ANCILLARY_FIXED_FEE_PRIMARY': "ANCILLARY_FIXED_FEE_PRIMARY",
            'ANCILLARY_FIXED_FEE_SECONDARY': "ANCILLARY_FIXED_FEE_SECONDARY",
            'SETTLEMENT_V2_TRANSFER': "SETTLEMENT_V2_TRANSFER",
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
            'value': (str,),
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {}

    read_only_vars = set()

    _composed_schemas = None

    required_properties = set([
        '_data_store',
        '_check_type',
        '_spec_property_naming',
        '_path_to_item',
        '_configuration',
        '_visited_composed_classes',
    ])

    @convert_js_args_to_python_args
    def __init__(self, *args, **kwargs):
        """FeeType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["APPLICATION_FEE", "ACH_BASIS_POINTS", "ACH_FIXED", "CARD_BASIS_POINTS", "CARD_FIXED", "CARD_INTERCHANGE", "VISA_BASIS_POINTS", "VISA_FIXED", "VISA_INTERCHANGE", "VISA_ASSESSMENT_BASIS_POINTS", "VISA_ACQUIRER_PROCESSING_FIXED", "VISA_CREDIT_VOUCHER_FIXED", "VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED", "VISA_BASE_II_CREDIT_VOUCHER_FIXED", "VISA_KILOBYTE_ACCESS_FIXED", "DISCOVER_BASIS_POINTS", "DISCOVER_FIXED", "DISCOVER_INTERCHANGE", "DISCOVER_ASSESSMENT_BASIS_POINTS", "DISCOVER_DATA_USAGE_FIXED", "DISCOVER_NETWORK_AUTHORIZATION_FIXED", "DINERS_CLUB_BASIS_POINTS", "DINERS_CLUB_FIXED", "DINERS_CLUB_INTERCHANGE", "MASTERCARD_BASIS_POINTS", "MASTERCARD_FIXED", "MASTERCARD_INTERCHANGE", "MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS", "MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS", "MASTERCARD_ACQUIRER_FEE_BASIS_POINTS", "JCB_BASIS_POINTS", "JCB_FIXED", "JCB_INTERCHANGE", "AMERICAN_EXPRESS_BASIS_POINTS", "AMERICAN_EXPRESS_FIXED", "AMERICAN_EXPRESS_INTERCHANGE", "AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS", "DISPUTE_INQUIRY_FIXED_FEE", "DISPUTE_FIXED_FEE", "QUALIFIED_TIER_BASIS_POINTS_FEE", "QUALIFIED_TIER_FIXED_FEE", "CUSTOM", "ACH_DEBIT_RETURN_FIXED_FEE", "ACH_CREDIT_RETURN_FIXED_FEE", "ANCILLARY_FIXED_FEE_PRIMARY", "ANCILLARY_FIXED_FEE_SECONDARY", "SETTLEMENT_V2_TRANSFER", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["APPLICATION_FEE", "ACH_BASIS_POINTS", "ACH_FIXED", "CARD_BASIS_POINTS", "CARD_FIXED", "CARD_INTERCHANGE", "VISA_BASIS_POINTS", "VISA_FIXED", "VISA_INTERCHANGE", "VISA_ASSESSMENT_BASIS_POINTS", "VISA_ACQUIRER_PROCESSING_FIXED", "VISA_CREDIT_VOUCHER_FIXED", "VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED", "VISA_BASE_II_CREDIT_VOUCHER_FIXED", "VISA_KILOBYTE_ACCESS_FIXED", "DISCOVER_BASIS_POINTS", "DISCOVER_FIXED", "DISCOVER_INTERCHANGE", "DISCOVER_ASSESSMENT_BASIS_POINTS", "DISCOVER_DATA_USAGE_FIXED", "DISCOVER_NETWORK_AUTHORIZATION_FIXED", "DINERS_CLUB_BASIS_POINTS", "DINERS_CLUB_FIXED", "DINERS_CLUB_INTERCHANGE", "MASTERCARD_BASIS_POINTS", "MASTERCARD_FIXED", "MASTERCARD_INTERCHANGE", "MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS", "MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS", "MASTERCARD_ACQUIRER_FEE_BASIS_POINTS", "JCB_BASIS_POINTS", "JCB_FIXED", "JCB_INTERCHANGE", "AMERICAN_EXPRESS_BASIS_POINTS", "AMERICAN_EXPRESS_FIXED", "AMERICAN_EXPRESS_INTERCHANGE", "AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS", "DISPUTE_INQUIRY_FIXED_FEE", "DISPUTE_FIXED_FEE", "QUALIFIED_TIER_BASIS_POINTS_FEE", "QUALIFIED_TIER_FIXED_FEE", "CUSTOM", "ACH_DEBIT_RETURN_FIXED_FEE", "ACH_CREDIT_RETURN_FIXED_FEE", "ANCILLARY_FIXED_FEE_PRIMARY", "ANCILLARY_FIXED_FEE_SECONDARY", "SETTLEMENT_V2_TRANSFER", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):
        """FeeType - a model defined in OpenAPI

        Note that value can be passed either in args or in kwargs, but not in both.

        Args:
            args[0] (str):, must be one of ["APPLICATION_FEE", "ACH_BASIS_POINTS", "ACH_FIXED", "CARD_BASIS_POINTS", "CARD_FIXED", "CARD_INTERCHANGE", "VISA_BASIS_POINTS", "VISA_FIXED", "VISA_INTERCHANGE", "VISA_ASSESSMENT_BASIS_POINTS", "VISA_ACQUIRER_PROCESSING_FIXED", "VISA_CREDIT_VOUCHER_FIXED", "VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED", "VISA_BASE_II_CREDIT_VOUCHER_FIXED", "VISA_KILOBYTE_ACCESS_FIXED", "DISCOVER_BASIS_POINTS", "DISCOVER_FIXED", "DISCOVER_INTERCHANGE", "DISCOVER_ASSESSMENT_BASIS_POINTS", "DISCOVER_DATA_USAGE_FIXED", "DISCOVER_NETWORK_AUTHORIZATION_FIXED", "DINERS_CLUB_BASIS_POINTS", "DINERS_CLUB_FIXED", "DINERS_CLUB_INTERCHANGE", "MASTERCARD_BASIS_POINTS", "MASTERCARD_FIXED", "MASTERCARD_INTERCHANGE", "MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS", "MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS", "MASTERCARD_ACQUIRER_FEE_BASIS_POINTS", "JCB_BASIS_POINTS", "JCB_FIXED", "JCB_INTERCHANGE", "AMERICAN_EXPRESS_BASIS_POINTS", "AMERICAN_EXPRESS_FIXED", "AMERICAN_EXPRESS_INTERCHANGE", "AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS", "DISPUTE_INQUIRY_FIXED_FEE", "DISPUTE_FIXED_FEE", "QUALIFIED_TIER_BASIS_POINTS_FEE", "QUALIFIED_TIER_FIXED_FEE", "CUSTOM", "ACH_DEBIT_RETURN_FIXED_FEE", "ACH_CREDIT_RETURN_FIXED_FEE", "ANCILLARY_FIXED_FEE_PRIMARY", "ANCILLARY_FIXED_FEE_SECONDARY", "SETTLEMENT_V2_TRANSFER", ]  # noqa: E501

        Keyword Args:
            value (str):, must be one of ["APPLICATION_FEE", "ACH_BASIS_POINTS", "ACH_FIXED", "CARD_BASIS_POINTS", "CARD_FIXED", "CARD_INTERCHANGE", "VISA_BASIS_POINTS", "VISA_FIXED", "VISA_INTERCHANGE", "VISA_ASSESSMENT_BASIS_POINTS", "VISA_ACQUIRER_PROCESSING_FIXED", "VISA_CREDIT_VOUCHER_FIXED", "VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED", "VISA_BASE_II_CREDIT_VOUCHER_FIXED", "VISA_KILOBYTE_ACCESS_FIXED", "DISCOVER_BASIS_POINTS", "DISCOVER_FIXED", "DISCOVER_INTERCHANGE", "DISCOVER_ASSESSMENT_BASIS_POINTS", "DISCOVER_DATA_USAGE_FIXED", "DISCOVER_NETWORK_AUTHORIZATION_FIXED", "DINERS_CLUB_BASIS_POINTS", "DINERS_CLUB_FIXED", "DINERS_CLUB_INTERCHANGE", "MASTERCARD_BASIS_POINTS", "MASTERCARD_FIXED", "MASTERCARD_INTERCHANGE", "MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS", "MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS", "MASTERCARD_ACQUIRER_FEE_BASIS_POINTS", "JCB_BASIS_POINTS", "JCB_FIXED", "JCB_INTERCHANGE", "AMERICAN_EXPRESS_BASIS_POINTS", "AMERICAN_EXPRESS_FIXED", "AMERICAN_EXPRESS_INTERCHANGE", "AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS", "DISPUTE_INQUIRY_FIXED_FEE", "DISPUTE_FIXED_FEE", "QUALIFIED_TIER_BASIS_POINTS_FEE", "QUALIFIED_TIER_FIXED_FEE", "CUSTOM", "ACH_DEBIT_RETURN_FIXED_FEE", "ACH_CREDIT_RETURN_FIXED_FEE", "ANCILLARY_FIXED_FEE_PRIMARY", "ANCILLARY_FIXED_FEE_SECONDARY", "SETTLEMENT_V2_TRANSFER", ]  # noqa: E501
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
        """
        # required up here when default value is not given
        _path_to_item = kwargs.pop('_path_to_item', ())

        self = super(OpenApiModel, cls).__new__(cls)

        if 'value' in kwargs:
            value = kwargs.pop('value')
        elif args:
            args = list(args)
            value = args.pop(0)
        else:
            raise ApiTypeError(
                "value is required, but not passed in args or kwargs and doesn't have default",
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        _check_type = kwargs.pop('_check_type', True)
        _spec_property_naming = kwargs.pop('_spec_property_naming', False)
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
        self.value = value
        if kwargs:
            raise ApiTypeError(
                "Invalid named arguments=%s passed to %s. Remove those invalid named arguments." % (
                    kwargs,
                    self.__class__.__name__,
                ),
                path_to_item=_path_to_item,
                valid_classes=(self.__class__,),
            )

        return self
