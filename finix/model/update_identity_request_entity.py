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
    from finix.model.create_identity_request_entity_incorporation_date import CreateIdentityRequestEntityIncorporationDate
    from finix.model.create_identity_request_entity_personal_address import CreateIdentityRequestEntityPersonalAddress
    from finix.model.update_identity_request_entity_business_address import UpdateIdentityRequestEntityBusinessAddress
    from finix.model.update_identity_request_entity_dob import UpdateIdentityRequestEntityDob
    globals()['CreateIdentityRequestEntityIncorporationDate'] = CreateIdentityRequestEntityIncorporationDate
    globals()['CreateIdentityRequestEntityPersonalAddress'] = CreateIdentityRequestEntityPersonalAddress
    globals()['UpdateIdentityRequestEntityBusinessAddress'] = UpdateIdentityRequestEntityBusinessAddress
    globals()['UpdateIdentityRequestEntityDob'] = UpdateIdentityRequestEntityDob


class UpdateIdentityRequestEntity(ModelNormal):
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
        ('business_type',): {
            'INDIVIDUAL_SOLE_PROPRIETORSHIP': "INDIVIDUAL_SOLE_PROPRIETORSHIP",
            'CORPORATION': "CORPORATION",
            'LIMITED_LIABILITY_COMPANY': "LIMITED_LIABILITY_COMPANY",
            'PARTNERSHIP': "PARTNERSHIP",
            'ASSOCIATION_ESTATE_TRUST': "ASSOCIATION_ESTATE_TRUST",
            'TAX_EXEMPT_ORGANIZATION': "TAX_EXEMPT_ORGANIZATION",
            'INTERNATIONAL_ORGANIZATION': "INTERNATIONAL_ORGANIZATION",
            'GOVERNMENT_AGENCY': "GOVERNMENT_AGENCY",
        },
    }

    validations = {
        ('last_name',): {
            'min_length': 1,
        },
        ('first_name',): {
            'min_length': 1,
        },
        ('email',): {
            'min_length': 1,
        },
        ('phone',): {
            'min_length': 1,
        },
        ('default_statement_descriptor',): {
            'min_length': 1,
        },
        ('ownership_type',): {
            'min_length': 1,
        },
        ('title',): {
            'min_length': 1,
        },
        ('business_tax_id',): {
            'min_length': 1,
        },
        ('doing_business_as',): {
            'min_length': 1,
        },
        ('mcc',): {
            'min_length': 1,
        },
        ('business_name',): {
            'min_length': 1,
        },
        ('tax_id',): {
            'min_length': 1,
        },
        ('business_type',): {
            'min_length': 1,
        },
        ('business_phone',): {
            'min_length': 1,
        },
        ('url',): {
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
            'last_name': (str,),  # noqa: E501
            'first_name': (str,),  # noqa: E501
            'email': (str,),  # noqa: E501
            'phone': (str,),  # noqa: E501
            'max_transaction_amount': (int,),  # noqa: E501
            'has_accepted_credit_cards_previously': (bool,),  # noqa: E501
            'default_statement_descriptor': (str,),  # noqa: E501
            'personal_address': (CreateIdentityRequestEntityPersonalAddress,),  # noqa: E501
            'incorporation_date': (CreateIdentityRequestEntityIncorporationDate,),  # noqa: E501
            'business_address': (UpdateIdentityRequestEntityBusinessAddress,),  # noqa: E501
            'ownership_type': (str,),  # noqa: E501
            'title': (str,),  # noqa: E501
            'business_tax_id': (str,),  # noqa: E501
            'doing_business_as': (str,),  # noqa: E501
            'principal_percentage_ownership': (int,),  # noqa: E501
            'mcc': (str,),  # noqa: E501
            'business_name': (str, none_type,),  # noqa: E501
            'tax_id': (str,),  # noqa: E501
            'business_type': (str,),  # noqa: E501
            'business_phone': (str,),  # noqa: E501
            'dob': (UpdateIdentityRequestEntityDob,),  # noqa: E501
            'url': (str,),  # noqa: E501
            'annual_card_volume': (int,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'last_name': 'last_name',  # noqa: E501
        'first_name': 'first_name',  # noqa: E501
        'email': 'email',  # noqa: E501
        'phone': 'phone',  # noqa: E501
        'max_transaction_amount': 'max_transaction_amount',  # noqa: E501
        'has_accepted_credit_cards_previously': 'has_accepted_credit_cards_previously',  # noqa: E501
        'default_statement_descriptor': 'default_statement_descriptor',  # noqa: E501
        'personal_address': 'personal_address',  # noqa: E501
        'incorporation_date': 'incorporation_date',  # noqa: E501
        'business_address': 'business_address',  # noqa: E501
        'ownership_type': 'ownership_type',  # noqa: E501
        'title': 'title',  # noqa: E501
        'business_tax_id': 'business_tax_id',  # noqa: E501
        'doing_business_as': 'doing_business_as',  # noqa: E501
        'principal_percentage_ownership': 'principal_percentage_ownership',  # noqa: E501
        'mcc': 'mcc',  # noqa: E501
        'business_name': 'business_name',  # noqa: E501
        'tax_id': 'tax_id',  # noqa: E501
        'business_type': 'business_type',  # noqa: E501
        'business_phone': 'business_phone',  # noqa: E501
        'dob': 'dob',  # noqa: E501
        'url': 'url',  # noqa: E501
        'annual_card_volume': 'annual_card_volume',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, last_name, first_name, email, phone, *args, **kwargs):  # noqa: E501
        """UpdateIdentityRequestEntity - a model defined in OpenAPI

        Args:
            last_name (str): The legal last name of the merchant's control owner (max 20 characters).
            first_name (str): The legal first name of the merchant's control owner (max 20 characters).
            email (str): The email address of the principal control owner where they can be reached (max 100 characters).
            phone (str): The principal control owner's phone number (max 10 characters).

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
            max_transaction_amount (int): The maximum amount (in cents) that can be charged for a single transaction (max 12 characters).. [optional]  # noqa: E501
            has_accepted_credit_cards_previously (bool): Defaults to **false** if not passed.. [optional]  # noqa: E501
            default_statement_descriptor (str): The description of the merchant that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            personal_address (CreateIdentityRequestEntityPersonalAddress): [optional]  # noqa: E501
            incorporation_date (CreateIdentityRequestEntityIncorporationDate): [optional]  # noqa: E501
            business_address (UpdateIdentityRequestEntityBusinessAddress): [optional]  # noqa: E501
            ownership_type (str): Values can be either: <ul><li><strong>PUBLIC</strong> to indicate a publicly-traded company. <li><strong>PRIVATE</strong> for privately-held businesses.. [optional]  # noqa: E501
            title (str): The corporate title of the control owner (e.g. Chief Executive Officer, CFO, etc. Max 60 characters).. [optional]  # noqa: E501
            business_tax_id (str): Details if the `business_tax_id` was provided.. [optional]  # noqa: E501
            doing_business_as (str): Alternate names of the business. If there are no other names, pass the same value used for `business_name` (max 60 characters).. [optional]  # noqa: E501
            principal_percentage_ownership (int): Percentage of the company owned by the principal control owner (min 0; max 100).. [optional]  # noqa: E501
            mcc (str): The Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under.. [optional]  # noqa: E501
            business_name (str, none_type): Abbreviated names of the business. If there are no abbreviated name, leave this field blank.. [optional]  # noqa: E501
            tax_id (str): Details if the `tax_id` was provided.. [optional]  # noqa: E501
            business_type (str): Include the value that best applies to the merchant.. [optional]  # noqa: E501
            business_phone (str): Customer service phone number where the merchant can be reached (max 10 characters).. [optional]  # noqa: E501
            dob (UpdateIdentityRequestEntityDob): [optional]  # noqa: E501
            url (str): The URL of the merchant's public website.. [optional]  # noqa: E501
            annual_card_volume (int): The annual credit card sales (in cents) expected to be processed by this merchant (max 19 characters).. [optional]  # noqa: E501
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

        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
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
    def __init__(self, last_name, first_name, email, phone, *args, **kwargs):  # noqa: E501
        """UpdateIdentityRequestEntity - a model defined in OpenAPI

        Args:
            last_name (str): The legal last name of the merchant's control owner (max 20 characters).
            first_name (str): The legal first name of the merchant's control owner (max 20 characters).
            email (str): The email address of the principal control owner where they can be reached (max 100 characters).
            phone (str): The principal control owner's phone number (max 10 characters).

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
            max_transaction_amount (int): The maximum amount (in cents) that can be charged for a single transaction (max 12 characters).. [optional]  # noqa: E501
            has_accepted_credit_cards_previously (bool): Defaults to **false** if not passed.. [optional]  # noqa: E501
            default_statement_descriptor (str): The description of the merchant that appears on the buyer's bank or card statement.. [optional]  # noqa: E501
            personal_address (CreateIdentityRequestEntityPersonalAddress): [optional]  # noqa: E501
            incorporation_date (CreateIdentityRequestEntityIncorporationDate): [optional]  # noqa: E501
            business_address (UpdateIdentityRequestEntityBusinessAddress): [optional]  # noqa: E501
            ownership_type (str): Values can be either: <ul><li><strong>PUBLIC</strong> to indicate a publicly-traded company. <li><strong>PRIVATE</strong> for privately-held businesses.. [optional]  # noqa: E501
            title (str): The corporate title of the control owner (e.g. Chief Executive Officer, CFO, etc. Max 60 characters).. [optional]  # noqa: E501
            business_tax_id (str): Details if the `business_tax_id` was provided.. [optional]  # noqa: E501
            doing_business_as (str): Alternate names of the business. If there are no other names, pass the same value used for `business_name` (max 60 characters).. [optional]  # noqa: E501
            principal_percentage_ownership (int): Percentage of the company owned by the principal control owner (min 0; max 100).. [optional]  # noqa: E501
            mcc (str): The Merchant Category Code ([MCC](http://www.dm.usda.gov/procurement/card/card_x/mcc.pdf)) that this merchant will be classified under.. [optional]  # noqa: E501
            business_name (str, none_type): Abbreviated names of the business. If there are no abbreviated name, leave this field blank.. [optional]  # noqa: E501
            tax_id (str): Details if the `tax_id` was provided.. [optional]  # noqa: E501
            business_type (str): Include the value that best applies to the merchant.. [optional]  # noqa: E501
            business_phone (str): Customer service phone number where the merchant can be reached (max 10 characters).. [optional]  # noqa: E501
            dob (UpdateIdentityRequestEntityDob): [optional]  # noqa: E501
            url (str): The URL of the merchant's public website.. [optional]  # noqa: E501
            annual_card_volume (int): The annual credit card sales (in cents) expected to be processed by this merchant (max 19 characters).. [optional]  # noqa: E501
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

        self.last_name = last_name
        self.first_name = first_name
        self.email = email
        self.phone = phone
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
