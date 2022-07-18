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
    from finix.model.currency import Currency
    from finix.model.settlement_engine_settlement_links import SettlementEngineSettlementLinks
    from finix.model.tags import Tags
    globals()['Currency'] = Currency
    globals()['SettlementEngineSettlementLinks'] = SettlementEngineSettlementLinks
    globals()['Tags'] = Tags


class SettlementEngineSettlement(ModelNormal):
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
        ('schedule_type',): {
            'None': None,
            'DAILY': "DAILY",
            'MONTHLY': "MONTHLY",
            'CONTINUOUS': "CONTINUOUS",
        },
        ('status',): {
            'APPROVED': "APPROVED",
            'AWAITING_APPROVAL': "AWAITING_APPROVAL",
            'CANCELLED': "CANCELLED",
            'PENDING': "PENDING",
            'STAGED': "STAGED",
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
            'id': (str, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'adjustment_credit_amount': (int,),  # noqa: E501
            'adjustment_credit_count': (int,),  # noqa: E501
            'adjustment_debit_amount': (int,),  # noqa: E501
            'adjustment_debit_count': (int,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'auto_close_time': (datetime, none_type,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'dispute_credit_amount': (int,),  # noqa: E501
            'dispute_credit_count': (int,),  # noqa: E501
            'dispute_debit_amount': (int,),  # noqa: E501
            'dispute_debit_count': (int,),  # noqa: E501
            'exception': (bool,),  # noqa: E501
            'fee_count': (int,),  # noqa: E501
            'identity': (str, none_type,),  # noqa: E501
            'merchant': (str, none_type,),  # noqa: E501
            'payout_plan': (str,),  # noqa: E501
            'processor_type': (str,),  # noqa: E501
            'reverse_amount': (int,),  # noqa: E501
            'reverse_count': (int,),  # noqa: E501
            'schedule_type': (str, none_type,),  # noqa: E501
            'settlement_group': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'total_amount': (int,),  # noqa: E501
            'total_fee_amount': (int,),  # noqa: E501
            'transfer_credit_amount': (int,),  # noqa: E501
            'transfer_credit_count': (int,),  # noqa: E501
            'transfer_debit_amount': (int,),  # noqa: E501
            'transfer_debit_count': (int,),  # noqa: E501
            'window_end': (datetime, none_type,),  # noqa: E501
            'window_start': (datetime, none_type,),  # noqa: E501
            'links': (SettlementEngineSettlementLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tags': 'tags',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'adjustment_credit_amount': 'adjustment_credit_amount',  # noqa: E501
        'adjustment_credit_count': 'adjustment_credit_count',  # noqa: E501
        'adjustment_debit_amount': 'adjustment_debit_amount',  # noqa: E501
        'adjustment_debit_count': 'adjustment_debit_count',  # noqa: E501
        'application': 'application',  # noqa: E501
        'auto_close_time': 'auto_close_time',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'dispute_credit_amount': 'dispute_credit_amount',  # noqa: E501
        'dispute_credit_count': 'dispute_credit_count',  # noqa: E501
        'dispute_debit_amount': 'dispute_debit_amount',  # noqa: E501
        'dispute_debit_count': 'dispute_debit_count',  # noqa: E501
        'exception': 'exception',  # noqa: E501
        'fee_count': 'fee_count',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'payout_plan': 'payout_plan',  # noqa: E501
        'processor_type': 'processor_type',  # noqa: E501
        'reverse_amount': 'reverse_amount',  # noqa: E501
        'reverse_count': 'reverse_count',  # noqa: E501
        'schedule_type': 'schedule_type',  # noqa: E501
        'settlement_group': 'settlement_group',  # noqa: E501
        'status': 'status',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'total_fee_amount': 'total_fee_amount',  # noqa: E501
        'transfer_credit_amount': 'transfer_credit_amount',  # noqa: E501
        'transfer_credit_count': 'transfer_credit_count',  # noqa: E501
        'transfer_debit_amount': 'transfer_debit_amount',  # noqa: E501
        'transfer_debit_count': 'transfer_debit_count',  # noqa: E501
        'window_end': 'window_end',  # noqa: E501
        'window_start': 'window_start',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """SettlementEngineSettlement - a model defined in OpenAPI

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
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            adjustment_credit_amount (int): [optional]  # noqa: E501
            adjustment_credit_count (int): [optional]  # noqa: E501
            adjustment_debit_amount (int): [optional]  # noqa: E501
            adjustment_debit_count (int): [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            auto_close_time (datetime, none_type): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            dispute_credit_amount (int): [optional]  # noqa: E501
            dispute_credit_count (int): [optional]  # noqa: E501
            dispute_debit_amount (int): [optional]  # noqa: E501
            dispute_debit_count (int): [optional]  # noqa: E501
            exception (bool): [optional]  # noqa: E501
            fee_count (int): [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            merchant (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            payout_plan (str): [optional]  # noqa: E501
            processor_type (str): [optional]  # noqa: E501
            reverse_amount (int): [optional]  # noqa: E501
            reverse_count (int): [optional]  # noqa: E501
            schedule_type (str, none_type): [optional]  # noqa: E501
            settlement_group (str): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            total_amount (int): [optional]  # noqa: E501
            total_fee_amount (int): [optional]  # noqa: E501
            transfer_credit_amount (int): [optional]  # noqa: E501
            transfer_credit_count (int): [optional]  # noqa: E501
            transfer_debit_amount (int): [optional]  # noqa: E501
            transfer_debit_count (int): [optional]  # noqa: E501
            window_end (datetime, none_type): [optional]  # noqa: E501
            window_start (datetime, none_type): [optional]  # noqa: E501
            links (SettlementEngineSettlementLinks): [optional]  # noqa: E501
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
        """SettlementEngineSettlement - a model defined in OpenAPI

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
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            adjustment_credit_amount (int): [optional]  # noqa: E501
            adjustment_credit_count (int): [optional]  # noqa: E501
            adjustment_debit_amount (int): [optional]  # noqa: E501
            adjustment_debit_count (int): [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            auto_close_time (datetime, none_type): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            dispute_credit_amount (int): [optional]  # noqa: E501
            dispute_credit_count (int): [optional]  # noqa: E501
            dispute_debit_amount (int): [optional]  # noqa: E501
            dispute_debit_count (int): [optional]  # noqa: E501
            exception (bool): [optional]  # noqa: E501
            fee_count (int): [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            merchant (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            payout_plan (str): [optional]  # noqa: E501
            processor_type (str): [optional]  # noqa: E501
            reverse_amount (int): [optional]  # noqa: E501
            reverse_count (int): [optional]  # noqa: E501
            schedule_type (str, none_type): [optional]  # noqa: E501
            settlement_group (str): [optional]  # noqa: E501
            status (str): [optional]  # noqa: E501
            total_amount (int): [optional]  # noqa: E501
            total_fee_amount (int): [optional]  # noqa: E501
            transfer_credit_amount (int): [optional]  # noqa: E501
            transfer_credit_count (int): [optional]  # noqa: E501
            transfer_debit_amount (int): [optional]  # noqa: E501
            transfer_debit_count (int): [optional]  # noqa: E501
            window_end (datetime, none_type): [optional]  # noqa: E501
            window_start (datetime, none_type): [optional]  # noqa: E501
            links (SettlementEngineSettlementLinks): [optional]  # noqa: E501
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
