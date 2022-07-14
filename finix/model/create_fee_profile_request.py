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
    from finix.model.tags import Tags
    globals()['Tags'] = Tags


class CreateFeeProfileRequest(ModelNormal):
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
        ('rounding_mode',): {
            'TRANSACTION': "TRANSACTION",
            'AGGREGATE': "AGGREGATE",
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
            'fixed_fee': (int,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'ach_basis_points': (int,),  # noqa: E501
            'ach_credit_return_fixed_fee': (int, none_type,),  # noqa: E501
            'ach_debit_return_fixed_fee': (int, none_type,),  # noqa: E501
            'ach_fixed_fee': (int,),  # noqa: E501
            'american_express_assessment_basis_points': (int, none_type,),  # noqa: E501
            'american_express_basis_points': (int, none_type,),  # noqa: E501
            'american_express_charge_interchange': (bool, none_type,),  # noqa: E501
            'american_express_fixed_fee': (int, none_type,),  # noqa: E501
            'american_express_externally_funded_basis_points': (int, none_type,),  # noqa: E501
            'american_express_externally_funded_fixed_fee': (int, none_type,),  # noqa: E501
            'ancillary_fixed_fee_primary': (int, none_type,),  # noqa: E501
            'ancillary_fixed_fee_secondary': (int, none_type,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'basis_points': (int,),  # noqa: E501
            'externally_funded_basis_points': (int, none_type,),  # noqa: E501
            'externally_funded_fixed_fee': (int, none_type,),  # noqa: E501
            'charge_interchange': (bool,),  # noqa: E501
            'diners_club_basis_points': (int, none_type,),  # noqa: E501
            'diners_club_charge_interchange': (bool, none_type,),  # noqa: E501
            'diners_club_fixed_fee': (int, none_type,),  # noqa: E501
            'discover_assessments_basis_points': (int, none_type,),  # noqa: E501
            'discover_basis_points': (int, none_type,),  # noqa: E501
            'discover_charge_interchange': (bool, none_type,),  # noqa: E501
            'discover_data_usage_fixed_fee': (int, none_type,),  # noqa: E501
            'discover_fixed_fee': (int, none_type,),  # noqa: E501
            'discover_externally_funded_basis_points': (int, none_type,),  # noqa: E501
            'discover_externally_funded_fixed_fee': (int, none_type,),  # noqa: E501
            'discover_network_authorization_fixed_fee': (int, none_type,),  # noqa: E501
            'dispute_fixed_fee': (int, none_type,),  # noqa: E501
            'dispute_inquiry_fixed_fee': (int, none_type,),  # noqa: E501
            'jcb_basis_points': (int, none_type,),  # noqa: E501
            'jcb_charge_interchange': (bool, none_type,),  # noqa: E501
            'jcb_fixed_fee': (int, none_type,),  # noqa: E501
            'mastercard_acquirer_fees_basis_points': (int, none_type,),  # noqa: E501
            'mastercard_assessments_over1k_basis_points': (int, none_type,),  # noqa: E501
            'mastercard_assessments_under1k_basis_points': (int, none_type,),  # noqa: E501
            'mastercard_basis_points': (int, none_type,),  # noqa: E501
            'mastercard_charge_interchange': (bool, none_type,),  # noqa: E501
            'mastercard_fixed_fee': (int, none_type,),  # noqa: E501
            'qualified_tiers': ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type,),  # noqa: E501
            'rounding_mode': (str,),  # noqa: E501
            'visa_acquirer_processing_fixed_fee': (int, none_type,),  # noqa: E501
            'visa_assessments_basis_points': (int, none_type,),  # noqa: E501
            'visa_base_ii_credit_voucher_fixed_fee': (int, none_type,),  # noqa: E501
            'visa_base_ii_system_file_transmission_fixed_fee': (int, none_type,),  # noqa: E501
            'visa_basis_points': (int, none_type,),  # noqa: E501
            'visa_charge_interchange': (bool, none_type,),  # noqa: E501
            'visa_credit_voucher_fixed_fee': (int, none_type,),  # noqa: E501
            'visa_fixed_fee': (int, none_type,),  # noqa: E501
            'visa_kilobyte_access_fixed_fee': (int, none_type,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'fixed_fee': 'fixed_fee',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'ach_basis_points': 'ach_basis_points',  # noqa: E501
        'ach_credit_return_fixed_fee': 'ach_credit_return_fixed_fee',  # noqa: E501
        'ach_debit_return_fixed_fee': 'ach_debit_return_fixed_fee',  # noqa: E501
        'ach_fixed_fee': 'ach_fixed_fee',  # noqa: E501
        'american_express_assessment_basis_points': 'american_express_assessment_basis_points',  # noqa: E501
        'american_express_basis_points': 'american_express_basis_points',  # noqa: E501
        'american_express_charge_interchange': 'american_express_charge_interchange',  # noqa: E501
        'american_express_fixed_fee': 'american_express_fixed_fee',  # noqa: E501
        'american_express_externally_funded_basis_points': 'american_express_externally_funded_basis_points',  # noqa: E501
        'american_express_externally_funded_fixed_fee': 'american_express_externally_funded_fixed_fee',  # noqa: E501
        'ancillary_fixed_fee_primary': 'ancillary_fixed_fee_primary',  # noqa: E501
        'ancillary_fixed_fee_secondary': 'ancillary_fixed_fee_secondary',  # noqa: E501
        'application': 'application',  # noqa: E501
        'basis_points': 'basis_points',  # noqa: E501
        'externally_funded_basis_points': 'externally_funded_basis_points',  # noqa: E501
        'externally_funded_fixed_fee': 'externally_funded_fixed_fee',  # noqa: E501
        'charge_interchange': 'charge_interchange',  # noqa: E501
        'diners_club_basis_points': 'diners_club_basis_points',  # noqa: E501
        'diners_club_charge_interchange': 'diners_club_charge_interchange',  # noqa: E501
        'diners_club_fixed_fee': 'diners_club_fixed_fee',  # noqa: E501
        'discover_assessments_basis_points': 'discover_assessments_basis_points',  # noqa: E501
        'discover_basis_points': 'discover_basis_points',  # noqa: E501
        'discover_charge_interchange': 'discover_charge_interchange',  # noqa: E501
        'discover_data_usage_fixed_fee': 'discover_data_usage_fixed_fee',  # noqa: E501
        'discover_fixed_fee': 'discover_fixed_fee',  # noqa: E501
        'discover_externally_funded_basis_points': 'discover_externally_funded_basis_points',  # noqa: E501
        'discover_externally_funded_fixed_fee': 'discover_externally_funded_fixed_fee',  # noqa: E501
        'discover_network_authorization_fixed_fee': 'discover_network_authorization_fixed_fee',  # noqa: E501
        'dispute_fixed_fee': 'dispute_fixed_fee',  # noqa: E501
        'dispute_inquiry_fixed_fee': 'dispute_inquiry_fixed_fee',  # noqa: E501
        'jcb_basis_points': 'jcb_basis_points',  # noqa: E501
        'jcb_charge_interchange': 'jcb_charge_interchange',  # noqa: E501
        'jcb_fixed_fee': 'jcb_fixed_fee',  # noqa: E501
        'mastercard_acquirer_fees_basis_points': 'mastercard_acquirer_fees_basis_points',  # noqa: E501
        'mastercard_assessments_over1k_basis_points': 'mastercard_assessments_over1k_basis_points',  # noqa: E501
        'mastercard_assessments_under1k_basis_points': 'mastercard_assessments_under1k_basis_points',  # noqa: E501
        'mastercard_basis_points': 'mastercard_basis_points',  # noqa: E501
        'mastercard_charge_interchange': 'mastercard_charge_interchange',  # noqa: E501
        'mastercard_fixed_fee': 'mastercard_fixed_fee',  # noqa: E501
        'qualified_tiers': 'qualified_tiers',  # noqa: E501
        'rounding_mode': 'rounding_mode',  # noqa: E501
        'visa_acquirer_processing_fixed_fee': 'visa_acquirer_processing_fixed_fee',  # noqa: E501
        'visa_assessments_basis_points': 'visa_assessments_basis_points',  # noqa: E501
        'visa_base_ii_credit_voucher_fixed_fee': 'visa_base_II_credit_voucher_fixed_fee',  # noqa: E501
        'visa_base_ii_system_file_transmission_fixed_fee': 'visa_base_II_system_file_transmission_fixed_fee',  # noqa: E501
        'visa_basis_points': 'visa_basis_points',  # noqa: E501
        'visa_charge_interchange': 'visa_charge_interchange',  # noqa: E501
        'visa_credit_voucher_fixed_fee': 'visa_credit_voucher_fixed_fee',  # noqa: E501
        'visa_fixed_fee': 'visa_fixed_fee',  # noqa: E501
        'visa_kilobyte_access_fixed_fee': 'visa_kilobyte_access_fixed_fee',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, fixed_fee, *args, **kwargs):  # noqa: E501
        """CreateFeeProfileRequest - a model defined in OpenAPI

        Args:
            fixed_fee (int): Fee in cents incurred for each individual card-based `Transfer`.

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
            ach_basis_points (int): Percentage-based fee incurred against the full amount of an eCheck (also called ACH payments). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            ach_credit_return_fixed_fee (int, none_type): A fixed amount in cents that will be charged to the merchant for processing an echeck (also called ACH payments) credit return.. [optional]  # noqa: E501
            ach_debit_return_fixed_fee (int, none_type): A fixed amount in cents that will be charged to the merchant for processing an echeck (also called ACH payment) debit return.. [optional]  # noqa: E501
            ach_fixed_fee (int): Fee in cents incurred for each individual `Transfer`.. [optional]  # noqa: E501
            american_express_assessment_basis_points (int, none_type): Applies to gross American Express card volume.. [optional]  # noqa: E501
            american_express_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each American Express `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            american_express_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for American Express `Transfers`.. [optional]  # noqa: E501
            american_express_fixed_fee (int, none_type): Fee in cents incurred for each individual American Express `Transfer`.. [optional]  # noqa: E501
            american_express_externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each American Express externally funded `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            american_express_externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual American Express externally funded `Transfer`.. [optional]  # noqa: E501
            ancillary_fixed_fee_primary (int, none_type): An additional fixed fee that can be charged per `Transfer`.. [optional]  # noqa: E501
            ancillary_fixed_fee_secondary (int, none_type): An additional fixed fee that can be charged per `Transfer` if `ancillary_fixed_fee_primary` is included.. [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            basis_points (int): Percentage-based fee incurred against the full amount of each card-based `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each `Transfer` that's card-based and externally funded. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual `Transfer` that's card-based and externally funded.. [optional]  # noqa: E501
            charge_interchange (bool): Set to **True** to incur interchange fees for card-based `Transfers`.. [optional]  # noqa: E501
            diners_club_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Diners `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            diners_club_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Diners `Transfers`.. [optional]  # noqa: E501
            diners_club_fixed_fee (int, none_type): Fee in cents incurred for each individual Diners `Transfer`.. [optional]  # noqa: E501
            discover_assessments_basis_points (int, none_type): Assessment applies to gross Discover card transaction volume.. [optional]  # noqa: E501
            discover_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Discover `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            discover_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Discover `Transfers`.. [optional]  # noqa: E501
            discover_data_usage_fixed_fee (int, none_type): Applies to all U.S.-based `Authorization` transactions.. [optional]  # noqa: E501
            discover_fixed_fee (int, none_type): Fee in cents incurred for each individual Discover `Transfer`.. [optional]  # noqa: E501
            discover_externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Discover externally funded `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            discover_externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual Discover externally funded `Transfer`.. [optional]  # noqa: E501
            discover_network_authorization_fixed_fee (int, none_type): This fee applies to all Discover network `authorizations` and replaces the previously assessed Data Transmission.. [optional]  # noqa: E501
            dispute_fixed_fee (int, none_type): Applied when a `dispute` is created or updated to a **PENDING** state.. [optional]  # noqa: E501
            dispute_inquiry_fixed_fee (int, none_type): Applied when a `dispute` is created or updated to a **INQUIRY** state.. [optional]  # noqa: E501
            jcb_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each JCB `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            jcb_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for JCB Transfers.. [optional]  # noqa: E501
            jcb_fixed_fee (int, none_type): Fee in cents incurred for each individual JCB `Transfer`.. [optional]  # noqa: E501
            mastercard_acquirer_fees_basis_points (int, none_type): The fee is assessed on a business’s gross MasterCard processing volume. This fee varies per acquirer based on MasterCard’s assessed charge as it’s distributed across the acquirer’s portfolio of merchants. Generally, this fee is a fraction of a basis point. For example, 0.0045%, 0.0075%, etc. are examples of a likely fee.. [optional]  # noqa: E501
            mastercard_assessments_over1k_basis_points (int, none_type): Fee applied to Mastercard credit sale transactions greater than $1,000.. [optional]  # noqa: E501
            mastercard_assessments_under1k_basis_points (int, none_type): Fee applied to Mastercard transactions less than or equal to $1,000.. [optional]  # noqa: E501
            mastercard_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each MasterCard `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            mastercard_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for MasterCard `Transfers`.. [optional]  # noqa: E501
            mastercard_fixed_fee (int, none_type): Fee in cents incurred for each individual MasterCard `Transfer`.. [optional]  # noqa: E501
            qualified_tiers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            rounding_mode (str): <ul><li>Include <strong>AGGREGATE</strong> if you want to round after the settlement calculation.<li>By default, rounding happens before the sum of the settlement calculation (i.e. round each fee transfer)</ul>. [optional]  # noqa: E501
            visa_acquirer_processing_fixed_fee (int, none_type): Applied to all U.S.-based credit card authorizations acquired in the U.S. regardless of where the issuer/cardholder is located. If your business is based in the U.S., the acquirer processing fee will apply to all Visa credit card authorizations.. [optional]  # noqa: E501
            visa_assessments_basis_points (int, none_type): Applies to all Visa credit transactions.. [optional]  # noqa: E501
            visa_base_ii_credit_voucher_fixed_fee (int, none_type): Applies to all U.S.-based refunds.. [optional]  # noqa: E501
            visa_base_ii_system_file_transmission_fixed_fee (int, none_type): Applies to all Visa transactions and is charged in addition to other transaction-based assessments.. [optional]  # noqa: E501
            visa_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Visa `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            visa_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Visa `Transfers`.. [optional]  # noqa: E501
            visa_credit_voucher_fixed_fee (int, none_type): Applies to Visa refunds.. [optional]  # noqa: E501
            visa_fixed_fee (int, none_type): Fee in cents incurred for each individual Visa `Transfer`.. [optional]  # noqa: E501
            visa_kilobyte_access_fixed_fee (int, none_type): Charged on each authorization transaction submitted to Visa’s network for settlement.. [optional]  # noqa: E501
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

        self.fixed_fee = fixed_fee
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
    def __init__(self, fixed_fee, *args, **kwargs):  # noqa: E501
        """CreateFeeProfileRequest - a model defined in OpenAPI

        Args:
            fixed_fee (int): Fee in cents incurred for each individual card-based `Transfer`.

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
            ach_basis_points (int): Percentage-based fee incurred against the full amount of an eCheck (also called ACH payments). Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            ach_credit_return_fixed_fee (int, none_type): A fixed amount in cents that will be charged to the merchant for processing an echeck (also called ACH payments) credit return.. [optional]  # noqa: E501
            ach_debit_return_fixed_fee (int, none_type): A fixed amount in cents that will be charged to the merchant for processing an echeck (also called ACH payment) debit return.. [optional]  # noqa: E501
            ach_fixed_fee (int): Fee in cents incurred for each individual `Transfer`.. [optional]  # noqa: E501
            american_express_assessment_basis_points (int, none_type): Applies to gross American Express card volume.. [optional]  # noqa: E501
            american_express_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each American Express `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            american_express_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for American Express `Transfers`.. [optional]  # noqa: E501
            american_express_fixed_fee (int, none_type): Fee in cents incurred for each individual American Express `Transfer`.. [optional]  # noqa: E501
            american_express_externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each American Express externally funded `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            american_express_externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual American Express externally funded `Transfer`.. [optional]  # noqa: E501
            ancillary_fixed_fee_primary (int, none_type): An additional fixed fee that can be charged per `Transfer`.. [optional]  # noqa: E501
            ancillary_fixed_fee_secondary (int, none_type): An additional fixed fee that can be charged per `Transfer` if `ancillary_fixed_fee_primary` is included.. [optional]  # noqa: E501
            application (str): The ID of the resource.. [optional]  # noqa: E501
            basis_points (int): Percentage-based fee incurred against the full amount of each card-based `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each `Transfer` that's card-based and externally funded. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual `Transfer` that's card-based and externally funded.. [optional]  # noqa: E501
            charge_interchange (bool): Set to **True** to incur interchange fees for card-based `Transfers`.. [optional]  # noqa: E501
            diners_club_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Diners `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            diners_club_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Diners `Transfers`.. [optional]  # noqa: E501
            diners_club_fixed_fee (int, none_type): Fee in cents incurred for each individual Diners `Transfer`.. [optional]  # noqa: E501
            discover_assessments_basis_points (int, none_type): Assessment applies to gross Discover card transaction volume.. [optional]  # noqa: E501
            discover_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Discover `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            discover_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Discover `Transfers`.. [optional]  # noqa: E501
            discover_data_usage_fixed_fee (int, none_type): Applies to all U.S.-based `Authorization` transactions.. [optional]  # noqa: E501
            discover_fixed_fee (int, none_type): Fee in cents incurred for each individual Discover `Transfer`.. [optional]  # noqa: E501
            discover_externally_funded_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Discover externally funded `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            discover_externally_funded_fixed_fee (int, none_type): Fee in cents incurred for each individual Discover externally funded `Transfer`.. [optional]  # noqa: E501
            discover_network_authorization_fixed_fee (int, none_type): This fee applies to all Discover network `authorizations` and replaces the previously assessed Data Transmission.. [optional]  # noqa: E501
            dispute_fixed_fee (int, none_type): Applied when a `dispute` is created or updated to a **PENDING** state.. [optional]  # noqa: E501
            dispute_inquiry_fixed_fee (int, none_type): Applied when a `dispute` is created or updated to a **INQUIRY** state.. [optional]  # noqa: E501
            jcb_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each JCB `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            jcb_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for JCB Transfers.. [optional]  # noqa: E501
            jcb_fixed_fee (int, none_type): Fee in cents incurred for each individual JCB `Transfer`.. [optional]  # noqa: E501
            mastercard_acquirer_fees_basis_points (int, none_type): The fee is assessed on a business’s gross MasterCard processing volume. This fee varies per acquirer based on MasterCard’s assessed charge as it’s distributed across the acquirer’s portfolio of merchants. Generally, this fee is a fraction of a basis point. For example, 0.0045%, 0.0075%, etc. are examples of a likely fee.. [optional]  # noqa: E501
            mastercard_assessments_over1k_basis_points (int, none_type): Fee applied to Mastercard credit sale transactions greater than $1,000.. [optional]  # noqa: E501
            mastercard_assessments_under1k_basis_points (int, none_type): Fee applied to Mastercard transactions less than or equal to $1,000.. [optional]  # noqa: E501
            mastercard_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each MasterCard `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            mastercard_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for MasterCard `Transfers`.. [optional]  # noqa: E501
            mastercard_fixed_fee (int, none_type): Fee in cents incurred for each individual MasterCard `Transfer`.. [optional]  # noqa: E501
            qualified_tiers ({str: (bool, date, datetime, dict, float, int, list, str, none_type)}, none_type): [optional]  # noqa: E501
            rounding_mode (str): <ul><li>Include <strong>AGGREGATE</strong> if you want to round after the settlement calculation.<li>By default, rounding happens before the sum of the settlement calculation (i.e. round each fee transfer)</ul>. [optional]  # noqa: E501
            visa_acquirer_processing_fixed_fee (int, none_type): Applied to all U.S.-based credit card authorizations acquired in the U.S. regardless of where the issuer/cardholder is located. If your business is based in the U.S., the acquirer processing fee will apply to all Visa credit card authorizations.. [optional]  # noqa: E501
            visa_assessments_basis_points (int, none_type): Applies to all Visa credit transactions.. [optional]  # noqa: E501
            visa_base_ii_credit_voucher_fixed_fee (int, none_type): Applies to all U.S.-based refunds.. [optional]  # noqa: E501
            visa_base_ii_system_file_transmission_fixed_fee (int, none_type): Applies to all Visa transactions and is charged in addition to other transaction-based assessments.. [optional]  # noqa: E501
            visa_basis_points (int, none_type): Percentage-based fee incurred against the full amount of each Visa `Transfer`. Calculated as one hundredth of one percent (1 basis point = .0001 or .01%).. [optional]  # noqa: E501
            visa_charge_interchange (bool, none_type): Set to **True** to incur interchange fees for Visa `Transfers`.. [optional]  # noqa: E501
            visa_credit_voucher_fixed_fee (int, none_type): Applies to Visa refunds.. [optional]  # noqa: E501
            visa_fixed_fee (int, none_type): Fee in cents incurred for each individual Visa `Transfer`.. [optional]  # noqa: E501
            visa_kilobyte_access_fixed_fee (int, none_type): Charged on each authorization transaction submitted to Visa’s network for settlement.. [optional]  # noqa: E501
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

        self.fixed_fee = fixed_fee
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
