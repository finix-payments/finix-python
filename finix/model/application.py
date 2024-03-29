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
    from finix.model.application_links import ApplicationLinks
    from finix.model.tags import Tags
    globals()['ApplicationLinks'] = ApplicationLinks
    globals()['Tags'] = Tags


class Application(ModelNormal):
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
        ('fee_ready_to_settle_upon',): {
            'None': None,
            'RECONCILIATION': "RECONCILIATION",
            'SUCCESSFUL_CAPTURE': "SUCCESSFUL_CAPTURE",
        },
        ('ready_to_settle_upon',): {
            'None': None,
            'RECONCILIATION': "RECONCILIATION",
            'SUCCESSFUL_CAPTURE': "SUCCESSFUL_CAPTURE",
        },
        ('settlement_funding_identifier',): {
            'UNSET': "UNSET",
            'MID_AND_DATE': "MID_AND_DATE",
            'MID_AND_MERCHANT_NAME': "MID_AND_MERCHANT_NAME",
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
            'id': (str,),  # noqa: E501
            'created_at': (datetime,),  # noqa: E501
            'updated_at': (datetime,),  # noqa: E501
            'card_cvv_required': (bool,),  # noqa: E501
            'card_expiration_date_required': (bool,),  # noqa: E501
            'creating_transfer_from_report_enabled': (bool,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'fee_ready_to_settle_upon': (str, none_type,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'owner': (str,),  # noqa: E501
            'processing_enabled': (bool,),  # noqa: E501
            'ready_to_settle_upon': (str, none_type,),  # noqa: E501
            'settlement_enabled': (bool,),  # noqa: E501
            'settlement_funding_identifier': (str,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'links': (ApplicationLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'card_cvv_required': 'card_cvv_required',  # noqa: E501
        'card_expiration_date_required': 'card_expiration_date_required',  # noqa: E501
        'creating_transfer_from_report_enabled': 'creating_transfer_from_report_enabled',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'fee_ready_to_settle_upon': 'fee_ready_to_settle_upon',  # noqa: E501
        'name': 'name',  # noqa: E501
        'owner': 'owner',  # noqa: E501
        'processing_enabled': 'processing_enabled',  # noqa: E501
        'ready_to_settle_upon': 'ready_to_settle_upon',  # noqa: E501
        'settlement_enabled': 'settlement_enabled',  # noqa: E501
        'settlement_funding_identifier': 'settlement_funding_identifier',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Application - a model defined in OpenAPI

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
            id (str): ID of the `Application` resource.. [optional]  # noqa: E501
            created_at (datetime): Point in time when this object was created.. [optional]  # noqa: E501
            updated_at (datetime): Point in time when this object was most recently updated.. [optional]  # noqa: E501
            card_cvv_required (bool): Details if the `Application` requires CVV code.. [optional]  # noqa: E501
            card_expiration_date_required (bool): Details if the `Application` requires the card's expiration date.. [optional]  # noqa: E501
            creating_transfer_from_report_enabled (bool): Details if the `Application` is automatically set to create `Transfers` once settlement reports get generated.. [optional]  # noqa: E501
            enabled (bool): Details if the `Application` is enabled and active. Set to **false** to disable the `Application`.. [optional]  # noqa: E501
            fee_ready_to_settle_upon (str, none_type): Details when the `fees` of `Authroizations` submitted under the `Application` will be ready to settle.. [optional]  # noqa: E501
            name (str): The name of the `Application`.. [optional]  # noqa: E501
            owner (str): ID of the `Identity` resource that created the `Application`.. [optional]  # noqa: E501
            processing_enabled (bool): Details if transaction processing is enabled for the `Application`. . [optional]  # noqa: E501
            ready_to_settle_upon (str, none_type): Details when transactions submitted under the `Application` will be ready to settle.. [optional]  # noqa: E501
            settlement_enabled (bool): Details if settlement processing is enabled for the `Application`. . [optional]  # noqa: E501
            settlement_funding_identifier (str): Includes additional information (like the MID or `Merchant` name) when submitting funding `Transfers` to processors. - **UNSET**: No additional details get provided to the processor. - **MID_AND_DATE**: The `MID` of the `Merchant` and the date the funding `Transfer` was submitted (Date is in UTC). e.g **MID:12345678-20220225** - **MID_AND_MERCHANT_NAME**: The `MID` of the `Merchant` and the `Merchant#name` (white spaces will be removed). e.g. **MID:12345678-NameOfMerchant**  These details appear alongside the seller's payout in their bank account as a description of the deposit.. [optional] if omitted the server will use the default value of "UNSET"  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            links (ApplicationLinks): [optional]  # noqa: E501
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
        """Application - a model defined in OpenAPI

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
            id (str): ID of the `Application` resource.. [optional]  # noqa: E501
            created_at (datetime): Point in time when this object was created.. [optional]  # noqa: E501
            updated_at (datetime): Point in time when this object was most recently updated.. [optional]  # noqa: E501
            card_cvv_required (bool): Details if the `Application` requires CVV code.. [optional]  # noqa: E501
            card_expiration_date_required (bool): Details if the `Application` requires the card's expiration date.. [optional]  # noqa: E501
            creating_transfer_from_report_enabled (bool): Details if the `Application` is automatically set to create `Transfers` once settlement reports get generated.. [optional]  # noqa: E501
            enabled (bool): Details if the `Application` is enabled and active. Set to **false** to disable the `Application`.. [optional]  # noqa: E501
            fee_ready_to_settle_upon (str, none_type): Details when the `fees` of `Authroizations` submitted under the `Application` will be ready to settle.. [optional]  # noqa: E501
            name (str): The name of the `Application`.. [optional]  # noqa: E501
            owner (str): ID of the `Identity` resource that created the `Application`.. [optional]  # noqa: E501
            processing_enabled (bool): Details if transaction processing is enabled for the `Application`. . [optional]  # noqa: E501
            ready_to_settle_upon (str, none_type): Details when transactions submitted under the `Application` will be ready to settle.. [optional]  # noqa: E501
            settlement_enabled (bool): Details if settlement processing is enabled for the `Application`. . [optional]  # noqa: E501
            settlement_funding_identifier (str): Includes additional information (like the MID or `Merchant` name) when submitting funding `Transfers` to processors. - **UNSET**: No additional details get provided to the processor. - **MID_AND_DATE**: The `MID` of the `Merchant` and the date the funding `Transfer` was submitted (Date is in UTC). e.g **MID:12345678-20220225** - **MID_AND_MERCHANT_NAME**: The `MID` of the `Merchant` and the `Merchant#name` (white spaces will be removed). e.g. **MID:12345678-NameOfMerchant**  These details appear alongside the seller's payout in their bank account as a description of the deposit.. [optional] if omitted the server will use the default value of "UNSET"  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            links (ApplicationLinks): [optional]  # noqa: E501
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
