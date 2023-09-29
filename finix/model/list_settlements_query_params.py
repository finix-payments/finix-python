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



class ListSettlementsQueryParams(ModelNormal):
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
            'created_at_gte': (str,),  # noqa: E501
            'created_at_lte': (str,),  # noqa: E501
            'amount': (int,),  # noqa: E501
            'amount_gt': (int,),  # noqa: E501
            'amount_gte': (int,),  # noqa: E501
            'amount_lt': (int,),  # noqa: E501
            'amount_lte': (int,),  # noqa: E501
            'status': (str,),  # noqa: E501
            'transfer_id': (str,),  # noqa: E501
            'funding_transfer_id': (str,),  # noqa: E501
            'accept': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'created_at_gte': 'created_at.gte',  # noqa: E501
        'created_at_lte': 'created_at.lte',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'amount_gt': 'amount.gt',  # noqa: E501
        'amount_gte': 'amount.gte',  # noqa: E501
        'amount_lt': 'amount.lt',  # noqa: E501
        'amount_lte': 'amount.lte',  # noqa: E501
        'status': 'status',  # noqa: E501
        'transfer_id': 'transfer_id',  # noqa: E501
        'funding_transfer_id': 'funding_transfer_id',  # noqa: E501
        'accept': 'Accept',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ListSettlementsQueryParams - a model defined in OpenAPI

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
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]  # noqa: E501
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]  # noqa: E501
            amount (int): Filter by an amount equal to the given value.. [optional]  # noqa: E501
            amount_gt (int): Filter by an amount greater than.. [optional]  # noqa: E501
            amount_gte (int): Filter by an amount greater than or equal.. [optional]  # noqa: E501
            amount_lt (int): Filter by an amount less than.. [optional]  # noqa: E501
            amount_lte (int): Filter by an amount less than or equal.. [optional]  # noqa: E501
            status (str): Filter by the status of the `Settlement`. Available values include:<ul><li>**PENDING**<li>**STAGED**<li>**AWAITING_APPROVAL**<li>**APPROVED**.</ul> Merchants only receive payouts when `Settlements` are **APPROVED**. For more information, see [Payouts](/docs/guides/payouts/payouts/).. [optional]  # noqa: E501
            transfer_id (str): Filter by a `transfer_id` a `Settlement` has accrued. Please note this filter is only available for non-versioned requests, or requests using `-H 'Finix-Version: 2018-01-01'`. We're actively working on making this filter available for later versions. For more details, see [Versioning](/guides/developers/versioning/).. [optional]  # noqa: E501
            funding_transfer_id (str): Filter by a `funding_transfer` a `Settlement` has created.. [optional]  # noqa: E501
            accept (str): Body Header. [optional]  # noqa: E501
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
        """ListSettlementsQueryParams - a model defined in OpenAPI

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
            created_at_gte (str): Filter where `created_at` is after the given date.. [optional]  # noqa: E501
            created_at_lte (str): Filter where `created_at` is before the given date.. [optional]  # noqa: E501
            amount (int): Filter by an amount equal to the given value.. [optional]  # noqa: E501
            amount_gt (int): Filter by an amount greater than.. [optional]  # noqa: E501
            amount_gte (int): Filter by an amount greater than or equal.. [optional]  # noqa: E501
            amount_lt (int): Filter by an amount less than.. [optional]  # noqa: E501
            amount_lte (int): Filter by an amount less than or equal.. [optional]  # noqa: E501
            status (str): Filter by the status of the `Settlement`. Available values include:<ul><li>**PENDING**<li>**STAGED**<li>**AWAITING_APPROVAL**<li>**APPROVED**.</ul> Merchants only receive payouts when `Settlements` are **APPROVED**. For more information, see [Payouts](/docs/guides/payouts/payouts/).. [optional]  # noqa: E501
            transfer_id (str): Filter by a `transfer_id` a `Settlement` has accrued. Please note this filter is only available for non-versioned requests, or requests using `-H 'Finix-Version: 2018-01-01'`. We're actively working on making this filter available for later versions. For more details, see [Versioning](/guides/developers/versioning/).. [optional]  # noqa: E501
            funding_transfer_id (str): Filter by a `funding_transfer` a `Settlement` has created.. [optional]  # noqa: E501
            accept (str): Body Header. [optional]  # noqa: E501
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
