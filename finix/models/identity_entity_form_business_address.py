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



class IdentityEntityFormBusinessAddress(ModelNormal):
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
        ('country',): {
            'None': None,
            '&#39;ABW&#39;': 'ABW',
            '&#39;AFG&#39;': 'AFG',
            '&#39;AGO&#39;': 'AGO',
            '&#39;AIA&#39;': 'AIA',
            '&#39;ALA&#39;': 'ALA',
            '&#39;ALB&#39;': 'ALB',
            '&#39;AND&#39;': 'AND',
            '&#39;ARE&#39;': 'ARE',
            '&#39;ARG&#39;': 'ARG',
            '&#39;ARM&#39;': 'ARM',
            '&#39;ASM&#39;': 'ASM',
            '&#39;ATA&#39;': 'ATA',
            '&#39;ATF&#39;': 'ATF',
            '&#39;ATG&#39;': 'ATG',
            '&#39;AUS&#39;': 'AUS',
            '&#39;AUT&#39;': 'AUT',
            '&#39;AZE&#39;': 'AZE',
            '&#39;BDI&#39;': 'BDI',
            '&#39;BEL&#39;': 'BEL',
            '&#39;BEN&#39;': 'BEN',
            '&#39;BES&#39;': 'BES',
            '&#39;BFA&#39;': 'BFA',
            '&#39;BGD&#39;': 'BGD',
            '&#39;BGR&#39;': 'BGR',
            '&#39;BHR&#39;': 'BHR',
            '&#39;BHS&#39;': 'BHS',
            '&#39;BIH&#39;': 'BIH',
            '&#39;BLM&#39;': 'BLM',
            '&#39;BLR&#39;': 'BLR',
            '&#39;BLZ&#39;': 'BLZ',
            '&#39;BMU&#39;': 'BMU',
            '&#39;BOL&#39;': 'BOL',
            '&#39;BRA&#39;': 'BRA',
            '&#39;BRB&#39;': 'BRB',
            '&#39;BRN&#39;': 'BRN',
            '&#39;BTN&#39;': 'BTN',
            '&#39;BVT&#39;': 'BVT',
            '&#39;BWA&#39;': 'BWA',
            '&#39;CAF&#39;': 'CAF',
            '&#39;CAN&#39;': 'CAN',
            '&#39;CCK&#39;': 'CCK',
            '&#39;CHE&#39;': 'CHE',
            '&#39;CHL&#39;': 'CHL',
            '&#39;CHN&#39;': 'CHN',
            '&#39;CIV&#39;': 'CIV',
            '&#39;CMR&#39;': 'CMR',
            '&#39;COD&#39;': 'COD',
            '&#39;COG&#39;': 'COG',
            '&#39;COK&#39;': 'COK',
            '&#39;COL&#39;': 'COL',
            '&#39;COM&#39;': 'COM',
            '&#39;CPV&#39;': 'CPV',
            '&#39;CRI&#39;': 'CRI',
            '&#39;CUB&#39;': 'CUB',
            '&#39;CUW&#39;': 'CUW',
            '&#39;CXR&#39;': 'CXR',
            '&#39;CYM&#39;': 'CYM',
            '&#39;CYP&#39;': 'CYP',
            '&#39;CZE&#39;': 'CZE',
            '&#39;DEU&#39;': 'DEU',
            '&#39;DJI&#39;': 'DJI',
            '&#39;DMA&#39;': 'DMA',
            '&#39;DNK&#39;': 'DNK',
            '&#39;DOM&#39;': 'DOM',
            '&#39;DZA&#39;': 'DZA',
            '&#39;ECU&#39;': 'ECU',
            '&#39;EGY&#39;': 'EGY',
            '&#39;ERI&#39;': 'ERI',
            '&#39;ESH&#39;': 'ESH',
            '&#39;ESP&#39;': 'ESP',
            '&#39;EST&#39;': 'EST',
            '&#39;ETH&#39;': 'ETH',
            '&#39;FIN&#39;': 'FIN',
            '&#39;FJI&#39;': 'FJI',
            '&#39;FLK&#39;': 'FLK',
            '&#39;FRA&#39;': 'FRA',
            '&#39;FRO&#39;': 'FRO',
            '&#39;FSM&#39;': 'FSM',
            '&#39;GAB&#39;': 'GAB',
            '&#39;GBR&#39;': 'GBR',
            '&#39;GEO&#39;': 'GEO',
            '&#39;GGY&#39;': 'GGY',
            '&#39;GHA&#39;': 'GHA',
            '&#39;GIB&#39;': 'GIB',
            '&#39;GIN&#39;': 'GIN',
            '&#39;GLP&#39;': 'GLP',
            '&#39;GMB&#39;': 'GMB',
            '&#39;GNB&#39;': 'GNB',
            '&#39;GNQ&#39;': 'GNQ',
            '&#39;GRC&#39;': 'GRC',
            '&#39;GRD&#39;': 'GRD',
            '&#39;GRL&#39;': 'GRL',
            '&#39;GTM&#39;': 'GTM',
            '&#39;GUF&#39;': 'GUF',
            '&#39;GUM&#39;': 'GUM',
            '&#39;GUY&#39;': 'GUY',
            '&#39;HKG&#39;': 'HKG',
            '&#39;HMD&#39;': 'HMD',
            '&#39;HND&#39;': 'HND',
            '&#39;HRV&#39;': 'HRV',
            '&#39;HTI&#39;': 'HTI',
            '&#39;HUN&#39;': 'HUN',
            '&#39;IDN&#39;': 'IDN',
            '&#39;IMN&#39;': 'IMN',
            '&#39;IND&#39;': 'IND',
            '&#39;IOT&#39;': 'IOT',
            '&#39;IRL&#39;': 'IRL',
            '&#39;IRN&#39;': 'IRN',
            '&#39;IRQ&#39;': 'IRQ',
            '&#39;ISL&#39;': 'ISL',
            '&#39;ISR&#39;': 'ISR',
            '&#39;ITA&#39;': 'ITA',
            '&#39;JAM&#39;': 'JAM',
            '&#39;JEY&#39;': 'JEY',
            '&#39;JOR&#39;': 'JOR',
            '&#39;JPN&#39;': 'JPN',
            '&#39;KAZ&#39;': 'KAZ',
            '&#39;KEN&#39;': 'KEN',
            '&#39;KGZ&#39;': 'KGZ',
            '&#39;KHM&#39;': 'KHM',
            '&#39;KIR&#39;': 'KIR',
            '&#39;KNA&#39;': 'KNA',
            '&#39;KOR&#39;': 'KOR',
            '&#39;KWT&#39;': 'KWT',
            '&#39;LAO&#39;': 'LAO',
            '&#39;LBN&#39;': 'LBN',
            '&#39;LBR&#39;': 'LBR',
            '&#39;LBY&#39;': 'LBY',
            '&#39;LCA&#39;': 'LCA',
            '&#39;LIE&#39;': 'LIE',
            '&#39;LKA&#39;': 'LKA',
            '&#39;LSO&#39;': 'LSO',
            '&#39;LTU&#39;': 'LTU',
            '&#39;LUX&#39;': 'LUX',
            '&#39;LVA&#39;': 'LVA',
            '&#39;MAC&#39;': 'MAC',
            '&#39;MAF&#39;': 'MAF',
            '&#39;MAR&#39;': 'MAR',
            '&#39;MCO&#39;': 'MCO',
            '&#39;MDA&#39;': 'MDA',
            '&#39;MDG&#39;': 'MDG',
            '&#39;MDV&#39;': 'MDV',
            '&#39;MEX&#39;': 'MEX',
            '&#39;MHL&#39;': 'MHL',
            '&#39;MKD&#39;': 'MKD',
            '&#39;MLI&#39;': 'MLI',
            '&#39;MLT&#39;': 'MLT',
            '&#39;MMR&#39;': 'MMR',
            '&#39;MNE&#39;': 'MNE',
            '&#39;MNG&#39;': 'MNG',
            '&#39;MNP&#39;': 'MNP',
            '&#39;MRT&#39;': 'MRT',
            '&#39;MSR&#39;': 'MSR',
            '&#39;MTQ&#39;': 'MTQ',
            '&#39;MUS&#39;': 'MUS',
            '&#39;MWI&#39;': 'MWI',
            '&#39;MYS&#39;': 'MYS',
            '&#39;MYT&#39;': 'MYT',
            '&#39;NAM&#39;': 'NAM',
            '&#39;NCL&#39;': 'NCL',
            '&#39;NER&#39;': 'NER',
            '&#39;NFK&#39;': 'NFK',
            '&#39;NGA&#39;': 'NGA',
            '&#39;NIC&#39;': 'NIC',
            '&#39;NIU&#39;': 'NIU',
            '&#39;NLD&#39;': 'NLD',
            '&#39;NOR&#39;': 'NOR',
            '&#39;NPL&#39;': 'NPL',
            '&#39;NRU&#39;': 'NRU',
            '&#39;NZL&#39;': 'NZL',
            '&#39;OMN&#39;': 'OMN',
            '&#39;PAK&#39;': 'PAK',
            '&#39;PAN&#39;': 'PAN',
            '&#39;PCN&#39;': 'PCN',
            '&#39;PER&#39;': 'PER',
            '&#39;PHL&#39;': 'PHL',
            '&#39;PLW&#39;': 'PLW',
            '&#39;PNG&#39;': 'PNG',
            '&#39;POL&#39;': 'POL',
            '&#39;PRI&#39;': 'PRI',
            '&#39;PRK&#39;': 'PRK',
            '&#39;PRT&#39;': 'PRT',
            '&#39;PRY&#39;': 'PRY',
            '&#39;PSE&#39;': 'PSE',
            '&#39;PYF&#39;': 'PYF',
            '&#39;QAT&#39;': 'QAT',
            '&#39;REU&#39;': 'REU',
            '&#39;ROU&#39;': 'ROU',
            '&#39;RUS&#39;': 'RUS',
            '&#39;RWA&#39;': 'RWA',
            '&#39;SAU&#39;': 'SAU',
            '&#39;SDN&#39;': 'SDN',
            '&#39;SEN&#39;': 'SEN',
            '&#39;SGP&#39;': 'SGP',
            '&#39;SGS&#39;': 'SGS',
            '&#39;SHN&#39;': 'SHN',
            '&#39;SJM&#39;': 'SJM',
            '&#39;SLB&#39;': 'SLB',
            '&#39;SLE&#39;': 'SLE',
            '&#39;SLV&#39;': 'SLV',
            '&#39;SMR&#39;': 'SMR',
            '&#39;SOM&#39;': 'SOM',
            '&#39;SPM&#39;': 'SPM',
            '&#39;SRB&#39;': 'SRB',
            '&#39;SSD&#39;': 'SSD',
            '&#39;STP&#39;': 'STP',
            '&#39;SUR&#39;': 'SUR',
            '&#39;SVK&#39;': 'SVK',
            '&#39;SVN&#39;': 'SVN',
            '&#39;SWE&#39;': 'SWE',
            '&#39;SWZ&#39;': 'SWZ',
            '&#39;SXM&#39;': 'SXM',
            '&#39;SYC&#39;': 'SYC',
            '&#39;SYR&#39;': 'SYR',
            '&#39;TCA&#39;': 'TCA',
            '&#39;TCD&#39;': 'TCD',
            '&#39;TGO&#39;': 'TGO',
            '&#39;THA&#39;': 'THA',
            '&#39;TJK&#39;': 'TJK',
            '&#39;TKL&#39;': 'TKL',
            '&#39;TKM&#39;': 'TKM',
            '&#39;TLS&#39;': 'TLS',
            '&#39;TON&#39;': 'TON',
            '&#39;TTO&#39;': 'TTO',
            '&#39;TUN&#39;': 'TUN',
            '&#39;TUR&#39;': 'TUR',
            '&#39;TUV&#39;': 'TUV',
            '&#39;TWN&#39;': 'TWN',
            '&#39;TZA&#39;': 'TZA',
            '&#39;UGA&#39;': 'UGA',
            '&#39;UKR&#39;': 'UKR',
            '&#39;UMI&#39;': 'UMI',
            '&#39;URY&#39;': 'URY',
            '&#39;USA&#39;': 'USA',
            '&#39;UZB&#39;': 'UZB',
            '&#39;VAT&#39;': 'VAT',
            '&#39;VCT&#39;': 'VCT',
            '&#39;VEN&#39;': 'VEN',
            '&#39;VGB&#39;': 'VGB',
            '&#39;VIR&#39;': 'VIR',
            '&#39;VNM&#39;': 'VNM',
            '&#39;VUT&#39;': 'VUT',
            '&#39;WLF&#39;': 'WLF',
            '&#39;WSM&#39;': 'WSM',
            '&#39;XKX&#39;': 'XKX',
            '&#39;YEM&#39;': 'YEM',
            '&#39;ZAF&#39;': 'ZAF',
            '&#39;ZMB&#39;': 'ZMB',
            '&#39;ZWE&#39;': 'ZWE',
        },
    }

    validations = {
    }

    additional_properties_type = None

    _nullable = True

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
            'city': (str,),  # noqa: E501
            'country': (str,),  # noqa: E501
            'line1': (str,),  # noqa: E501
            'postal_code': (str,),  # noqa: E501
            'region': (str,),  # noqa: E501
            'line2': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'city': 'city',  # noqa: E501
        'country': 'country',  # noqa: E501
        'line1': 'line1',  # noqa: E501
        'postal_code': 'postal_code',  # noqa: E501
        'region': 'region',  # noqa: E501
        'line2': 'line2',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, city, country, line1, postal_code, region, *args, **kwargs):  # noqa: E501
        """IdentityEntityFormBusinessAddress - a model defined in OpenAPI

        Args:
            city (str): City (max 20 characters).
            country (str): 3-Letter Country code.
            line1 (str): First line of the address (max 35 characters).
            postal_code (str): Zip or Postal code (max 7 characters).
            region (str): 2-letter State code.

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
            line2 (str): Second line of the address (max 35 characters).. [optional]  # noqa: E501
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

        self.city = city
        self.country = country
        self.line1 = line1
        self.postal_code = postal_code
        self.region = region
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
    def __init__(self, city, country, line1, postal_code, region, *args, **kwargs):  # noqa: E501
        """IdentityEntityFormBusinessAddress - a model defined in OpenAPI

        Args:
            city (str): City (max 20 characters).
            country (str): 3-Letter Country code.
            line1 (str): First line of the address (max 35 characters).
            postal_code (str): Zip or Postal code (max 7 characters).
            region (str): 2-letter State code.

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
            line2 (str): Second line of the address (max 35 characters).. [optional]  # noqa: E501
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

        self.city = city
        self.country = country
        self.line1 = line1
        self.postal_code = postal_code
        self.region = region
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
