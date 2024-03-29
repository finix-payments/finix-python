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
    from finix.model.additional_purchase_data_order_date import AdditionalPurchaseDataOrderDate
    from finix.model.l3_additional_purchase_data_item_data import L3AdditionalPurchaseDataItemData
    globals()['AdditionalPurchaseDataOrderDate'] = AdditionalPurchaseDataOrderDate
    globals()['L3AdditionalPurchaseDataItemData'] = L3AdditionalPurchaseDataItemData


class L3AdditionalPurchaseData(ModelNormal):
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
        ('customer_reference_number',): {
            'max_length': 17,
        },
        ('destination_postal_code',): {
            'max_length': 10,
        },
        ('invoice_reference_number',): {
            'max_length': 15,
        },
        ('ship_from_postal_code',): {
            'max_length': 10,
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
            'customer_reference_number': (str,),  # noqa: E501
            'customs_duty_amount': (int,),  # noqa: E501
            'discount_amount': (int,),  # noqa: E501
            'item_data': ([L3AdditionalPurchaseDataItemData],),  # noqa: E501
            'sales_tax': (int,),  # noqa: E501
            'shipping_amount': (int,),  # noqa: E501
            'destination_country_code': (str,),  # noqa: E501
            'destination_postal_code': (str,),  # noqa: E501
            'invoice_reference_number': (str,),  # noqa: E501
            'order_date': (AdditionalPurchaseDataOrderDate,),  # noqa: E501
            'ship_from_postal_code': (str,),  # noqa: E501
            'tax_exempt': (bool,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'customer_reference_number': 'customer_reference_number',  # noqa: E501
        'customs_duty_amount': 'customs_duty_amount',  # noqa: E501
        'discount_amount': 'discount_amount',  # noqa: E501
        'item_data': 'item_data',  # noqa: E501
        'sales_tax': 'sales_tax',  # noqa: E501
        'shipping_amount': 'shipping_amount',  # noqa: E501
        'destination_country_code': 'destination_country_code',  # noqa: E501
        'destination_postal_code': 'destination_postal_code',  # noqa: E501
        'invoice_reference_number': 'invoice_reference_number',  # noqa: E501
        'order_date': 'order_date',  # noqa: E501
        'ship_from_postal_code': 'ship_from_postal_code',  # noqa: E501
        'tax_exempt': 'tax_exempt',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, customer_reference_number, customs_duty_amount, discount_amount, item_data, sales_tax, shipping_amount, *args, **kwargs):  # noqa: E501
        """L3AdditionalPurchaseData - a model defined in OpenAPI

        Args:
            customer_reference_number (str): The customer reference for the purchase (max 17 characters).
            customs_duty_amount (int): The duty in cents on the total purchase amount for the order
            discount_amount (int): The amount in cents of the discount for the order.
            item_data ([L3AdditionalPurchaseDataItemData]): Additional information about the transaction. Used for Level 2 and Level 3 Processing.
            sales_tax (int): - Total aggregate tax amount in cents for the entire purchase. Field is automatically calculated if you pass in the itemized tax amounts.  - For non-taxable transactions either set `sales_tax` to 0 or omit from payload and also set `tax_exempt` to **True**. - Request must align so `amount_excluding_sales_tax` + `sales_tax` = `amount_including_sales_tax`.e**.
            shipping_amount (int): The shipping cost in cents for the order. 

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
            destination_country_code (str): The ISO country code of the order destination.. [optional]  # noqa: E501
            destination_postal_code (str): The postal code of the order destination (10 characters). [optional]  # noqa: E501
            invoice_reference_number (str): The order's invoice number (max 15 characters). [optional]  # noqa: E501
            order_date (AdditionalPurchaseDataOrderDate): [optional]  # noqa: E501
            ship_from_postal_code (str): The postal code from where order is shipped (10 characters). [optional]  # noqa: E501
            tax_exempt (bool): - For tax exempt purchases set to **True**. - If set to **True**, request can't include `sales_tax`.. [optional]  # noqa: E501
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

        self.customer_reference_number = customer_reference_number
        self.customs_duty_amount = customs_duty_amount
        self.discount_amount = discount_amount
        self.item_data = item_data
        self.sales_tax = sales_tax
        self.shipping_amount = shipping_amount
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
    def __init__(self, customer_reference_number, customs_duty_amount, discount_amount, item_data, sales_tax, shipping_amount, *args, **kwargs):  # noqa: E501
        """L3AdditionalPurchaseData - a model defined in OpenAPI

        Args:
            customer_reference_number (str): The customer reference for the purchase (max 17 characters).
            customs_duty_amount (int): The duty in cents on the total purchase amount for the order
            discount_amount (int): The amount in cents of the discount for the order.
            item_data ([L3AdditionalPurchaseDataItemData]): Additional information about the transaction. Used for Level 2 and Level 3 Processing.
            sales_tax (int): - Total aggregate tax amount in cents for the entire purchase. Field is automatically calculated if you pass in the itemized tax amounts.  - For non-taxable transactions either set `sales_tax` to 0 or omit from payload and also set `tax_exempt` to **True**. - Request must align so `amount_excluding_sales_tax` + `sales_tax` = `amount_including_sales_tax`.e**.
            shipping_amount (int): The shipping cost in cents for the order. 

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
            destination_country_code (str): The ISO country code of the order destination.. [optional]  # noqa: E501
            destination_postal_code (str): The postal code of the order destination (10 characters). [optional]  # noqa: E501
            invoice_reference_number (str): The order's invoice number (max 15 characters). [optional]  # noqa: E501
            order_date (AdditionalPurchaseDataOrderDate): [optional]  # noqa: E501
            ship_from_postal_code (str): The postal code from where order is shipped (10 characters). [optional]  # noqa: E501
            tax_exempt (bool): - For tax exempt purchases set to **True**. - If set to **True**, request can't include `sales_tax`.. [optional]  # noqa: E501
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

        self.customer_reference_number = customer_reference_number
        self.customs_duty_amount = customs_duty_amount
        self.discount_amount = discount_amount
        self.item_data = item_data
        self.sales_tax = sales_tax
        self.shipping_amount = shipping_amount
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
