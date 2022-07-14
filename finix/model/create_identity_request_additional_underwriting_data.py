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
    from finix.model.create_identity_request_additional_underwriting_data_card_volume_distribution import CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution
    from finix.model.create_identity_request_additional_underwriting_data_volume_distribution_by_business_type import CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType
    globals()['CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution'] = CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution
    globals()['CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType'] = CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType


class CreateIdentityRequestAdditionalUnderwritingData(ModelNormal):
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
        ('refund_policy',): {
            'NO_REFUNDS': "NO_REFUNDS",
            'MERCHANDISE_EXCHANGE_ONLY': "MERCHANDISE_EXCHANGE_ONLY",
            '30_DAYS': "30_DAYS",
        },
    }

    validations = {
        ('merchant_agreement_ip_address',): {
            'min_length': 1,
        },
        ('credit_check_user_agent',): {
            'min_length': 1,
        },
        ('refund_policy',): {
            'min_length': 1,
        },
        ('credit_check_timestamp',): {
            'min_length': 1,
        },
        ('merchant_agreement_timestamp',): {
            'min_length': 1,
        },
        ('business_description',): {
            'min_length': 1,
        },
        ('credit_check_ip_address',): {
            'min_length': 1,
        },
        ('merchant_agreement_user_agent',): {
            'min_length': 1,
        },
    }

    @cached_property
    def additional_properties_type():
        """
        This must be a method because a model may have properties that are
        of type self, this must run after the class is loaded
        """
        lazy_import()
        return (bool, date, datetime, dict, float, int, list, str, none_type,)  # noqa: E501

    _nullable = True

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
            'merchant_agreement_accepted': (bool,),  # noqa: E501
            'merchant_agreement_ip_address': (str,),  # noqa: E501
            'volume_distribution_by_business_type': (CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType,),  # noqa: E501
            'average_ach_transfer_amount': (int,),  # noqa: E501
            'annual_ach_volume': (int,),  # noqa: E501
            'credit_check_user_agent': (str,),  # noqa: E501
            'refund_policy': (str,),  # noqa: E501
            'credit_check_timestamp': (str,),  # noqa: E501
            'credit_check_allowed': (bool,),  # noqa: E501
            'merchant_agreement_timestamp': (str,),  # noqa: E501
            'business_description': (str,),  # noqa: E501
            'average_card_transfer_amount': (int,),  # noqa: E501
            'credit_check_ip_address': (str,),  # noqa: E501
            'merchant_agreement_user_agent': (str,),  # noqa: E501
            'card_volume_distribution': (CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'merchant_agreement_accepted': 'merchant_agreement_accepted',  # noqa: E501
        'merchant_agreement_ip_address': 'merchant_agreement_ip_address',  # noqa: E501
        'volume_distribution_by_business_type': 'volume_distribution_by_business_type',  # noqa: E501
        'average_ach_transfer_amount': 'average_ach_transfer_amount',  # noqa: E501
        'annual_ach_volume': 'annual_ach_volume',  # noqa: E501
        'credit_check_user_agent': 'credit_check_user_agent',  # noqa: E501
        'refund_policy': 'refund_policy',  # noqa: E501
        'credit_check_timestamp': 'credit_check_timestamp',  # noqa: E501
        'credit_check_allowed': 'credit_check_allowed',  # noqa: E501
        'merchant_agreement_timestamp': 'merchant_agreement_timestamp',  # noqa: E501
        'business_description': 'business_description',  # noqa: E501
        'average_card_transfer_amount': 'average_card_transfer_amount',  # noqa: E501
        'credit_check_ip_address': 'credit_check_ip_address',  # noqa: E501
        'merchant_agreement_user_agent': 'merchant_agreement_user_agent',  # noqa: E501
        'card_volume_distribution': 'card_volume_distribution',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """CreateIdentityRequestAdditionalUnderwritingData - a model defined in OpenAPI

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
            merchant_agreement_accepted (bool): Sets whether this merchant has accepted the terms and conditions of the merchant agreement.. [optional]  # noqa: E501
            merchant_agreement_ip_address (str): IP address of the merchant when this merchant accepted the merchant agreement (e.g., 42.1.1.113).. [optional]  # noqa: E501
            volume_distribution_by_business_type (CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType): [optional]  # noqa: E501
            average_ach_transfer_amount (int): The approximate average ACH sale amount (in cents) for this merchant.. [optional]  # noqa: E501
            annual_ach_volume (int): The approximate annual ACH sales expected to be processed (in cents) by this merchant (max 10 characters).. [optional]  # noqa: E501
            credit_check_user_agent (str): The details of the browser that was used when this merchant consented to a credit check (e.g., Mozilla 5.0 (Macintosh; Intel Mac OS X 10 _14_6)).. [optional]  # noqa: E501
            refund_policy (str): Include the value that best applies to the merchant's refund policy.. [optional]  # noqa: E501
            credit_check_timestamp (str): A timestamp of when this merchant consented to a credit check (e.g., 2021-04-28T16:42:55Z).. [optional]  # noqa: E501
            credit_check_allowed (bool): Sets if this merchant has consented and accepted to a credit check.. [optional]  # noqa: E501
            merchant_agreement_timestamp (str): Timestamp of when the merchant accepted Finix's Terms of Service (e.g., 2021-04-28T16:42:55Z).. [optional]  # noqa: E501
            business_description (str): Description of this merchant's business (max 200 characters).. [optional]  # noqa: E501
            average_card_transfer_amount (int): The average credit card sale amount (in cents) for this merchant.. [optional]  # noqa: E501
            credit_check_ip_address (str): The IP address of the merchant when they consented to a credit check (e.g., 42.1.1.113 ).. [optional]  # noqa: E501
            merchant_agreement_user_agent (str): The details of the browser that was used when this merchant accepted Finix's Terms of Service (e.g., Mozilla 5.0 (Macintosh; Intel Mac OS X 10 _14_6)).. [optional]  # noqa: E501
            card_volume_distribution (CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution): [optional]  # noqa: E501
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
        """CreateIdentityRequestAdditionalUnderwritingData - a model defined in OpenAPI

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
            merchant_agreement_accepted (bool): Sets whether this merchant has accepted the terms and conditions of the merchant agreement.. [optional]  # noqa: E501
            merchant_agreement_ip_address (str): IP address of the merchant when this merchant accepted the merchant agreement (e.g., 42.1.1.113).. [optional]  # noqa: E501
            volume_distribution_by_business_type (CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType): [optional]  # noqa: E501
            average_ach_transfer_amount (int): The approximate average ACH sale amount (in cents) for this merchant.. [optional]  # noqa: E501
            annual_ach_volume (int): The approximate annual ACH sales expected to be processed (in cents) by this merchant (max 10 characters).. [optional]  # noqa: E501
            credit_check_user_agent (str): The details of the browser that was used when this merchant consented to a credit check (e.g., Mozilla 5.0 (Macintosh; Intel Mac OS X 10 _14_6)).. [optional]  # noqa: E501
            refund_policy (str): Include the value that best applies to the merchant's refund policy.. [optional]  # noqa: E501
            credit_check_timestamp (str): A timestamp of when this merchant consented to a credit check (e.g., 2021-04-28T16:42:55Z).. [optional]  # noqa: E501
            credit_check_allowed (bool): Sets if this merchant has consented and accepted to a credit check.. [optional]  # noqa: E501
            merchant_agreement_timestamp (str): Timestamp of when the merchant accepted Finix's Terms of Service (e.g., 2021-04-28T16:42:55Z).. [optional]  # noqa: E501
            business_description (str): Description of this merchant's business (max 200 characters).. [optional]  # noqa: E501
            average_card_transfer_amount (int): The average credit card sale amount (in cents) for this merchant.. [optional]  # noqa: E501
            credit_check_ip_address (str): The IP address of the merchant when they consented to a credit check (e.g., 42.1.1.113 ).. [optional]  # noqa: E501
            merchant_agreement_user_agent (str): The details of the browser that was used when this merchant accepted Finix's Terms of Service (e.g., Mozilla 5.0 (Macintosh; Intel Mac OS X 10 _14_6)).. [optional]  # noqa: E501
            card_volume_distribution (CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution): [optional]  # noqa: E501
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
