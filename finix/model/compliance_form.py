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
    from finix.model.compliance_form_files import ComplianceFormFiles
    from finix.model.compliance_form_pci_saq_a import ComplianceFormPciSaqA
    from finix.model.tags import Tags
    globals()['ComplianceFormFiles'] = ComplianceFormFiles
    globals()['ComplianceFormPciSaqA'] = ComplianceFormPciSaqA
    globals()['Tags'] = Tags


class ComplianceForm(ModelNormal):
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
        ('state',): {
            'PENDING': "PENDING",
            'COMPLETE': "COMPLETE",
            'INVALID': "INVALID",
            'INCOMPLETE': "INCOMPLETE",
        },
        ('type',): {
            'PCI_SAQ_A': "PCI_SAQ_A",
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
            'application_id': (str,),  # noqa: E501
            'compliance_form_template': (str,),  # noqa: E501
            'due_at': (datetime,),  # noqa: E501
            'files': (ComplianceFormFiles,),  # noqa: E501
            'linked_to': (str,),  # noqa: E501
            'linked_type': (str,),  # noqa: E501
            'pci_saq_a': (ComplianceFormPciSaqA,),  # noqa: E501
            'state': (str,),  # noqa: E501
            'tags': (Tags,),  # noqa: E501
            'type': (str,),  # noqa: E501
            'valid_from': (datetime,),  # noqa: E501
            'valid_until': (str,),  # noqa: E501
            'version': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'id': 'id',  # noqa: E501
        'created_at': 'created_at',  # noqa: E501
        'updated_at': 'updated_at',  # noqa: E501
        'application_id': 'application_id',  # noqa: E501
        'compliance_form_template': 'compliance_form_template',  # noqa: E501
        'due_at': 'due_at',  # noqa: E501
        'files': 'files',  # noqa: E501
        'linked_to': 'linked_to',  # noqa: E501
        'linked_type': 'linked_type',  # noqa: E501
        'pci_saq_a': 'pci_saq_a',  # noqa: E501
        'state': 'state',  # noqa: E501
        'tags': 'tags',  # noqa: E501
        'type': 'type',  # noqa: E501
        'valid_from': 'valid_from',  # noqa: E501
        'valid_until': 'valid_until',  # noqa: E501
        'version': 'version',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ComplianceForm - a model defined in OpenAPI

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
            id (str): ID of the `compliance_form`.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            application_id (str): The ID of the `Application` the `compliance_form` was created under.. [optional]  # noqa: E501
            compliance_form_template (str): Template linked to this `compliance_form`.. [optional]  # noqa: E501
            due_at (datetime): Timestamp of when the `compliance_form` must be completed by.. [optional]  # noqa: E501
            files (ComplianceFormFiles): [optional]  # noqa: E501
            linked_to (str): The ID of the `merchant` linked to the `compliance_form`.. [optional]  # noqa: E501
            linked_type (str): The type of resource this `compliance_form` is linked to.. [optional]  # noqa: E501
            pci_saq_a (ComplianceFormPciSaqA): [optional]  # noqa: E501
            state (str): The state of the `compliance_form`.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            type (str): Type of `compliance_form`. There is one available value: **PCI_SAQ_A**.. [optional] if omitted the server will use the default value of "PCI_SAQ_A"  # noqa: E501
            valid_from (datetime): Timestamp of when the `compliance_form` becomes active and valid.. [optional]  # noqa: E501
            valid_until (str): Timestamp of when the `compliance_form` is no longer active and valid.. [optional]  # noqa: E501
            version (str): Details the version of the SAQ form. When `compliance_forms` are created, Finix automatically provides the most up-to-date SAQ form that's available.. [optional]  # noqa: E501
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
        """ComplianceForm - a model defined in OpenAPI

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
            id (str): ID of the `compliance_form`.. [optional]  # noqa: E501
            created_at (datetime): Timestamp of when the object was created.. [optional]  # noqa: E501
            updated_at (datetime): Timestamp of when the object was last updated.. [optional]  # noqa: E501
            application_id (str): The ID of the `Application` the `compliance_form` was created under.. [optional]  # noqa: E501
            compliance_form_template (str): Template linked to this `compliance_form`.. [optional]  # noqa: E501
            due_at (datetime): Timestamp of when the `compliance_form` must be completed by.. [optional]  # noqa: E501
            files (ComplianceFormFiles): [optional]  # noqa: E501
            linked_to (str): The ID of the `merchant` linked to the `compliance_form`.. [optional]  # noqa: E501
            linked_type (str): The type of resource this `compliance_form` is linked to.. [optional]  # noqa: E501
            pci_saq_a (ComplianceFormPciSaqA): [optional]  # noqa: E501
            state (str): The state of the `compliance_form`.. [optional]  # noqa: E501
            tags (Tags): [optional]  # noqa: E501
            type (str): Type of `compliance_form`. There is one available value: **PCI_SAQ_A**.. [optional] if omitted the server will use the default value of "PCI_SAQ_A"  # noqa: E501
            valid_from (datetime): Timestamp of when the `compliance_form` becomes active and valid.. [optional]  # noqa: E501
            valid_until (str): Timestamp of when the `compliance_form` is no longer active and valid.. [optional]  # noqa: E501
            version (str): Details the version of the SAQ form. When `compliance_forms` are created, Finix automatically provides the most up-to-date SAQ form that's available.. [optional]  # noqa: E501
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
