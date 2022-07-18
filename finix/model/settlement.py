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
    from finix.model.settlement_links import SettlementLinks
    from finix.model.tags import Tags
    globals()['Currency'] = Currency
    globals()['SettlementLinks'] = SettlementLinks
    globals()['Tags'] = Tags


class Settlement(ModelNormal):
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
        ('type',): {
            'MERCHANT_REVENUE': "MERCHANT_REVENUE",
            'PLATFORM_FEE': "PLATFORM_FEE",
            'PARTNER_FEE': "PARTNER_FEE",
            'NOOP': "NOOP",
            'MERCHANT': "MERCHANT",
            'APPLICATION': "APPLICATION",
            'PLATFORM': "PLATFORM",
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
        ('destination',): {
            'regex': {
                'pattern': r'^(PI)[a-zA-Z0-9]{16,32}$',  # noqa: E501
            },
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
            'type': (str,),  # noqa: E501
            'id': (str, none_type,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'destination': (str, none_type,),  # noqa: E501
            'funds_flow': (str, none_type,),  # noqa: E501
            'identity': (str, none_type,),  # noqa: E501
            'merchant_id': (str, none_type,),  # noqa: E501
            'net_amount': (int,),  # noqa: E501
            'payment_type': (str, none_type,),  # noqa: E501
            'processor': (str,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'total_amount': (int,),  # noqa: E501
            'total_fee': (int,),  # noqa: E501
            'total_fees': (int,),  # noqa: E501
            'links': (SettlementLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'tags': 'tags',  # noqa: E501
        'type': 'type',  # noqa: E501
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'application': 'application',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'destination': 'destination',  # noqa: E501
        'funds_flow': 'funds_flow',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'merchant_id': 'merchant_id',  # noqa: E501
        'net_amount': 'net_amount',  # noqa: E501
        'payment_type': 'payment_type',  # noqa: E501
        'processor': 'processor',  # noqa: E501
        'status': 'status',  # noqa: E501
        'total_amount': 'total_amount',  # noqa: E501
        'total_fee': 'total_fee',  # noqa: E501
        'total_fees': 'total_fees',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Settlement - a model defined in OpenAPI

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
            type (str): Type of `Settlement`.. [optional]  # noqa: E501
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource the `Settlement` was created under.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): ID of the `Payment Instrument` where funds will be sent.. [optional]  # noqa: E501
            funds_flow (str, none_type): Details how funds will be dispersed in the `Funding Transfer` (usually **null**).. [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            merchant_id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            net_amount (int): The amount in cents that will be deposited into the merchant's bank account.. [optional]  # noqa: E501
            payment_type (str, none_type): The type of `Payment Instrument` used in the `Funding Transfer` (or the original payment).. [optional]  # noqa: E501
            processor (str): Name of the `Settlement` processor.. [optional]  # noqa: E501
            status (str): The status of the `Settlement`. Available values include:<ul><li>**PENDING**<li>**STAGED**<li>**AWAITING_APPROVAL**<li>**APPROVED**.</ul> Merchants only receive payouts when `Settlements` are **APPROVED**. For more information, see [Payouts](/guides/payouts/payouts/).. [optional]  # noqa: E501
            total_amount (int): Total amount of the `Settlement` (in cents).. [optional]  # noqa: E501
            total_fee (int): Sum of the fees in the `Settlement`.. [optional]  # noqa: E501
            total_fees (int): Sum of the fees in the `Settlement`.. [optional]  # noqa: E501
            links (SettlementLinks): [optional]  # noqa: E501
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
        """Settlement - a model defined in OpenAPI

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
            type (str): Type of `Settlement`.. [optional]  # noqa: E501
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource the `Settlement` was created under.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            destination (str, none_type): ID of the `Payment Instrument` where funds will be sent.. [optional]  # noqa: E501
            funds_flow (str, none_type): Details how funds will be dispersed in the `Funding Transfer` (usually **null**).. [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            merchant_id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            net_amount (int): The amount in cents that will be deposited into the merchant's bank account.. [optional]  # noqa: E501
            payment_type (str, none_type): The type of `Payment Instrument` used in the `Funding Transfer` (or the original payment).. [optional]  # noqa: E501
            processor (str): Name of the `Settlement` processor.. [optional]  # noqa: E501
            status (str): The status of the `Settlement`. Available values include:<ul><li>**PENDING**<li>**STAGED**<li>**AWAITING_APPROVAL**<li>**APPROVED**.</ul> Merchants only receive payouts when `Settlements` are **APPROVED**. For more information, see [Payouts](/guides/payouts/payouts/).. [optional]  # noqa: E501
            total_amount (int): Total amount of the `Settlement` (in cents).. [optional]  # noqa: E501
            total_fee (int): Sum of the fees in the `Settlement`.. [optional]  # noqa: E501
            total_fees (int): Sum of the fees in the `Settlement`.. [optional]  # noqa: E501
            links (SettlementLinks): [optional]  # noqa: E501
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
