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



class ListDisputesQueryParams(ModelNormal):
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
        return {
            'limit': (int,),  # noqa: E501
            'created_at_gte': (str,),  # noqa: E501
            'created_at_lte': (str,),  # noqa: E501
            'updated_at_gte': (str,),  # noqa: E501
            'updated_at_lte': (str,),  # noqa: E501
            'transfer_id': (str,),  # noqa: E501
            'adjustment_transfer_id': (str,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'amount_gte': (int,),  # noqa: E501
            'amount_gt': (int,),  # noqa: E501
            'amount_lt': (int,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'response_state': (str,),  # noqa: E501
            'respond_by_lte': (str,),  # noqa: E501
            'respond_by_gte': (str,),  # noqa: E501
            'instrument_bin': (str,),  # noqa: E501
            'instrument_brand_type': (str,),  # noqa: E501
            'merchant_identity_id': (str,),  # noqa: E501
            'merchant_identity_name': (str,),  # noqa: E501
            'instrument_name': (str,),  # noqa: E501
            'instrument_type': (str,),  # noqa: E501
            'merchant_id': (str,),  # noqa: E501
            'merchant_mid': (str,),  # noqa: E501
            'instrument_card_last4': (str,),  # noqa: E501
            'instrument_card_type': (str,),  # noqa: E501
            'instrument_fingerprint': (str,),  # noqa: E501
            'before_cursor': (str,),  # noqa: E501
            'tags_key': (str,),  # noqa: E501
            'tags_value': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'limit': 'limit',  # noqa: E501
        'created_at_gte': 'created_at.gte',  # noqa: E501
        'created_at_lte': 'created_at.lte',  # noqa: E501
        'updated_at_gte': 'updated_at.gte',  # noqa: E501
        'updated_at_lte': 'updated_at.lte',  # noqa: E501
        'transfer_id': 'transfer_id',  # noqa: E501
        'adjustment_transfer_id': 'adjustment_transfer_id',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'amount_gte': 'amount.gte',  # noqa: E501
        'amount_gt': 'amount.gt',  # noqa: E501
        'amount_lt': 'amount.lt',  # noqa: E501
        'state': 'state',  # noqa: E501
        'response_state': 'response_state',  # noqa: E501
        'respond_by_lte': 'respond_by.lte',  # noqa: E501
        'respond_by_gte': 'respond_by.gte',  # noqa: E501
        'instrument_bin': 'instrument_bin',  # noqa: E501
        'instrument_brand_type': 'instrument_brand_type',  # noqa: E501
        'merchant_identity_id': 'merchant_identity_id',  # noqa: E501
        'merchant_identity_name': 'merchant_identity_name',  # noqa: E501
        'instrument_name': 'instrument_name',  # noqa: E501
        'instrument_type': 'instrument_type',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'merchant_mid': 'merchant_mid',  # noqa: E501
        'instrument_card_last4': 'instrument_card_last4',  # noqa: E501
        'instrument_card_type': 'instrument_card_type',  # noqa: E501
        'instrument_fingerprint': 'instrument_fingerprint',  # noqa: E501
        'before_cursor': 'before_cursor',  # noqa: E501
        'tags_key': 'tags.key',  # noqa: E501
        'tags_value': 'tags.value',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ListDisputesQueryParams - a model defined in OpenAPI

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
            limit (int): The numbers of items to return.. [optional]  # noqa: E501
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]  # noqa: E501
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]  # noqa: E501
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]  # noqa: E501
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]  # noqa: E501
            transfer_id (str): Filter by the ID of the `Transfer` that's being disputed. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]  # noqa: E501
            adjustment_transfer_id (str): Filter by the ID of the adjustment `Transfer`. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]  # noqa: E501
            amount (int): Filter by an amount equal to the given value.. [optional]  # noqa: E501
            amount_gte (int): Filter by an amount greater than or equal.. [optional]  # noqa: E501
            amount_gt (int): Filter by an amount greater than.. [optional]  # noqa: E501
            amount_lt (int): Filter by an amount less than.. [optional]  # noqa: E501
            state (str): Filter by the state of the `Dispute`.. [optional]  # noqa: E501
            response_state (str): Filter by the `response_state` of the `Dispute`.. [optional]  # noqa: E501
            respond_by_lte (str): Filter where `respond_by` is before the given date.. [optional]  # noqa: E501
            respond_by_gte (str): Filter where `respond_by` is after the given date.. [optional]  # noqa: E501
            instrument_bin (str): Filter by the Bank Identification Number (BIN). The BIN is the first 6 digits of the masked account number.. [optional]  # noqa: E501
            instrument_brand_type (str): Filter by the card brand used.. [optional]  # noqa: E501
            merchant_identity_id (str): Filter by the ID of the `Identity` used by the `Merchant`.. [optional]  # noqa: E501
            merchant_identity_name (str): Filter by the name used by the `Merchant`.. [optional]  # noqa: E501
            instrument_name (str): Filter by the name of the `Payment Instrument`.. [optional]  # noqa: E501
            instrument_type (str): Filter by `Payment Instrument` type.. [optional]  # noqa: E501
            merchant_id (str): Filter by the ID of the `Merchant`.. [optional]  # noqa: E501
            merchant_mid (str): Filter by the MID of the `Merchant`.. [optional]  # noqa: E501
            instrument_card_last4 (str): Filter by the last 4 digits of the card used.. [optional]  # noqa: E501
            instrument_card_type (str): Filter by the card type.. [optional]  # noqa: E501
            instrument_fingerprint (str): Filter by the fingerprint of the `Payment Instrument`.. [optional]  # noqa: E501
            before_cursor (str): Returns every `Dispute` created before the cursor value.. [optional]  # noqa: E501
            tags_key (str): Filter by the [`key` of a `Tag`](/api/overview/#section/Tags).. [optional]  # noqa: E501
            tags_value (str): Filter by the [value of a `Tag`](https://finix.com/docs/api/overview/#section/Tags).. [optional]  # noqa: E501
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
        """ListDisputesQueryParams - a model defined in OpenAPI

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
            limit (int): The numbers of items to return.. [optional]  # noqa: E501
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]  # noqa: E501
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]  # noqa: E501
            updated_at_gte (str): Filter where `updated_at` is after the given date.. [optional]  # noqa: E501
            updated_at_lte (str): Filter where `updated_at` is before the given date.. [optional]  # noqa: E501
            transfer_id (str): Filter by the ID of the `Transfer` that's being disputed. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]  # noqa: E501
            adjustment_transfer_id (str): Filter by the ID of the adjustment `Transfer`. <br><br>**Note**: If included, all other filter parameters are ignored.. [optional]  # noqa: E501
            amount (int): Filter by an amount equal to the given value.. [optional]  # noqa: E501
            amount_gte (int): Filter by an amount greater than or equal.. [optional]  # noqa: E501
            amount_gt (int): Filter by an amount greater than.. [optional]  # noqa: E501
            amount_lt (int): Filter by an amount less than.. [optional]  # noqa: E501
            state (str): Filter by the state of the `Dispute`.. [optional]  # noqa: E501
            response_state (str): Filter by the `response_state` of the `Dispute`.. [optional]  # noqa: E501
            respond_by_lte (str): Filter where `respond_by` is before the given date.. [optional]  # noqa: E501
            respond_by_gte (str): Filter where `respond_by` is after the given date.. [optional]  # noqa: E501
            instrument_bin (str): Filter by the Bank Identification Number (BIN). The BIN is the first 6 digits of the masked account number.. [optional]  # noqa: E501
            instrument_brand_type (str): Filter by the card brand used.. [optional]  # noqa: E501
            merchant_identity_id (str): Filter by the ID of the `Identity` used by the `Merchant`.. [optional]  # noqa: E501
            merchant_identity_name (str): Filter by the name used by the `Merchant`.. [optional]  # noqa: E501
            instrument_name (str): Filter by the name of the `Payment Instrument`.. [optional]  # noqa: E501
            instrument_type (str): Filter by `Payment Instrument` type.. [optional]  # noqa: E501
            merchant_id (str): Filter by the ID of the `Merchant`.. [optional]  # noqa: E501
            merchant_mid (str): Filter by the MID of the `Merchant`.. [optional]  # noqa: E501
            instrument_card_last4 (str): Filter by the last 4 digits of the card used.. [optional]  # noqa: E501
            instrument_card_type (str): Filter by the card type.. [optional]  # noqa: E501
            instrument_fingerprint (str): Filter by the fingerprint of the `Payment Instrument`.. [optional]  # noqa: E501
            before_cursor (str): Returns every `Dispute` created before the cursor value.. [optional]  # noqa: E501
            tags_key (str): Filter by the [`key` of a `Tag`](/api/overview/#section/Tags).. [optional]  # noqa: E501
            tags_value (str): Filter by the [value of a `Tag`](https://finix.com/docs/api/overview/#section/Tags).. [optional]  # noqa: E501
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
