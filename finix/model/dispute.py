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
    from finix.model.dispute_dispute_details import DisputeDisputeDetails
    from finix.model.dispute_links import DisputeLinks
    from finix.model.tags import Tags
    globals()['DisputeDisputeDetails'] = DisputeDisputeDetails
    globals()['DisputeLinks'] = DisputeLinks
    globals()['Tags'] = Tags


class Dispute(ModelNormal):
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
        ('evidence_submitted',): {
            'CHARGEBACK': "CHARGEBACK",
            'NOT_SUPPORTED': "NOT_SUPPORTED",
            'NONE': "NONE",
            'UNKNOWN': "UNKNOWN",
            'INQUIRY': "INQUIRY",
        },
        ('reason',): {
            'CLERICAL': "CLERICAL",
            'FRAUD': "FRAUD",
            'INQUIRY': "INQUIRY",
            'QUALITY': "QUALITY",
            'TECHNICAL': "TECHNICAL",
        },
        ('response_state',): {
            'NEEDS_RESPONSE': "NEEDS_RESPONSE",
            'RESPONDED': "RESPONDED",
            'ACCEPTED': "ACCEPTED",
            'NO_RESPONSE_ALLOWED': "NO_RESPONSE_ALLOWED",
            'UNKNOWN': "UNKNOWN",
        },
        ('state',): {
            'INQUIRY': "INQUIRY",
            'PENDING': "PENDING",
            'WON': "WON",
            'LOST': "LOST",
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
            'action': (str, none_type,),  # noqa: E501
            'amount': (int, none_type,),  # noqa: E501
            'application': (str,),  # noqa: E501
            'dispute_details': (DisputeDisputeDetails,),  # noqa: E501
            'evidence_submitted': (str,),  # noqa: E501
            'identity': (str,),  # noqa: E501
            'merchant': (str,),  # noqa: E501
            'message': (str, none_type,),  # noqa: E501
            'occurred_at': (datetime, none_type,),  # noqa: E501
            'reason': (str,),  # noqa: E501
            'respond_by': (datetime, none_type,),  # noqa: E501
            'response_state': (str,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'transfer': (str,),  # noqa: E501
            'links': (DisputeLinks,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'action': 'action',  # noqa: E501
        'amount': 'amount',  # noqa: E501
        'application': 'application',  # noqa: E501
        'dispute_details': 'dispute_details',  # noqa: E501
        'evidence_submitted': 'evidence_submitted',  # noqa: E501
        'identity': 'identity',  # noqa: E501
        'merchant': 'merchant',  # noqa: E501
        'message': 'message',  # noqa: E501
        'occurred_at': 'occurred_at',  # noqa: E501
        'reason': 'reason',  # noqa: E501
        'respond_by': 'respond_by',  # noqa: E501
        'response_state': 'response_state',  # noqa: E501
        'state': 'state',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'transfer': 'transfer',  # noqa: E501
        'links': '_links',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """Dispute - a model defined in OpenAPI

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
            id (str): The ID of the `Dispute` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            action (str, none_type): The next `action` required to move forward with the `Dispute`.. [optional]  # noqa: E501
            amount (int, none_type): The total amount of the `Dispute` (in cents).. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource that the `Dispute` was created under.. [optional]  # noqa: E501
            dispute_details (DisputeDisputeDetails): [optional]  # noqa: E501
            evidence_submitted (str): The status of the uploaded evidence. [See `Dispute#response_details` for the next steps to move the `Dispute` forward](/api/tag/Disputes/#tag/Disputes/operation/getDispute!c=200&path=response_state&t=response).. [optional]  # noqa: E501
            identity (str): - The ID of the seller's `Identity` resource. - This is the `Identity` resource that was used to create the seller's `Merchant`.. [optional]  # noqa: E501
            merchant (str): - The ID of the seller's `Merchant` resource.  - This is the `Merchant` account the `Dispute` was filed against.. [optional]  # noqa: E501
            message (str, none_type): Message field that provides additional details. This field is typically **null**.. [optional]  # noqa: E501
            occurred_at (datetime, none_type): Point in time when the `Transfer` that's getting disputed got created.. [optional]  # noqa: E501
            reason (str): The system-defined reason for the `Dispute`. Available values include:<ul><li>**INQUIRY**<li>**QUALITY**<li>**FRAUD**. [optional]  # noqa: E501
            respond_by (datetime, none_type): Point in time, the `Merchant` needs to respond to the dispute by.. [optional]  # noqa: E501
            response_state (str): Details the state of the `Dispute` and what action the `Merchant` needs to take. - **NEEDS_RESPONSE**: The `Merchant` needs to respond to the `Dispute` by `Dispute#respond_by`. For details on how to respond to a `Dispute`, see [Responding to Disputes](/guides/after-the-payment/disputes/responding-disputes/). - **RESPONDED**: The issuing bank has received the evidence and actively reviewing it. No action needed from the `Merchant`. - **ACCEPTED**: The `Merchant` has accepted the `Dispute`. When a `Dispute` is accepted, you concede that the dispute is not worth challenging or representing. For details on how to accept a `Dispute`, see [Accepting a Dispute](/guides/after-the-payment/disputes/accepting-disputes/). - **NO_RESPONSE_ALLOWED**: The final `Dispute#response_state` when a `Dispute` is either **WON** or **LOST**. - **UNKNOWN**: `Dispute` details couldn't be submitted to the processor. Comes up when testing `Disputes` in sandbox or on the **DUMMY_V1** processor.. [optional]  # noqa: E501
            state (str): The current state of the `Dispute`.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            transfer (str): ID of the `Transfer` resource.. [optional]  # noqa: E501
            links (DisputeLinks): [optional]  # noqa: E501
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
        """Dispute - a model defined in OpenAPI

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
            id (str): The ID of the `Dispute` resource.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            action (str, none_type): The next `action` required to move forward with the `Dispute`.. [optional]  # noqa: E501
            amount (int, none_type): The total amount of the `Dispute` (in cents).. [optional]  # noqa: E501
            application (str): The ID of the `Application` resource that the `Dispute` was created under.. [optional]  # noqa: E501
            dispute_details (DisputeDisputeDetails): [optional]  # noqa: E501
            evidence_submitted (str): The status of the uploaded evidence. [See `Dispute#response_details` for the next steps to move the `Dispute` forward](/api/tag/Disputes/#tag/Disputes/operation/getDispute!c=200&path=response_state&t=response).. [optional]  # noqa: E501
            identity (str): - The ID of the seller's `Identity` resource. - This is the `Identity` resource that was used to create the seller's `Merchant`.. [optional]  # noqa: E501
            merchant (str): - The ID of the seller's `Merchant` resource.  - This is the `Merchant` account the `Dispute` was filed against.. [optional]  # noqa: E501
            message (str, none_type): Message field that provides additional details. This field is typically **null**.. [optional]  # noqa: E501
            occurred_at (datetime, none_type): Point in time when the `Transfer` that's getting disputed got created.. [optional]  # noqa: E501
            reason (str): The system-defined reason for the `Dispute`. Available values include:<ul><li>**INQUIRY**<li>**QUALITY**<li>**FRAUD**. [optional]  # noqa: E501
            respond_by (datetime, none_type): Point in time, the `Merchant` needs to respond to the dispute by.. [optional]  # noqa: E501
            response_state (str): Details the state of the `Dispute` and what action the `Merchant` needs to take. - **NEEDS_RESPONSE**: The `Merchant` needs to respond to the `Dispute` by `Dispute#respond_by`. For details on how to respond to a `Dispute`, see [Responding to Disputes](/guides/after-the-payment/disputes/responding-disputes/). - **RESPONDED**: The issuing bank has received the evidence and actively reviewing it. No action needed from the `Merchant`. - **ACCEPTED**: The `Merchant` has accepted the `Dispute`. When a `Dispute` is accepted, you concede that the dispute is not worth challenging or representing. For details on how to accept a `Dispute`, see [Accepting a Dispute](/guides/after-the-payment/disputes/accepting-disputes/). - **NO_RESPONSE_ALLOWED**: The final `Dispute#response_state` when a `Dispute` is either **WON** or **LOST**. - **UNKNOWN**: `Dispute` details couldn't be submitted to the processor. Comes up when testing `Disputes` in sandbox or on the **DUMMY_V1** processor.. [optional]  # noqa: E501
            state (str): The current state of the `Dispute`.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            transfer (str): ID of the `Transfer` resource.. [optional]  # noqa: E501
            links (DisputeLinks): [optional]  # noqa: E501
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
