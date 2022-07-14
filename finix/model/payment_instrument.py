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
    from finix.model.address import Address
    from finix.model.country import Country
    from finix.model.currency import Currency
    from finix.model.payment_instrument_links import PaymentInstrumentLinks
    from finix.model.tags import Tags
    globals()['Address'] = Address
    globals()['Country'] = Country
    globals()['Currency'] = Currency
    globals()['PaymentInstrumentLinks'] = PaymentInstrumentLinks
    globals()['Tags'] = Tags


class PaymentInstrument(ModelNormal):
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
            'VIRTUAL': "VIRTUAL",
            'PAYMENT_CARD_PRESENT': "PAYMENT_CARD_PRESENT",
            'TOKEN': "TOKEN",
            'SWIPED_PAYMENT_CARD': "SWIPED_PAYMENT_CARD",
            'BANK_ACCOUNT': "BANK_ACCOUNT",
            'VANTIV_OMNI_TOKEN': "VANTIV_OMNI_TOKEN",
            'PAYMENT_CARD': "PAYMENT_CARD",
        },
        ('account_type',): {
            'CHECKING': "CHECKING",
            'SAVINGS': "SAVINGS",
            'CORPORATE': "CORPORATE",
            'CORP_SAVINGS': "CORP_SAVINGS",
        },
        ('instrument_type',): {
            'VIRTUAL': "VIRTUAL",
            'PAYMENT_CARD_PRESENT': "PAYMENT_CARD_PRESENT",
            'TOKEN': "TOKEN",
            'SWIPED_PAYMENT_CARD': "SWIPED_PAYMENT_CARD",
            'BANK_ACCOUNT': "BANK_ACCOUNT",
            'VANTIV_OMNI_TOKEN': "VANTIV_OMNI_TOKEN",
            'PAYMENT_CARD': "PAYMENT_CARD",
        },
        ('payload_type',): {
            'SOURCE': "SOURCE",
            'DESTINATION': "DESTINATION",
        },
        ('address_verification',): {
            'POSTAL_CODE_AND_STREET_MATCH': "POSTAL_CODE_AND_STREET_MATCH",
            'STREET_MATCH': "STREET_MATCH",
            'POSTAL_CODE_MATCH': "POSTAL_CODE_MATCH",
            'NO_ADDRESS': "NO_ADDRESS",
            'NO_MATCH': "NO_MATCH",
            'NOT_SUPPORTED': "NOT_SUPPORTED",
            'UNKNOWN': "UNKNOWN",
        },
        ('brand',): {
            'UNKNOWN': "UNKNOWN",
            'DINERS_CLUB_INTERNATIONAL': "DINERS_CLUB_INTERNATIONAL",
            'DANKORT': "DANKORT",
            'MIR': "MIR",
            'TROY': "TROY",
            'UATP': "UATP",
            'CHINA_T_UNION': "CHINA_T_UNION",
            'CHINA_UNION_PAY': "CHINA_UNION_PAY",
            'AMERICAN_EXPRESS': "AMERICAN_EXPRESS",
            'VERVE': "VERVE",
            'RUPAY': "RUPAY",
            'DISCOVER': "DISCOVER",
            'JCB': "JCB",
            'MASTERCARD': "MASTERCARD",
            'INTERPAYMENT': "INTERPAYMENT",
            'INSTAPAYMENT': "INSTAPAYMENT",
            'MAESTRO': "MAESTRO",
            'VISA': "VISA",
            'LANKAPAY': "LANKAPAY",
            'DINERS_CLUB': "DINERS_CLUB",
        },
        ('card_type',): {
            'UNKNOWN': "UNKNOWN",
            'PREPAID': "PREPAID",
            'CREDIT': "CREDIT",
            'DEBIT': "DEBIT",
            'FSA': "FSA",
        },
        ('security_code_verification',): {
            'MATCHED': "MATCHED",
            'UNKNOWN': "UNKNOWN",
            'UNMATCHED': "UNMATCHED",
        },
    }

    validations = {
        ('bank_code',): {
            'regex': {
                'pattern': r'^\d+$',  # noqa: E501
            },
        },
        ('masked_account_number',): {
            'regex': {
                'pattern': r'X+\d{4}',  # noqa: E501
            },
        },
        ('bin',): {
            'regex': {
                'pattern': r'^\d{6}$',  # noqa: E501
            },
        },
        ('expiration_month',): {
            'inclusive_maximum': 12,
            'inclusive_minimum': 1,
        },
        ('expiration_year',): {
            'inclusive_minimum': 1,
        },
        ('last_four',): {
            'regex': {
                'pattern': r'^\d{4}$',  # noqa: E501
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
            'account_type': (str,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'bank_code': (str,),  # noqa: E501
            'country': (Country,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'fingerprint': (str,),  # noqa: E501
            'identity': (str, none_type,),  # noqa: E501
            'instrument_type': (str,),  # noqa: E501
            'masked_account_number': (str, none_type,),  # noqa: E501
            'name': (str, none_type,),  # noqa: E501
            'payload_type': (str,),  # noqa: E501
            'links': (PaymentInstrumentLinks,),  # noqa: E501
            'address': (Address,),  # noqa: E501
            'address_verification': (str,),  # noqa: E501
            'bin': (str,),  # noqa: E501
            'brand': (str,),  # noqa: E501
            'card_name': (str, none_type,),  # noqa: E501
            'card_type': (str,),  # noqa: E501
            'expiration_month': (int,),  # noqa: E501
            'expiration_year': (int,),  # noqa: E501
            'fast_funds_indicator': (str,),  # noqa: E501
            'last_four': (str,),  # noqa: E501
            'online_gambing_block_indicator': (str,),  # noqa: E501
            'push_funds_block_indicator': (str,),  # noqa: E501
            'security_code_verification': (str,),  # noqa: E501
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
        'account_type': 'account_type',  # noqa: E501
        'application': 'application',  # noqa: E501
        'bank_code': 'bank_code',  # noqa: E501
        'country': 'country',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'fingerprint': 'fingerprint',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'instrument_type': 'instrument_type',  # noqa: E501
        'masked_account_number': 'masked_account_number',  # noqa: E501
        'name': 'name',  # noqa: E501
        'payload_type': 'payload_type',  # noqa: E501
        'links': '_links',  # noqa: E501
        'address': 'address',  # noqa: E501
        'address_verification': 'address_verification',  # noqa: E501
        'bin': 'bin',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'card_name': 'card_name',  # noqa: E501
        'card_type': 'card_type',  # noqa: E501
        'expiration_month': 'expiration_month',  # noqa: E501
        'expiration_year': 'expiration_year',  # noqa: E501
        'fast_funds_indicator': 'fast_funds_indicator',  # noqa: E501
        'last_four': 'last_four',  # noqa: E501
        'online_gambing_block_indicator': 'online_gambing_block_indicator',  # noqa: E501
        'push_funds_block_indicator': 'push_funds_block_indicator',  # noqa: E501
        'security_code_verification': 'security_code_verification',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """PaymentInstrument - a model defined in OpenAPI

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
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            account_type (str): Details what kind of **BANK_ACCOUNT** is being used.. [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            country (Country): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            fingerprint (str): Unique ID that represents the tokenized card data.. [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            instrument_type (str): The type of `Payment Instrument`.. [optional]  # noqa: E501
            masked_account_number (str, none_type): The last 4 digits of the account number used to create the `Payment Instrument`.. [optional]  # noqa: E501
            name (str, none_type): The name of the bank account or card owner.. [optional]  # noqa: E501
            payload_type (str): [optional]  # noqa: E501
            links (PaymentInstrumentLinks): [optional]  # noqa: E501
            address (Address): [optional]  # noqa: E501
            address_verification (str): Additional address information that’s required to verify the identity of the merchant.. [optional]  # noqa: E501
            bin (str): Bank Identification number for the `Payment Instrument`.. [optional]  # noqa: E501
            brand (str): The `brand` of the card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            card_name (str, none_type): A custom name you can include to identify the card being used (e.g. **Business Card**).. [optional]  # noqa: E501
            card_type (str): The type of card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            expiration_month (int): Expiration month (e.g. 12 for December).. [optional]  # noqa: E501
            expiration_year (int): 4-digit expiration year.. [optional]  # noqa: E501
            fast_funds_indicator (str): Details if Fast Funds is enabled for the card.. [optional]  # noqa: E501
            last_four (str): Last four digits of the card or bank account number.. [optional]  # noqa: E501
            online_gambing_block_indicator (str): Detailes if the card is enabled to receive push-payments for online gambling payouts.. [optional]  # noqa: E501
            push_funds_block_indicator (str): Details if the card is enabled to receive push-to-card disbursements.. [optional]  # noqa: E501
            security_code_verification (str): Details the results of the Card Verification Code check.. [optional]  # noqa: E501
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
        """PaymentInstrument - a model defined in OpenAPI

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
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
            id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            account_type (str): Details what kind of **BANK_ACCOUNT** is being used.. [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            country (Country): [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            fingerprint (str): Unique ID that represents the tokenized card data.. [optional]  # noqa: E501
            identity (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            instrument_type (str): The type of `Payment Instrument`.. [optional]  # noqa: E501
            masked_account_number (str, none_type): The last 4 digits of the account number used to create the `Payment Instrument`.. [optional]  # noqa: E501
            name (str, none_type): The name of the bank account or card owner.. [optional]  # noqa: E501
            payload_type (str): [optional]  # noqa: E501
            links (PaymentInstrumentLinks): [optional]  # noqa: E501
            address (Address): [optional]  # noqa: E501
            address_verification (str): Additional address information that’s required to verify the identity of the merchant.. [optional]  # noqa: E501
            bin (str): Bank Identification number for the `Payment Instrument`.. [optional]  # noqa: E501
            brand (str): The `brand` of the card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            card_name (str, none_type): A custom name you can include to identify the card being used (e.g. **Business Card**).. [optional]  # noqa: E501
            card_type (str): The type of card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            expiration_month (int): Expiration month (e.g. 12 for December).. [optional]  # noqa: E501
            expiration_year (int): 4-digit expiration year.. [optional]  # noqa: E501
            fast_funds_indicator (str): Details if Fast Funds is enabled for the card.. [optional]  # noqa: E501
            last_four (str): Last four digits of the card or bank account number.. [optional]  # noqa: E501
            online_gambing_block_indicator (str): Detailes if the card is enabled to receive push-payments for online gambling payouts.. [optional]  # noqa: E501
            push_funds_block_indicator (str): Details if the card is enabled to receive push-to-card disbursements.. [optional]  # noqa: E501
            security_code_verification (str): Details the results of the Card Verification Code check.. [optional]  # noqa: E501
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
