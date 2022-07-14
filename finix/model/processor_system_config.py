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
    from finix.model.country import Country
    from finix.model.currency import Currency
    from finix.model.processor_system_config_configuration_templates import ProcessorSystemConfigConfigurationTemplates
    globals()['Country'] = Country
    globals()['Currency'] = Currency
    globals()['ProcessorSystemConfigConfigurationTemplates'] = ProcessorSystemConfigConfigurationTemplates


class ProcessorSystemConfig(ModelNormal):
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
        ('class_key_identifier',): {
            'IO.FINIX.VISA.DIRECT.CLIENT.VISASYSTEMCONFIG': "io.finix.visa.direct.client.VisaSystemConfig",
        },
        ('acquirer_country_code',): {
            '004': "004",
            '008': "008",
            '010': "010",
            '012': "012",
            '016': "016",
            '020': "020",
            '024': "024",
            '028': "028",
            '031': "031",
            '032': "032",
            '036': "036",
            '040': "040",
            '044': "044",
            '048': "048",
            '050': "050",
            '051': "051",
            '052': "052",
            '056': "056",
            '060': "060",
            '064': "064",
            '068': "068",
            '070': "070",
            '072': "072",
            '074': "074",
            '076': "076",
            '084': "084",
            '086': "086",
            '090': "090",
            '092': "092",
            '096': "096",
            '100': "100",
            '104': "104",
            '108': "108",
            '112': "112",
            '116': "116",
            '120': "120",
            '124': "124",
            '132': "132",
            '136': "136",
            '140': "140",
            '144': "144",
            '148': "148",
            '152': "152",
            '156': "156",
            '158': "158",
            '162': "162",
            '166': "166",
            '170': "170",
            '174': "174",
            '175': "175",
            '178': "178",
            '180': "180",
            '184': "184",
            '188': "188",
            '191': "191",
            '192': "192",
            '196': "196",
            '203': "203",
            '204': "204",
            '208': "208",
            '212': "212",
            '214': "214",
            '218': "218",
            '222': "222",
            '226': "226",
            '231': "231",
            '232': "232",
            '233': "233",
            '234': "234",
            '238': "238",
            '239': "239",
            '242': "242",
            '246': "246",
            '248': "248",
            '250': "250",
            '254': "254",
            '258': "258",
            '260': "260",
            '262': "262",
            '266': "266",
            '268': "268",
            '270': "270",
            '275': "275",
            '276': "276",
            '288': "288",
            '292': "292",
            '296': "296",
            '300': "300",
            '304': "304",
            '308': "308",
            '312': "312",
            '316': "316",
            '320': "320",
            '324': "324",
            '328': "328",
            '332': "332",
            '334': "334",
            '336': "336",
            '340': "340",
            '344': "344",
            '348': "348",
            '352': "352",
            '356': "356",
            '360': "360",
            '364': "364",
            '368': "368",
            '372': "372",
            '376': "376",
            '380': "380",
            '384': "384",
            '388': "388",
            '392': "392",
            '398': "398",
            '400': "400",
            '404': "404",
            '408': "408",
            '410': "410",
            '414': "414",
            '417': "417",
            '418': "418",
            '422': "422",
            '426': "426",
            '428': "428",
            '430': "430",
            '434': "434",
            '438': "438",
            '440': "440",
            '442': "442",
            '446': "446",
            '450': "450",
            '454': "454",
            '458': "458",
            '462': "462",
            '466': "466",
            '470': "470",
            '474': "474",
            '478': "478",
            '480': "480",
            '484': "484",
            '492': "492",
            '496': "496",
            '498': "498",
            '499': "499",
            '500': "500",
            '504': "504",
            '508': "508",
            '512': "512",
            '516': "516",
            '520': "520",
            '524': "524",
            '528': "528",
            '531': "531",
            '533': "533",
            '534': "534",
            '535': "535",
            '540': "540",
            '548': "548",
            '554': "554",
            '558': "558",
            '562': "562",
            '566': "566",
            '570': "570",
            '574': "574",
            '578': "578",
            '580': "580",
            '581': "581",
            '583': "583",
            '584': "584",
            '585': "585",
            '586': "586",
            '591': "591",
            '598': "598",
            '600': "600",
            '604': "604",
            '608': "608",
            '612': "612",
            '616': "616",
            '620': "620",
            '624': "624",
            '626': "626",
            '630': "630",
            '634': "634",
            '638': "638",
            '642': "642",
            '643': "643",
            '646': "646",
            '652': "652",
            '654': "654",
            '659': "659",
            '660': "660",
            '662': "662",
            '663': "663",
            '666': "666",
            '670': "670",
            '674': "674",
            '678': "678",
            '682': "682",
            '686': "686",
            '688': "688",
            '690': "690",
            '694': "694",
            '702': "702",
            '703': "703",
            '704': "704",
            '705': "705",
            '706': "706",
            '710': "710",
            '716': "716",
            '724': "724",
            '728': "728",
            '729': "729",
            '732': "732",
            '740': "740",
            '744': "744",
            '748': "748",
            '752': "752",
            '756': "756",
            '760': "760",
            '762': "762",
            '764': "764",
            '768': "768",
            '772': "772",
            '776': "776",
            '780': "780",
            '784': "784",
            '788': "788",
            '792': "792",
            '795': "795",
            '796': "796",
            '798': "798",
            '800': "800",
            '804': "804",
            '807': "807",
            '818': "818",
            '826': "826",
            '831': "831",
            '832': "832",
            '833': "833",
            '834': "834",
            '840': "840",
            '850': "850",
            '854': "854",
            '858': "858",
            '860': "860",
            '862': "862",
            '876': "876",
            '882': "882",
            '887': "887",
            '894': "894",
        },
        ('source_of_funds',): {
            '01': "01",
            '02': "02",
            '03': "03",
            '04': "04",
            '05': "05",
            '06': "06",
        },
    }

    validations = {
        ('acquiring_bin',): {
            'regex': {
                'pattern': r'^\d{6}$',  # noqa: E501
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
        lazy_import()
        return {
            'class_key_identifier': (str,),  # noqa: E501
            'acquirer_country_code': (str,),  # noqa: E501
            'acquiring_bin': (str,),  # noqa: E501
            'allow_credit_for_partner': (bool,),  # noqa: E501
            'available_countries': ([Country],),  # noqa: E501
            'business_application_id': (str, none_type,),  # noqa: E501
            'configuration_templates': (ProcessorSystemConfigConfigurationTemplates,),  # noqa: E501
            'default_currencies': ([Currency],),  # noqa: E501
            'disable_ppgs': (bool,),  # noqa: E501
            'fee_program_indicator': (str,),  # noqa: E501
            'gateway_proxy_certificate': (str, none_type,),  # noqa: E501
            'gateway_proxy_host': (str, none_type,),  # noqa: E501
            'gateway_proxy_password': (str, none_type,),  # noqa: E501
            'gateway_proxy_port': (str, none_type,),  # noqa: E501
            'gateway_proxy_username': (str, none_type,),  # noqa: E501
            'key_store_password': (str,),  # noqa: E501
            'key_store_path': (str,),  # noqa: E501
            'merchant_pseudo_aba_number': (str, none_type,),  # noqa: E501
            'online_credit_processing': (bool,),  # noqa: E501
            'online_debit_processing': (bool,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'private_key_password': (str,),  # noqa: E501
            'processor_sequence_limit': (int,),  # noqa: E501
            'pseudo_batch_push': (bool,),  # noqa: E501
            'source_of_funds': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'visa_acceptance_cloud_key_store_path': (str, none_type,),  # noqa: E501
            'visa_acceptance_cloud_password': (str, none_type,),  # noqa: E501
            'visa_acceptance_cloud_url': (str, none_type,),  # noqa: E501
            'visa_acceptance_cloud_user_id': (str, none_type,),  # noqa: E501
            'visa_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'class_key_identifier': 'CLASS_KEY_IDENTIFIER',  # noqa: E501
        'acquirer_country_code': 'acquirer_country_code',  # noqa: E501
        'acquiring_bin': 'acquiring_bin',  # noqa: E501
        'allow_credit_for_partner': 'allow_credit_for_partner',  # noqa: E501
        'available_countries': 'available_countries',  # noqa: E501
        'business_application_id': 'business_application_id',  # noqa: E501
        'configuration_templates': 'configuration_templates',  # noqa: E501
        'default_currencies': 'default_currencies',  # noqa: E501
        'disable_ppgs': 'disable_ppgs',  # noqa: E501
        'fee_program_indicator': 'fee_program_indicator',  # noqa: E501
        'gateway_proxy_certificate': 'gateway_proxy_certificate',  # noqa: E501
        'gateway_proxy_host': 'gateway_proxy_host',  # noqa: E501
        'gateway_proxy_password': 'gateway_proxy_password',  # noqa: E501
        'gateway_proxy_port': 'gateway_proxy_port',  # noqa: E501
        'gateway_proxy_username': 'gateway_proxy_username',  # noqa: E501
        'key_store_password': 'key_store_password',  # noqa: E501
        'key_store_path': 'key_store_path',  # noqa: E501
        'merchant_pseudo_aba_number': 'merchant_pseudo_aba_number',  # noqa: E501
        'online_credit_processing': 'online_credit_processing',  # noqa: E501
        'online_debit_processing': 'online_debit_processing',  # noqa: E501
        'password': 'password',  # noqa: E501
        'private_key_password': 'private_key_password',  # noqa: E501
        'processor_sequence_limit': 'processor_sequence_limit',  # noqa: E501
        'pseudo_batch_push': 'pseudo_batch_push',  # noqa: E501
        'source_of_funds': 'source_of_funds',  # noqa: E501
        'user_id': 'user_id',  # noqa: E501
        'visa_acceptance_cloud_key_store_path': 'visa_acceptance_cloud_key_store_path',  # noqa: E501
        'visa_acceptance_cloud_password': 'visa_acceptance_cloud_password',  # noqa: E501
        'visa_acceptance_cloud_url': 'visa_acceptance_cloud_url',  # noqa: E501
        'visa_acceptance_cloud_user_id': 'visa_acceptance_cloud_user_id',  # noqa: E501
        'visa_url': 'visa_url',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ProcessorSystemConfig - a model defined in OpenAPI

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
            class_key_identifier (str): Field used by processor to communicate with Finix.. [optional] if omitted the server will use the default value of "io.finix.visa.direct.client.VisaSystemConfig"  # noqa: E501
            acquirer_country_code (str): The 3 letter ISO 4217 country code for the country transactions are originating from.. [optional]  # noqa: E501
            acquiring_bin (str): The Bank Identification Number (BIN) the `Processor` is registered under with Visa Direct.. [optional]  # noqa: E501
            allow_credit_for_partner (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            available_countries ([Country]): Details the countries the `Processor` is avalible in.. [optional]  # noqa: E501
            business_application_id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            configuration_templates (ProcessorSystemConfigConfigurationTemplates): [optional]  # noqa: E501
            default_currencies ([Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            disable_ppgs (bool): Set to **true** to enables the option to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            fee_program_indicator (str): Details the price of a Visa Direct payout.. [optional]  # noqa: E501
            gateway_proxy_certificate (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_host (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_password (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_port (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_username (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            key_store_password (str): The password for the Java Keystore that stores the private keys and cert.pem files needed to process transactions using Visa Direct.. [optional]  # noqa: E501
            key_store_path (str): The path in AWS where the Java Keystore that stores the private keys and cert.pem files are and use to transact using Visa Direct.. [optional]  # noqa: E501
            merchant_pseudo_aba_number (str, none_type): A unique ID that's provided when a `Processor` signs up for Push Payment Gateway transactions (PPGS). PPGS allows you to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            online_credit_processing (bool): Details if the `Processor` can handle online credit transactions.. [optional]  # noqa: E501
            online_debit_processing (bool): Details if the `Processor` can handle online debit transactions.. [optional]  # noqa: E501
            password (str): The password found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            private_key_password (str): The password that was used to encrypt the private key that is contained in the Java Keystore.. [optional]  # noqa: E501
            processor_sequence_limit (int): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            pseudo_batch_push (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            source_of_funds (str): Specific code that reflects the use case (e.g. funds disbursement, money transfer, etc.). For a full list of codes, see the following [list from Visa](https://developer.visa.com/request_response_codes#source_of_funds).. [optional]  # noqa: E501
            user_id (str): The user ID found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            visa_acceptance_cloud_key_store_path (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_password (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_url (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_user_id (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_url (str): The URL that is used to connect to Visa.. [optional]  # noqa: E501
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
        """ProcessorSystemConfig - a model defined in OpenAPI

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
            class_key_identifier (str): Field used by processor to communicate with Finix.. [optional] if omitted the server will use the default value of "io.finix.visa.direct.client.VisaSystemConfig"  # noqa: E501
            acquirer_country_code (str): The 3 letter ISO 4217 country code for the country transactions are originating from.. [optional]  # noqa: E501
            acquiring_bin (str): The Bank Identification Number (BIN) the `Processor` is registered under with Visa Direct.. [optional]  # noqa: E501
            allow_credit_for_partner (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            available_countries ([Country]): Details the countries the `Processor` is avalible in.. [optional]  # noqa: E501
            business_application_id (str, none_type): The ID of the resource.. [optional]  # noqa: E501
            configuration_templates (ProcessorSystemConfigConfigurationTemplates): [optional]  # noqa: E501
            default_currencies ([Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            disable_ppgs (bool): Set to **true** to enables the option to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            fee_program_indicator (str): Details the price of a Visa Direct payout.. [optional]  # noqa: E501
            gateway_proxy_certificate (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_host (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_password (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_port (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_username (str, none_type): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            key_store_password (str): The password for the Java Keystore that stores the private keys and cert.pem files needed to process transactions using Visa Direct.. [optional]  # noqa: E501
            key_store_path (str): The path in AWS where the Java Keystore that stores the private keys and cert.pem files are and use to transact using Visa Direct.. [optional]  # noqa: E501
            merchant_pseudo_aba_number (str, none_type): A unique ID that's provided when a `Processor` signs up for Push Payment Gateway transactions (PPGS). PPGS allows you to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            online_credit_processing (bool): Details if the `Processor` can handle online credit transactions.. [optional]  # noqa: E501
            online_debit_processing (bool): Details if the `Processor` can handle online debit transactions.. [optional]  # noqa: E501
            password (str): The password found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            private_key_password (str): The password that was used to encrypt the private key that is contained in the Java Keystore.. [optional]  # noqa: E501
            processor_sequence_limit (int): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            pseudo_batch_push (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            source_of_funds (str): Specific code that reflects the use case (e.g. funds disbursement, money transfer, etc.). For a full list of codes, see the following [list from Visa](https://developer.visa.com/request_response_codes#source_of_funds).. [optional]  # noqa: E501
            user_id (str): The user ID found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            visa_acceptance_cloud_key_store_path (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_password (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_url (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_user_id (str, none_type): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_url (str): The URL that is used to connect to Visa.. [optional]  # noqa: E501
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
