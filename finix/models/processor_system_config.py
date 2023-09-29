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
    Country
    Currency
    ProcessorSystemConfigConfig


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
        ('acquirer_country_code',): {
            '&#39;004&#39;': '004',
            '&#39;008&#39;': '008',
            '&#39;010&#39;': '010',
            '&#39;012&#39;': '012',
            '&#39;016&#39;': '016',
            '&#39;020&#39;': '020',
            '&#39;024&#39;': '024',
            '&#39;028&#39;': '028',
            '&#39;031&#39;': '031',
            '&#39;032&#39;': '032',
            '&#39;036&#39;': '036',
            '&#39;040&#39;': '040',
            '&#39;044&#39;': '044',
            '&#39;048&#39;': '048',
            '&#39;050&#39;': '050',
            '&#39;051&#39;': '051',
            '&#39;052&#39;': '052',
            '&#39;056&#39;': '056',
            '&#39;060&#39;': '060',
            '&#39;064&#39;': '064',
            '&#39;068&#39;': '068',
            '&#39;070&#39;': '070',
            '&#39;072&#39;': '072',
            '&#39;074&#39;': '074',
            '&#39;076&#39;': '076',
            '&#39;084&#39;': '084',
            '&#39;086&#39;': '086',
            '&#39;090&#39;': '090',
            '&#39;092&#39;': '092',
            '&#39;096&#39;': '096',
            '&#39;100&#39;': '100',
            '&#39;104&#39;': '104',
            '&#39;108&#39;': '108',
            '&#39;112&#39;': '112',
            '&#39;116&#39;': '116',
            '&#39;120&#39;': '120',
            '&#39;124&#39;': '124',
            '&#39;132&#39;': '132',
            '&#39;136&#39;': '136',
            '&#39;140&#39;': '140',
            '&#39;144&#39;': '144',
            '&#39;148&#39;': '148',
            '&#39;152&#39;': '152',
            '&#39;156&#39;': '156',
            '&#39;158&#39;': '158',
            '&#39;162&#39;': '162',
            '&#39;166&#39;': '166',
            '&#39;170&#39;': '170',
            '&#39;174&#39;': '174',
            '&#39;175&#39;': '175',
            '&#39;178&#39;': '178',
            '&#39;180&#39;': '180',
            '&#39;184&#39;': '184',
            '&#39;188&#39;': '188',
            '&#39;191&#39;': '191',
            '&#39;192&#39;': '192',
            '&#39;196&#39;': '196',
            '&#39;203&#39;': '203',
            '&#39;204&#39;': '204',
            '&#39;208&#39;': '208',
            '&#39;212&#39;': '212',
            '&#39;214&#39;': '214',
            '&#39;218&#39;': '218',
            '&#39;222&#39;': '222',
            '&#39;226&#39;': '226',
            '&#39;231&#39;': '231',
            '&#39;232&#39;': '232',
            '&#39;233&#39;': '233',
            '&#39;234&#39;': '234',
            '&#39;238&#39;': '238',
            '&#39;239&#39;': '239',
            '&#39;242&#39;': '242',
            '&#39;246&#39;': '246',
            '&#39;248&#39;': '248',
            '&#39;250&#39;': '250',
            '&#39;254&#39;': '254',
            '&#39;258&#39;': '258',
            '&#39;260&#39;': '260',
            '&#39;262&#39;': '262',
            '&#39;266&#39;': '266',
            '&#39;268&#39;': '268',
            '&#39;270&#39;': '270',
            '&#39;275&#39;': '275',
            '&#39;276&#39;': '276',
            '&#39;288&#39;': '288',
            '&#39;292&#39;': '292',
            '&#39;296&#39;': '296',
            '&#39;300&#39;': '300',
            '&#39;304&#39;': '304',
            '&#39;308&#39;': '308',
            '&#39;312&#39;': '312',
            '&#39;316&#39;': '316',
            '&#39;320&#39;': '320',
            '&#39;324&#39;': '324',
            '&#39;328&#39;': '328',
            '&#39;332&#39;': '332',
            '&#39;334&#39;': '334',
            '&#39;336&#39;': '336',
            '&#39;340&#39;': '340',
            '&#39;344&#39;': '344',
            '&#39;348&#39;': '348',
            '&#39;352&#39;': '352',
            '&#39;356&#39;': '356',
            '&#39;360&#39;': '360',
            '&#39;364&#39;': '364',
            '&#39;368&#39;': '368',
            '&#39;372&#39;': '372',
            '&#39;376&#39;': '376',
            '&#39;380&#39;': '380',
            '&#39;384&#39;': '384',
            '&#39;388&#39;': '388',
            '&#39;392&#39;': '392',
            '&#39;398&#39;': '398',
            '&#39;400&#39;': '400',
            '&#39;404&#39;': '404',
            '&#39;408&#39;': '408',
            '&#39;410&#39;': '410',
            '&#39;414&#39;': '414',
            '&#39;417&#39;': '417',
            '&#39;418&#39;': '418',
            '&#39;422&#39;': '422',
            '&#39;426&#39;': '426',
            '&#39;428&#39;': '428',
            '&#39;430&#39;': '430',
            '&#39;434&#39;': '434',
            '&#39;438&#39;': '438',
            '&#39;440&#39;': '440',
            '&#39;442&#39;': '442',
            '&#39;446&#39;': '446',
            '&#39;450&#39;': '450',
            '&#39;454&#39;': '454',
            '&#39;458&#39;': '458',
            '&#39;462&#39;': '462',
            '&#39;466&#39;': '466',
            '&#39;470&#39;': '470',
            '&#39;474&#39;': '474',
            '&#39;478&#39;': '478',
            '&#39;480&#39;': '480',
            '&#39;484&#39;': '484',
            '&#39;492&#39;': '492',
            '&#39;496&#39;': '496',
            '&#39;498&#39;': '498',
            '&#39;499&#39;': '499',
            '&#39;500&#39;': '500',
            '&#39;504&#39;': '504',
            '&#39;508&#39;': '508',
            '&#39;512&#39;': '512',
            '&#39;516&#39;': '516',
            '&#39;520&#39;': '520',
            '&#39;524&#39;': '524',
            '&#39;528&#39;': '528',
            '&#39;531&#39;': '531',
            '&#39;533&#39;': '533',
            '&#39;534&#39;': '534',
            '&#39;535&#39;': '535',
            '&#39;540&#39;': '540',
            '&#39;548&#39;': '548',
            '&#39;554&#39;': '554',
            '&#39;558&#39;': '558',
            '&#39;562&#39;': '562',
            '&#39;566&#39;': '566',
            '&#39;570&#39;': '570',
            '&#39;574&#39;': '574',
            '&#39;578&#39;': '578',
            '&#39;580&#39;': '580',
            '&#39;581&#39;': '581',
            '&#39;583&#39;': '583',
            '&#39;584&#39;': '584',
            '&#39;585&#39;': '585',
            '&#39;586&#39;': '586',
            '&#39;591&#39;': '591',
            '&#39;598&#39;': '598',
            '&#39;600&#39;': '600',
            '&#39;604&#39;': '604',
            '&#39;608&#39;': '608',
            '&#39;612&#39;': '612',
            '&#39;616&#39;': '616',
            '&#39;620&#39;': '620',
            '&#39;624&#39;': '624',
            '&#39;626&#39;': '626',
            '&#39;630&#39;': '630',
            '&#39;634&#39;': '634',
            '&#39;638&#39;': '638',
            '&#39;642&#39;': '642',
            '&#39;643&#39;': '643',
            '&#39;646&#39;': '646',
            '&#39;652&#39;': '652',
            '&#39;654&#39;': '654',
            '&#39;659&#39;': '659',
            '&#39;660&#39;': '660',
            '&#39;662&#39;': '662',
            '&#39;663&#39;': '663',
            '&#39;666&#39;': '666',
            '&#39;670&#39;': '670',
            '&#39;674&#39;': '674',
            '&#39;678&#39;': '678',
            '&#39;682&#39;': '682',
            '&#39;686&#39;': '686',
            '&#39;688&#39;': '688',
            '&#39;690&#39;': '690',
            '&#39;694&#39;': '694',
            '&#39;702&#39;': '702',
            '&#39;703&#39;': '703',
            '&#39;704&#39;': '704',
            '&#39;705&#39;': '705',
            '&#39;706&#39;': '706',
            '&#39;710&#39;': '710',
            '&#39;716&#39;': '716',
            '&#39;724&#39;': '724',
            '&#39;728&#39;': '728',
            '&#39;729&#39;': '729',
            '&#39;732&#39;': '732',
            '&#39;740&#39;': '740',
            '&#39;744&#39;': '744',
            '&#39;748&#39;': '748',
            '&#39;752&#39;': '752',
            '&#39;756&#39;': '756',
            '&#39;760&#39;': '760',
            '&#39;762&#39;': '762',
            '&#39;764&#39;': '764',
            '&#39;768&#39;': '768',
            '&#39;772&#39;': '772',
            '&#39;776&#39;': '776',
            '&#39;780&#39;': '780',
            '&#39;784&#39;': '784',
            '&#39;788&#39;': '788',
            '&#39;792&#39;': '792',
            '&#39;795&#39;': '795',
            '&#39;796&#39;': '796',
            '&#39;798&#39;': '798',
            '&#39;800&#39;': '800',
            '&#39;804&#39;': '804',
            '&#39;807&#39;': '807',
            '&#39;818&#39;': '818',
            '&#39;826&#39;': '826',
            '&#39;831&#39;': '831',
            '&#39;832&#39;': '832',
            '&#39;833&#39;': '833',
            '&#39;834&#39;': '834',
            '&#39;840&#39;': '840',
            '&#39;850&#39;': '850',
            '&#39;854&#39;': '854',
            '&#39;858&#39;': '858',
            '&#39;860&#39;': '860',
            '&#39;862&#39;': '862',
            '&#39;876&#39;': '876',
            '&#39;882&#39;': '882',
            '&#39;887&#39;': '887',
            '&#39;894&#39;': '894',
        },
        ('class_key_identifier',): {
            '&#39;io.finix.visa.direct.client.VisaSystemConfig&#39;': 'io.finix.visa.direct.client.VisaSystemConfig',
        },
        ('source_of_funds',): {
            '&#39;01&#39;': '01',
            '&#39;02&#39;': '02',
            '&#39;03&#39;': '03',
            '&#39;04&#39;': '04',
            '&#39;05&#39;': '05',
            '&#39;06&#39;': '06',
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
        lazy_import()
        return {
            'acquirer_country_code': (str,),  # noqa: E501
            'acquiring_bin': (str,),  # noqa: E501
            'allow_credit_for_partner': (bool,),  # noqa: E501
            'available_countries': (List[Country],),  # noqa: E501
            'business_application_id': (str,),  # noqa: E501
            'class_key_identifier': (str,),  # noqa: E501
            'config': (ProcessorSystemConfigConfig,),  # noqa: E501
            'default_currencies': (List[Currency],),  # noqa: E501
            'disable_ppgs': (bool,),  # noqa: E501
            'fee_program_indicator': (str,),  # noqa: E501
            'gateway_proxy_certificate': (str,),  # noqa: E501
            'gateway_proxy_host': (str,),  # noqa: E501
            'gateway_proxy_password': (str,),  # noqa: E501
            'gateway_proxy_port': (str,),  # noqa: E501
            'gateway_proxy_username': (str,),  # noqa: E501
            'key_store_password': (str,),  # noqa: E501
            'key_store_path': (str,),  # noqa: E501
            'merchant_pseudo_aba_number': (str,),  # noqa: E501
            'online_credit_processing': (bool,),  # noqa: E501
            'online_debit_processing': (bool,),  # noqa: E501
            'password': (str,),  # noqa: E501
            'private_key_password': (str,),  # noqa: E501
            'processor_sequence_limit': (int,),  # noqa: E501
            'pseudo_batch_push': (bool,),  # noqa: E501
            'source_of_funds': (str,),  # noqa: E501
            'user_id': (str,),  # noqa: E501
            'visa_acceptance_cloud_key_store_path': (str,),  # noqa: E501
            'visa_acceptance_cloud_password': (str,),  # noqa: E501
            'visa_acceptance_cloud_url': (str,),  # noqa: E501
            'visa_acceptance_cloud_user_id': (str,),  # noqa: E501
            'visa_url': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'acquirer_country_code': 'acquirer_country_code',  # noqa: E501
        'acquiring_bin': 'acquiring_bin',  # noqa: E501
        'allow_credit_for_partner': 'allow_credit_for_partner',  # noqa: E501
        'available_countries': 'available_countries',  # noqa: E501
        'business_application_id': 'business_application_id',  # noqa: E501
        'class_key_identifier': 'class_key_identifier',  # noqa: E501
        'config': 'config',  # noqa: E501
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
            acquirer_country_code (str): The 3 letter ISO 4217 country code for the country transactions are originating from.. [optional]  # noqa: E501
            acquiring_bin (str): The Bank Identification Number (BIN) the `Processor` is registered under with Visa Direct.. [optional]  # noqa: E501
            allow_credit_for_partner (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            available_countries (List[Country]): Details the countries the `Processor` is avalible in.. [optional]  # noqa: E501
            business_application_id (str): The ID of the `Application` linked to the `Processor`.. [optional]  # noqa: E501
            class_key_identifier (str): Field used by processor to communicate with Finix.. [optional]  # noqa: E501
            config (ProcessorSystemConfigConfig): [optional]  # noqa: E501
            default_currencies (List[Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            disable_ppgs (bool): Set to **true** to enables the option to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            fee_program_indicator (str): Details the price of a Visa Direct payout.. [optional]  # noqa: E501
            gateway_proxy_certificate (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_host (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_password (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_port (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_username (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            key_store_password (str): The password for the Java Keystore that stores the private keys and cert.pem files needed to process transactions using Visa Direct.. [optional]  # noqa: E501
            key_store_path (str): The path in AWS where the Java Keystore that stores the private keys and cert.pem files are and use to transact using Visa Direct.. [optional]  # noqa: E501
            merchant_pseudo_aba_number (str): A unique ID that's provided when a `Processor` signs up for Push Payment Gateway transactions (PPGS). PPGS allows you to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            online_credit_processing (bool): Details if the `Processor` can handle online credit transactions.. [optional]  # noqa: E501
            online_debit_processing (bool): Details if the `Processor` can handle online debit transactions.. [optional]  # noqa: E501
            password (str): The password found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            private_key_password (str): The password that was used to encrypt the private key that is contained in the Java Keystore.. [optional]  # noqa: E501
            processor_sequence_limit (int): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            pseudo_batch_push (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            source_of_funds (str): Specific code that reflects the use case (e.g. funds disbursement, money transfer, etc.). For a full list of codes, see the following [list from Visa](https://developer.visa.com/request_response_codes#source_of_funds).. [optional]  # noqa: E501
            user_id (str): The user ID found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            visa_acceptance_cloud_key_store_path (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_password (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_url (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_user_id (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
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
            acquirer_country_code (str): The 3 letter ISO 4217 country code for the country transactions are originating from.. [optional]  # noqa: E501
            acquiring_bin (str): The Bank Identification Number (BIN) the `Processor` is registered under with Visa Direct.. [optional]  # noqa: E501
            allow_credit_for_partner (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            available_countries (List[Country]): Details the countries the `Processor` is avalible in.. [optional]  # noqa: E501
            business_application_id (str): The ID of the `Application` linked to the `Processor`.. [optional]  # noqa: E501
            class_key_identifier (str): Field used by processor to communicate with Finix.. [optional]  # noqa: E501
            config (ProcessorSystemConfigConfig): [optional]  # noqa: E501
            default_currencies (List[Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            disable_ppgs (bool): Set to **true** to enables the option to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            fee_program_indicator (str): Details the price of a Visa Direct payout.. [optional]  # noqa: E501
            gateway_proxy_certificate (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_host (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_password (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_port (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            gateway_proxy_username (str): Used if the Gateway needs a proxy. Not applicable to Visa Direct.. [optional]  # noqa: E501
            key_store_password (str): The password for the Java Keystore that stores the private keys and cert.pem files needed to process transactions using Visa Direct.. [optional]  # noqa: E501
            key_store_path (str): The path in AWS where the Java Keystore that stores the private keys and cert.pem files are and use to transact using Visa Direct.. [optional]  # noqa: E501
            merchant_pseudo_aba_number (str): A unique ID that's provided when a `Processor` signs up for Push Payment Gateway transactions (PPGS). PPGS allows you to push payments to other U.S. debit networks using our Visa Direct integration.. [optional]  # noqa: E501
            online_credit_processing (bool): Details if the `Processor` can handle online credit transactions.. [optional]  # noqa: E501
            online_debit_processing (bool): Details if the `Processor` can handle online debit transactions.. [optional]  # noqa: E501
            password (str): The password found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            private_key_password (str): The password that was used to encrypt the private key that is contained in the Java Keystore.. [optional]  # noqa: E501
            processor_sequence_limit (int): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            pseudo_batch_push (bool): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            source_of_funds (str): Specific code that reflects the use case (e.g. funds disbursement, money transfer, etc.). For a full list of codes, see the following [list from Visa](https://developer.visa.com/request_response_codes#source_of_funds).. [optional]  # noqa: E501
            user_id (str): The user ID found in the credentials section of the Visa Developer Portal (VDP) project. This is needed to connect to Visa Direct.. [optional]  # noqa: E501
            visa_acceptance_cloud_key_store_path (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_password (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_url (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
            visa_acceptance_cloud_user_id (str): Field used by Finix and processor to handle transactions.. [optional]  # noqa: E501
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
