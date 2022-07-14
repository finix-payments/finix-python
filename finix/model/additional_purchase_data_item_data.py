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



class AdditionalPurchaseDataItemData(ModelNormal):
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
            'amount_excluding_sales_tax': (int,),  # noqa: E501
            'amount_including_sales_tax': (int,),  # noqa: E501
            'commodity_code': (str,),  # noqa: E501
            'cost_per_unit': (int,),  # noqa: E501
            'item_description': (str,),  # noqa: E501
            'item_discount_amount': (int,),  # noqa: E501
            'merchant_product_code': (str,),  # noqa: E501
            'quantity': (int,),  # noqa: E501
            'unit_of_measure': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'amount_excluding_sales_tax': 'amount_excluding_sales_tax',  # noqa: E501
        'amount_including_sales_tax': 'amount_including_sales_tax',  # noqa: E501
        'commodity_code': 'commodity_code',  # noqa: E501
        'cost_per_unit': 'cost_per_unit',  # noqa: E501
        'item_description': 'item_description',  # noqa: E501
        'item_discount_amount': 'item_discount_amount',  # noqa: E501
        'merchant_product_code': 'merchant_product_code',  # noqa: E501
        'quantity': 'quantity',  # noqa: E501
        'unit_of_measure': 'unit_of_measure',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, amount_excluding_sales_tax, amount_including_sales_tax, commodity_code, cost_per_unit, item_description, item_discount_amount, merchant_product_code, quantity, unit_of_measure, *args, **kwargs):  # noqa: E501
        """AdditionalPurchaseDataItemData - a model defined in OpenAPI

        Args:
            amount_excluding_sales_tax (int): Total cost in cents of the line item excluding tax.
            amount_including_sales_tax (int): Total cost in cents of the line item including tax.
            commodity_code (str): A commodity code is a numeric code representing a particular product or service as defined by the National Institute of Governmental Purchasing. The code can be 3, 5, 7, or 11 digits in length. The longer the code the more granular the description of the product/service. (max 12 characters).
            cost_per_unit (int): The price in cents of one unit of the item purchased
            item_description (str): Required when `item_data` is supplied (max 25 characters)
            item_discount_amount (int): Item discount amount in cents 
            merchant_product_code (str): Merchant defined product code (max 12 characters).
            quantity (int): The number of items purchased. Must be greater than 0.
            unit_of_measure (str): The unit of measure of the purchased item (max 3 characters).

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

        self.amount_excluding_sales_tax = amount_excluding_sales_tax
        self.amount_including_sales_tax = amount_including_sales_tax
        self.commodity_code = commodity_code
        self.cost_per_unit = cost_per_unit
        self.item_description = item_description
        self.item_discount_amount = item_discount_amount
        self.merchant_product_code = merchant_product_code
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
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
    def __init__(self, amount_excluding_sales_tax, amount_including_sales_tax, commodity_code, cost_per_unit, item_description, item_discount_amount, merchant_product_code, quantity, unit_of_measure, *args, **kwargs):  # noqa: E501
        """AdditionalPurchaseDataItemData - a model defined in OpenAPI

        Args:
            amount_excluding_sales_tax (int): Total cost in cents of the line item excluding tax.
            amount_including_sales_tax (int): Total cost in cents of the line item including tax.
            commodity_code (str): A commodity code is a numeric code representing a particular product or service as defined by the National Institute of Governmental Purchasing. The code can be 3, 5, 7, or 11 digits in length. The longer the code the more granular the description of the product/service. (max 12 characters).
            cost_per_unit (int): The price in cents of one unit of the item purchased
            item_description (str): Required when `item_data` is supplied (max 25 characters)
            item_discount_amount (int): Item discount amount in cents 
            merchant_product_code (str): Merchant defined product code (max 12 characters).
            quantity (int): The number of items purchased. Must be greater than 0.
            unit_of_measure (str): The unit of measure of the purchased item (max 3 characters).

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

        self.amount_excluding_sales_tax = amount_excluding_sales_tax
        self.amount_including_sales_tax = amount_including_sales_tax
        self.commodity_code = commodity_code
        self.cost_per_unit = cost_per_unit
        self.item_description = item_description
        self.item_discount_amount = item_discount_amount
        self.merchant_product_code = merchant_product_code
        self.quantity = quantity
        self.unit_of_measure = unit_of_measure
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
