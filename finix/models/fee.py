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
    Currency
    FeeLinks


class Fee(ModelNormal):
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
        ('fee_subtype',): {
            '&#39;CUSTOM&#39;': 'CUSTOM',
            '&#39;APPLICATION_FEE&#39;': 'APPLICATION_FEE',
            '&#39;PLATFORM_FEE&#39;': 'PLATFORM_FEE',
        },
        ('fee_type',): {
            '&#39;APPLICATION_FEE&#39;': 'APPLICATION_FEE',
            '&#39;ACH_BASIS_POINTS&#39;': 'ACH_BASIS_POINTS',
            '&#39;ACH_FIXED&#39;': 'ACH_FIXED',
            '&#39;CARD_BASIS_POINTS&#39;': 'CARD_BASIS_POINTS',
            '&#39;CARD_FIXED&#39;': 'CARD_FIXED',
            '&#39;CARD_INTERCHANGE&#39;': 'CARD_INTERCHANGE',
            '&#39;VISA_BASIS_POINTS&#39;': 'VISA_BASIS_POINTS',
            '&#39;VISA_FIXED&#39;': 'VISA_FIXED',
            '&#39;VISA_INTERCHANGE&#39;': 'VISA_INTERCHANGE',
            '&#39;VISA_ASSESSMENT_BASIS_POINTS&#39;': 'VISA_ASSESSMENT_BASIS_POINTS',
            '&#39;VISA_ACQUIRER_PROCESSING_FIXED&#39;': 'VISA_ACQUIRER_PROCESSING_FIXED',
            '&#39;VISA_CREDIT_VOUCHER_FIXED&#39;': 'VISA_CREDIT_VOUCHER_FIXED',
            '&#39;VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED&#39;': 'VISA_BASE_II_SYSTEM_FILE_TRANSMISSION_FIXED',
            '&#39;VISA_BASE_II_CREDIT_VOUCHER_FIXED&#39;': 'VISA_BASE_II_CREDIT_VOUCHER_FIXED',
            '&#39;VISA_KILOBYTE_ACCESS_FIXED&#39;': 'VISA_KILOBYTE_ACCESS_FIXED',
            '&#39;DISCOVER_BASIS_POINTS&#39;': 'DISCOVER_BASIS_POINTS',
            '&#39;DISCOVER_FIXED&#39;': 'DISCOVER_FIXED',
            '&#39;DISCOVER_INTERCHANGE&#39;': 'DISCOVER_INTERCHANGE',
            '&#39;DISCOVER_ASSESSMENT_BASIS_POINTS&#39;': 'DISCOVER_ASSESSMENT_BASIS_POINTS',
            '&#39;DISCOVER_DATA_USAGE_FIXED&#39;': 'DISCOVER_DATA_USAGE_FIXED',
            '&#39;DISCOVER_NETWORK_AUTHORIZATION_FIXED&#39;': 'DISCOVER_NETWORK_AUTHORIZATION_FIXED',
            '&#39;DINERS_CLUB_BASIS_POINTS&#39;': 'DINERS_CLUB_BASIS_POINTS',
            '&#39;DINERS_CLUB_FIXED&#39;': 'DINERS_CLUB_FIXED',
            '&#39;DINERS_CLUB_INTERCHANGE&#39;': 'DINERS_CLUB_INTERCHANGE',
            '&#39;MASTERCARD_BASIS_POINTS&#39;': 'MASTERCARD_BASIS_POINTS',
            '&#39;MASTERCARD_FIXED&#39;': 'MASTERCARD_FIXED',
            '&#39;MASTERCARD_INTERCHANGE&#39;': 'MASTERCARD_INTERCHANGE',
            '&#39;MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS&#39;': 'MASTERCARD_ASSESSMENT_UNDER_1K_BASIS_POINTS',
            '&#39;MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS&#39;': 'MASTERCARD_ASSESSMENT_OVER_1K_BASIS_POINTS',
            '&#39;MASTERCARD_ACQUIRER_FEE_BASIS_POINTS&#39;': 'MASTERCARD_ACQUIRER_FEE_BASIS_POINTS',
            '&#39;JCB_BASIS_POINTS&#39;': 'JCB_BASIS_POINTS',
            '&#39;JCB_FIXED&#39;': 'JCB_FIXED',
            '&#39;JCB_INTERCHANGE&#39;': 'JCB_INTERCHANGE',
            '&#39;AMERICAN_EXPRESS_BASIS_POINTS&#39;': 'AMERICAN_EXPRESS_BASIS_POINTS',
            '&#39;AMERICAN_EXPRESS_FIXED&#39;': 'AMERICAN_EXPRESS_FIXED',
            '&#39;AMERICAN_EXPRESS_INTERCHANGE&#39;': 'AMERICAN_EXPRESS_INTERCHANGE',
            '&#39;AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS&#39;': 'AMERICAN_EXPRESS_ASSESSMENT_BASIS_POINTS',
            '&#39;DISPUTE_INQUIRY_FIXED_FEE&#39;': 'DISPUTE_INQUIRY_FIXED_FEE',
            '&#39;DISPUTE_FIXED_FEE&#39;': 'DISPUTE_FIXED_FEE',
            '&#39;QUALIFIED_TIER_BASIS_POINTS_FEE&#39;': 'QUALIFIED_TIER_BASIS_POINTS_FEE',
            '&#39;QUALIFIED_TIER_FIXED_FEE&#39;': 'QUALIFIED_TIER_FIXED_FEE',
            '&#39;CUSTOM&#39;': 'CUSTOM',
            '&#39;ACH_DEBIT_RETURN_FIXED_FEE&#39;': 'ACH_DEBIT_RETURN_FIXED_FEE',
            '&#39;ACH_CREDIT_RETURN_FIXED_FEE&#39;': 'ACH_CREDIT_RETURN_FIXED_FEE',
            '&#39;ANCILLARY_FIXED_FEE_PRIMARY&#39;': 'ANCILLARY_FIXED_FEE_PRIMARY',
            '&#39;ANCILLARY_FIXED_FEE_SECONDARY&#39;': 'ANCILLARY_FIXED_FEE_SECONDARY',
            '&#39;SETTLEMENT_V2_TRANSFER&#39;': 'SETTLEMENT_V2_TRANSFER',
        },
        ('linked_type',): {
            '&#39;APPLICATION&#39;': 'APPLICATION',
            '&#39;PLATFORM&#39;': 'PLATFORM',
            '&#39;SUBSCRIPTION&#39;': 'SUBSCRIPTION',
            '&#39;TRANSFER&#39;': 'TRANSFER',
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
        lazy_import()
        return {
            'id': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'display_name': (str,),  # noqa: E501
            'fee_subtype': (str,),  # noqa: E501
            'fee_type': (str,),  # noqa: E501
            'label': (str,),  # noqa: E501
            'linked_id': (str,),  # noqa: E501
            'linked_type': (str,),  # noqa: E501
            'merchant': (str,),  # noqa: E501
            'tags': (object,),  # noqa: E501
            'links': (FeeLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'display_name': 'display_name',  # noqa: E501
        'fee_subtype': 'fee_subtype',  # noqa: E501
        'fee_type': 'fee_type',  # noqa: E501
        'label': 'label',  # noqa: E501
        'linked_id': 'linked_id',  # noqa: E501
        'linked_type': 'linked_type',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Fee - a model defined in OpenAPI

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
            id (str): The ID of the `fee` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            amount (int): The amount of the fee in cents.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            display_name (str): The name of the `fee` object that was include in `display_name` when creating the fee.. [optional]  # noqa: E501
            fee_subtype (str): Subtype of the `fee`.. [optional]  # noqa: E501
            fee_type (str): The type of `fee`.. [optional]  # noqa: E501
            label (str): The name of the `fee` object that was include in `label` when creating the fee.. [optional]  # noqa: E501
            linked_id (str): ID of the linked resource.. [optional]  # noqa: E501
            linked_type (str): The type of entity the `fee` is linked to (**null** by default).. [optional]  # noqa: E501
            merchant (str): The `Merchant` ID that the fee is being debited from.. [optional]  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            links (FeeLinks): [optional]  # noqa: E501
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
        """Fee - a model defined in OpenAPI

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
            id (str): The ID of the `fee` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            amount (int): The amount of the fee in cents.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            display_name (str): The name of the `fee` object that was include in `display_name` when creating the fee.. [optional]  # noqa: E501
            fee_subtype (str): Subtype of the `fee`.. [optional]  # noqa: E501
            fee_type (str): The type of `fee`.. [optional]  # noqa: E501
            label (str): The name of the `fee` object that was include in `label` when creating the fee.. [optional]  # noqa: E501
            linked_id (str): ID of the linked resource.. [optional]  # noqa: E501
            linked_type (str): The type of entity the `fee` is linked to (**null** by default).. [optional]  # noqa: E501
            merchant (str): The `Merchant` ID that the fee is being debited from.. [optional]  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            links (FeeLinks): [optional]  # noqa: E501
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
