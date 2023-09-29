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
    Address
    Country
    Currency
    PaymentInstrumentLinks


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
        ('address_verification',): {
            '&#39;NOT_SUPPORTED&#39;': 'NOT_SUPPORTED',
            '&#39;NO_ADDRESS&#39;': 'NO_ADDRESS',
            '&#39;NO_MATCH&#39;': 'NO_MATCH',
            '&#39;POSTAL_CODE_AND_STREET_MATCH&#39;': 'POSTAL_CODE_AND_STREET_MATCH',
            '&#39;POSTAL_CODE_MATCH&#39;': 'POSTAL_CODE_MATCH',
            '&#39;STREET_MATCH&#39;': 'STREET_MATCH',
            '&#39;UNKNOWN&#39;': 'UNKNOWN',
        },
        ('brand',): {
            '&#39;AMERICAN_EXPRESS&#39;': 'AMERICAN_EXPRESS',
            '&#39;CHINA_T_UNION&#39;': 'CHINA_T_UNION',
            '&#39;CHINA_UNION_PAY&#39;': 'CHINA_UNION_PAY',
            '&#39;DANKORT&#39;': 'DANKORT',
            '&#39;DINERS_CLUB&#39;': 'DINERS_CLUB',
            '&#39;DINERS_CLUB_INTERNATIONAL&#39;': 'DINERS_CLUB_INTERNATIONAL',
            '&#39;DISCOVER&#39;': 'DISCOVER',
            '&#39;INSTAPAYMENT&#39;': 'INSTAPAYMENT',
            '&#39;INTERPAYMENT&#39;': 'INTERPAYMENT',
            '&#39;JCB&#39;': 'JCB',
            '&#39;LANKAPAY&#39;': 'LANKAPAY',
            '&#39;MAESTRO&#39;': 'MAESTRO',
            '&#39;MASTERCARD&#39;': 'MASTERCARD',
            '&#39;MIR&#39;': 'MIR',
            '&#39;RUPAY&#39;': 'RUPAY',
            '&#39;TROY&#39;': 'TROY',
            '&#39;UATP&#39;': 'UATP',
            '&#39;UNKNOWN&#39;': 'UNKNOWN',
            '&#39;VERVE&#39;': 'VERVE',
            '&#39;VISA&#39;': 'VISA',
        },
        ('card_type',): {
            '&#39;CREDIT&#39;': 'CREDIT',
            '&#39;DEBIT&#39;': 'DEBIT',
            '&#39;HSA_FSA&#39;': 'HSA_FSA',
            '&#39;NON_RELOADABLE_PREPAID&#39;': 'NON_RELOADABLE_PREPAID',
            '&#39;RELOADABLE_PREPAID&#39;': 'RELOADABLE_PREPAID',
            '&#39;UNKNOWN&#39;': 'UNKNOWN',
        },
        ('instrument_type',): {
            '&#39;APPLE_PAY&#39;': 'APPLE_PAY',
            '&#39;BANK_ACCOUNT&#39;': 'BANK_ACCOUNT',
            '&#39;GOOGLE_PAY&#39;': 'GOOGLE_PAY',
            '&#39;PAYMENT_CARD&#39;': 'PAYMENT_CARD',
            '&#39;PAYMENT_CARD_PRESENT&#39;': 'PAYMENT_CARD_PRESENT',
            '&#39;SWIPED_PAYMENT_CARD&#39;': 'SWIPED_PAYMENT_CARD',
            '&#39;TOKEN&#39;': 'TOKEN',
            '&#39;VANTIV_OMNI_TOKEN&#39;': 'VANTIV_OMNI_TOKEN',
            '&#39;VIRTUAL&#39;': 'VIRTUAL',
        },
        ('issuer_country',): {
            '&#39;NON_USA&#39;': 'NON_USA',
            '&#39;UNKNOWN&#39;': 'UNKNOWN',
            '&#39;USA&#39;': 'USA',
        },
        ('payload_type',): {
            '&#39;DESTINATION&#39;': 'DESTINATION',
            '&#39;SOURCE&#39;': 'SOURCE',
        },
        ('security_code_verification',): {
            '&#39;MATCHED&#39;': 'MATCHED',
            '&#39;UNKNOWN&#39;': 'UNKNOWN',
            '&#39;UNMATCHED&#39;': 'UNMATCHED',
        },
        ('type',): {
            '&#39;APPLE_PAY&#39;': 'APPLE_PAY',
            '&#39;BANK_ACCOUNT&#39;': 'BANK_ACCOUNT',
            '&#39;GOOGLE_PAY&#39;': 'GOOGLE_PAY',
            '&#39;PAYMENT_CARD&#39;': 'PAYMENT_CARD',
            '&#39;PAYMENT_CARD_PRESENT&#39;': 'PAYMENT_CARD_PRESENT',
            '&#39;SWIPED_PAYMENT_CARD&#39;': 'SWIPED_PAYMENT_CARD',
            '&#39;TOKEN&#39;': 'TOKEN',
            '&#39;VANTIV_OMNI_TOKEN&#39;': 'VANTIV_OMNI_TOKEN',
            '&#39;VIRTUAL&#39;': 'VIRTUAL',
        },
        ('account_type',): {
            '&#39;CHECKING&#39;': 'CHECKING',
            '&#39;SAVINGS&#39;': 'SAVINGS',
        },
        ('bank_account_validation_check',): {
            '&#39;INCONCLUSIVE&#39;': 'INCONCLUSIVE',
            '&#39;INVALID&#39;': 'INVALID',
            '&#39;NOT_ATTEMPTED&#39;': 'NOT_ATTEMPTED',
            '&#39;VALID&#39;': 'VALID',
        },
    }

    validations = {
        ('expiration_month',): {
            'inclusive_maximum': 12,
            'inclusive_minimum': 1,
        },
        ('expiration_year',): {
            'inclusive_minimum': 1,
        },
    }

    additional_properties_type = None

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
            'address': (Address,),  # noqa: E501
            'address_verification': (str,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'bin': (str,),  # noqa: E501
            'brand': (str,),  # noqa: E501
            'card_name': (str,),  # noqa: E501
            'card_type': (str,),  # noqa: E501
            'currency': (Currency,),  # noqa: E501
            'enabled': (bool,),  # noqa: E501
            'expiration_month': (int,),  # noqa: E501
            'expiration_year': (int,),  # noqa: E501
            'fast_funds_indicator': (str,),  # noqa: E501
            'fingerprint': (str,),  # noqa: E501
            'identity': (str,),  # noqa: E501
            'instrument_type': (str,),  # noqa: E501
            'issuer_country': (str,),  # noqa: E501
            'last_four': (str,),  # noqa: E501
            'name': (str,),  # noqa: E501
            'online_gambing_block_indicator': (str,),  # noqa: E501
            'payload_type': (str,),  # noqa: E501
            'push_funds_block_indicator': (str,),  # noqa: E501
            'security_code_verification': (str,),  # noqa: E501
            'tags': (object,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'links': (PaymentInstrumentLinks,),  # noqa: E501
            'account_type': (str,),  # noqa: E501
            'bank_account_validation_check': (str,),  # noqa: E501
            'bank_code': (str,),  # noqa: E501
            'country': (Country,),  # noqa: E501
            'masked_account_number': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'address': 'address',  # noqa: E501
        'address_verification': 'address_verification',  # noqa: E501
        'application': 'application',  # noqa: E501
        'bin': 'bin',  # noqa: E501
        'brand': 'brand',  # noqa: E501
        'card_name': 'card_name',  # noqa: E501
        'card_type': 'card_type',  # noqa: E501
        'currency': 'currency',  # noqa: E501
        'enabled': 'enabled',  # noqa: E501
        'expiration_month': 'expiration_month',  # noqa: E501
        'expiration_year': 'expiration_year',  # noqa: E501
        'fast_funds_indicator': 'fast_funds_indicator',  # noqa: E501
        'fingerprint': 'fingerprint',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'instrument_type': 'instrument_type',  # noqa: E501
        'issuer_country': 'issuer_country',  # noqa: E501
        'last_four': 'last_four',  # noqa: E501
        'name': 'name',  # noqa: E501
        'online_gambing_block_indicator': 'online_gambing_block_indicator',  # noqa: E501
        'payload_type': 'payload_type',  # noqa: E501
        'push_funds_block_indicator': 'push_funds_block_indicator',  # noqa: E501
        'security_code_verification': 'security_code_verification',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'type': 'type',  # noqa: E501
        'links': '_links',  # noqa: E501
        'account_type': 'account_type',  # noqa: E501
        'bank_account_validation_check': 'bank_account_validation_check',  # noqa: E501
        'bank_code': 'bank_code',  # noqa: E501
        'country': 'country',  # noqa: E501
        'masked_account_number': 'masked_account_number',  # noqa: E501
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
            id (str): The ID of the `Payment Instrument`.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            address (Address): [optional]  # noqa: E501
            address_verification (str): Additional address information that’s required to verify the identity of the merchant.. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource the `Payment Instrument` was created under.. [optional]  # noqa: E501
            bin (str): Bank Identification number for the `Payment Instrument`.. [optional]  # noqa: E501
            brand (str): The `brand` of the card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            card_name (str): A custom name you can include to identify the card being used (e.g. **Business Card**).. [optional]  # noqa: E501
            card_type (str): The type of payment card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            enabled (bool): Details if the `Payment Instrument` resource is enabled. Default value is **true**; set to **false** to disable the `Payment Instrument`.. [optional]  # noqa: E501
            expiration_month (int): Expiration month (e.g. 12 for December).. [optional]  # noqa: E501
            expiration_year (int): 4-digit expiration year.. [optional]  # noqa: E501
            fast_funds_indicator (str): Details if Fast Funds is enabled for the card.. [optional]  # noqa: E501
            fingerprint (str): Unique ID that represents the tokenized card data.. [optional]  # noqa: E501
            identity (str): The ID of the `Identity` used to create the `Payment Instrument` resource.. [optional]  # noqa: E501
            instrument_type (str): The type of `Payment Instrument`.. [optional]  # noqa: E501
            issuer_country (str): Details what country the card was issued in:<li><strong>USA</strong>: The card was issued inside the United States.<li><strong>NON_USA</strong>: The card was issued outside of the United States.<li><strong>UNKNOWN</strong>: Processor did not return an issuer country for this particular BIN.. [optional]  # noqa: E501
            last_four (str): Last four digits of the card or bank account number.. [optional]  # noqa: E501
            name (str): The name of the bank account or card owner.. [optional]  # noqa: E501
            online_gambing_block_indicator (str): Detailes if the card is enabled to receive push-payments for online gambling payouts.. [optional]  # noqa: E501
            payload_type (str): [optional]  # noqa: E501
            push_funds_block_indicator (str): Details if the card is enabled to receive push-to-card disbursements.. [optional]  # noqa: E501
            security_code_verification (str): Details the results of the Card Verification Code check.. [optional]  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
            links (PaymentInstrumentLinks): [optional]  # noqa: E501
            account_type (str): Details what kind of **BANK_ACCOUNT** is being used.. [optional]  # noqa: E501
            bank_account_validation_check (str): Details the results of the bank account validation check if `attempt_bank_account_validation_check` is set to **true** or the `Payment Instrument` gets used to create a `Transfer`. - **INCONCLUSIVE**: A verification check was performed, but the bank account couldn't be found or verified with the issuing bank. Reach out to the buyer to verify the details collected or request another method of payment,  - **INVALID**: The `Payment Instrument` was used in transactions that returned one of the following ACH errors: <ul><li>**Account Does Not Allow ACH Transactions**</li><li>**Account is Closed**</li><li>**Account Funds are Frozen**</li><li>**Deceased Account Holder**</li><li>**Invalid Account Number**</li><li>**Invalid Routing Number**</li><li>**No Account on File**</li></ul>. For more details on the different ACH failure codes, see [ACH Direct Debit.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/#failed-ach-direct-debits) - **NOT_ATTEMPTED**: A verification check wasn't performed and the `Payment Instrument` hasn't been used to create a `Transfer` or `Authorization`. - **VALID**: The bank account was verified. The `Payment Instrument` can be used to create [ACH Direct Debits.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/#failed-ach-direct-debits). [optional] if omitted the server will use the default value of 'NOT_ATTEMPTED'  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            country (Country): [optional]  # noqa: E501
            masked_account_number (str): The last 4 digits of the account number used to create the `Payment Instrument`.. [optional]  # noqa: E501
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
            id (str): The ID of the `Payment Instrument`.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            address (Address): [optional]  # noqa: E501
            address_verification (str): Additional address information that’s required to verify the identity of the merchant.. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource the `Payment Instrument` was created under.. [optional]  # noqa: E501
            bin (str): Bank Identification number for the `Payment Instrument`.. [optional]  # noqa: E501
            brand (str): The `brand` of the card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            card_name (str): A custom name you can include to identify the card being used (e.g. **Business Card**).. [optional]  # noqa: E501
            card_type (str): The type of payment card saved in the `Payment Instrument`.. [optional]  # noqa: E501
            currency (Currency): [optional]  # noqa: E501
            enabled (bool): Details if the `Payment Instrument` resource is enabled. Default value is **true**; set to **false** to disable the `Payment Instrument`.. [optional]  # noqa: E501
            expiration_month (int): Expiration month (e.g. 12 for December).. [optional]  # noqa: E501
            expiration_year (int): 4-digit expiration year.. [optional]  # noqa: E501
            fast_funds_indicator (str): Details if Fast Funds is enabled for the card.. [optional]  # noqa: E501
            fingerprint (str): Unique ID that represents the tokenized card data.. [optional]  # noqa: E501
            identity (str): The ID of the `Identity` used to create the `Payment Instrument` resource.. [optional]  # noqa: E501
            instrument_type (str): The type of `Payment Instrument`.. [optional]  # noqa: E501
            issuer_country (str): Details what country the card was issued in:<li><strong>USA</strong>: The card was issued inside the United States.<li><strong>NON_USA</strong>: The card was issued outside of the United States.<li><strong>UNKNOWN</strong>: Processor did not return an issuer country for this particular BIN.. [optional]  # noqa: E501
            last_four (str): Last four digits of the card or bank account number.. [optional]  # noqa: E501
            name (str): The name of the bank account or card owner.. [optional]  # noqa: E501
            online_gambing_block_indicator (str): Detailes if the card is enabled to receive push-payments for online gambling payouts.. [optional]  # noqa: E501
            payload_type (str): [optional]  # noqa: E501
            push_funds_block_indicator (str): Details if the card is enabled to receive push-to-card disbursements.. [optional]  # noqa: E501
            security_code_verification (str): Details the results of the Card Verification Code check.. [optional]  # noqa: E501
            tags (object): Include up to 50 `key`: **value** pairs to annotate requests with custom metadata. - Maximum character length for individual `keys` is 40. - Maximum character length for individual **values** is 500.  (e.g., `order number`: **25**, `item_type`: **produce**, `department`: **sales**, etc.). [optional]  # noqa: E501
            type (str): Type of `Payment Instrument`.. [optional]  # noqa: E501
            links (PaymentInstrumentLinks): [optional]  # noqa: E501
            account_type (str): Details what kind of **BANK_ACCOUNT** is being used.. [optional]  # noqa: E501
            bank_account_validation_check (str): Details the results of the bank account validation check if `attempt_bank_account_validation_check` is set to **true** or the `Payment Instrument` gets used to create a `Transfer`. - **INCONCLUSIVE**: A verification check was performed, but the bank account couldn't be found or verified with the issuing bank. Reach out to the buyer to verify the details collected or request another method of payment,  - **INVALID**: The `Payment Instrument` was used in transactions that returned one of the following ACH errors: <ul><li>**Account Does Not Allow ACH Transactions**</li><li>**Account is Closed**</li><li>**Account Funds are Frozen**</li><li>**Deceased Account Holder**</li><li>**Invalid Account Number**</li><li>**Invalid Routing Number**</li><li>**No Account on File**</li></ul>. For more details on the different ACH failure codes, see [ACH Direct Debit.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/#failed-ach-direct-debits) - **NOT_ATTEMPTED**: A verification check wasn't performed and the `Payment Instrument` hasn't been used to create a `Transfer` or `Authorization`. - **VALID**: The bank account was verified. The `Payment Instrument` can be used to create [ACH Direct Debits.](/guides/payments/online-payments/getting-started/finix-api/ach-echeck/#failed-ach-direct-debits). [optional] if omitted the server will use the default value of 'NOT_ATTEMPTED'  # noqa: E501
            bank_code (str): The routing number of the bank account.. [optional]  # noqa: E501
            country (Country): [optional]  # noqa: E501
            masked_account_number (str): The last 4 digits of the account number used to create the `Payment Instrument`.. [optional]  # noqa: E501
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
