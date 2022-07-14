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
    from finix.model.processor_application_config_configuration_templates import ProcessorApplicationConfigConfigurationTemplates
    globals()['Country'] = Country
    globals()['Currency'] = Currency
    globals()['ProcessorApplicationConfigConfigurationTemplates'] = ProcessorApplicationConfigConfigurationTemplates


class ProcessorApplicationConfig(ModelNormal):
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
        ('allowed_business_application_ids',): {
            'AA': "AA",
            'BB': "BB",
            'BI': "BI",
            'CP': "CP",
            'FD': "FD",
            'FT': "FT",
            'GD': "GD",
            'GP': "GP",
            'LO': "LO",
            'CI': "CI",
            'CO': "CO",
            'MP': "MP",
            'MD': "MD",
            'OG': "OG",
            'PD': "PD",
            'PP': "PP",
            'TU': "TU",
            'WT': "WT",
        },
        ('default_mcc',): {
            '0742': "0742",
            '0763': "0763",
            '0780': "0780",
            '1520': "1520",
            '1711': "1711",
            '1731': "1731",
            '1740': "1740",
            '1750': "1750",
            '1761': "1761",
            '1771': "1771",
            '1799': "1799",
            '2741': "2741",
            '2791': "2791",
            '2842': "2842",
            '3000': "3000",
            '3001': "3001",
            '3002': "3002",
            '3003': "3003",
            '3004': "3004",
            '3005': "3005",
            '3006': "3006",
            '3007': "3007",
            '3008': "3008",
            '3009': "3009",
            '3010': "3010",
            '3011': "3011",
            '3012': "3012",
            '3013': "3013",
            '3014': "3014",
            '3015': "3015",
            '3016': "3016",
            '3017': "3017",
            '3018': "3018",
            '3019': "3019",
            '3020': "3020",
            '3021': "3021",
            '3022': "3022",
            '3023': "3023",
            '3024': "3024",
            '3025': "3025",
            '3026': "3026",
            '3027': "3027",
            '3028': "3028",
            '3029': "3029",
            '3030': "3030",
            '3031': "3031",
            '3032': "3032",
            '3033': "3033",
            '3034': "3034",
            '3035': "3035",
            '3036': "3036",
            '3037': "3037",
            '3038': "3038",
            '3039': "3039",
            '3040': "3040",
            '3041': "3041",
            '3042': "3042",
            '3043': "3043",
            '3044': "3044",
            '3045': "3045",
            '3046': "3046",
            '3047': "3047",
            '3048': "3048",
            '3049': "3049",
            '3050': "3050",
            '3051': "3051",
            '3052': "3052",
            '3053': "3053",
            '3054': "3054",
            '3055': "3055",
            '3056': "3056",
            '3057': "3057",
            '3058': "3058",
            '3059': "3059",
            '3060': "3060",
            '3061': "3061",
            '3062': "3062",
            '3063': "3063",
            '3064': "3064",
            '3065': "3065",
            '3066': "3066",
            '3067': "3067",
            '3068': "3068",
            '3069': "3069",
            '3070': "3070",
            '3071': "3071",
            '3072': "3072",
            '3073': "3073",
            '3074': "3074",
            '3075': "3075",
            '3076': "3076",
            '3077': "3077",
            '3078': "3078",
            '3079': "3079",
            '3080': "3080",
            '3081': "3081",
            '3082': "3082",
            '3083': "3083",
            '3084': "3084",
            '3085': "3085",
            '3086': "3086",
            '3087': "3087",
            '3088': "3088",
            '3089': "3089",
            '3090': "3090",
            '3091': "3091",
            '3092': "3092",
            '3093': "3093",
            '3094': "3094",
            '3095': "3095",
            '3096': "3096",
            '3097': "3097",
            '3098': "3098",
            '3099': "3099",
            '3100': "3100",
            '3101': "3101",
            '3102': "3102",
            '3103': "3103",
            '3104': "3104",
            '3105': "3105",
            '3106': "3106",
            '3107': "3107",
            '3108': "3108",
            '3109': "3109",
            '3110': "3110",
            '3111': "3111",
            '3112': "3112",
            '3113': "3113",
            '3114': "3114",
            '3115': "3115",
            '3116': "3116",
            '3117': "3117",
            '3118': "3118",
            '3119': "3119",
            '3120': "3120",
            '3121': "3121",
            '3122': "3122",
            '3123': "3123",
            '3124': "3124",
            '3125': "3125",
            '3126': "3126",
            '3127': "3127",
            '3128': "3128",
            '3129': "3129",
            '3130': "3130",
            '3131': "3131",
            '3132': "3132",
            '3133': "3133",
            '3134': "3134",
            '3135': "3135",
            '3136': "3136",
            '3137': "3137",
            '3138': "3138",
            '3139': "3139",
            '3140': "3140",
            '3141': "3141",
            '3142': "3142",
            '3143': "3143",
            '3144': "3144",
            '3145': "3145",
            '3146': "3146",
            '3147': "3147",
            '3148': "3148",
            '3149': "3149",
            '3150': "3150",
            '3151': "3151",
            '3152': "3152",
            '3153': "3153",
            '3154': "3154",
            '3155': "3155",
            '3156': "3156",
            '3157': "3157",
            '3158': "3158",
            '3159': "3159",
            '3160': "3160",
            '3161': "3161",
            '3162': "3162",
            '3163': "3163",
            '3164': "3164",
            '3165': "3165",
            '3166': "3166",
            '3167': "3167",
            '3168': "3168",
            '3169': "3169",
            '3170': "3170",
            '3171': "3171",
            '3172': "3172",
            '3173': "3173",
            '3174': "3174",
            '3175': "3175",
            '3176': "3176",
            '3177': "3177",
            '3178': "3178",
            '3179': "3179",
            '3180': "3180",
            '3181': "3181",
            '3182': "3182",
            '3183': "3183",
            '3184': "3184",
            '3185': "3185",
            '3186': "3186",
            '3187': "3187",
            '3188': "3188",
            '3189': "3189",
            '3190': "3190",
            '3191': "3191",
            '3192': "3192",
            '3193': "3193",
            '3194': "3194",
            '3195': "3195",
            '3196': "3196",
            '3197': "3197",
            '3198': "3198",
            '3199': "3199",
            '3200': "3200",
            '3201': "3201",
            '3202': "3202",
            '3203': "3203",
            '3204': "3204",
            '3205': "3205",
            '3206': "3206",
            '3207': "3207",
            '3208': "3208",
            '3209': "3209",
            '3210': "3210",
            '3211': "3211",
            '3212': "3212",
            '3213': "3213",
            '3214': "3214",
            '3215': "3215",
            '3216': "3216",
            '3217': "3217",
            '3218': "3218",
            '3219': "3219",
            '3220': "3220",
            '3221': "3221",
            '3222': "3222",
            '3223': "3223",
            '3224': "3224",
            '3225': "3225",
            '3226': "3226",
            '3227': "3227",
            '3228': "3228",
            '3229': "3229",
            '3230': "3230",
            '3231': "3231",
            '3232': "3232",
            '3233': "3233",
            '3234': "3234",
            '3235': "3235",
            '3236': "3236",
            '3237': "3237",
            '3238': "3238",
            '3239': "3239",
            '3240': "3240",
            '3241': "3241",
            '3242': "3242",
            '3243': "3243",
            '3244': "3244",
            '3245': "3245",
            '3246': "3246",
            '3247': "3247",
            '3248': "3248",
            '3249': "3249",
            '3250': "3250",
            '3251': "3251",
            '3252': "3252",
            '3253': "3253",
            '3254': "3254",
            '3255': "3255",
            '3256': "3256",
            '3257': "3257",
            '3258': "3258",
            '3259': "3259",
            '3260': "3260",
            '3261': "3261",
            '3262': "3262",
            '3263': "3263",
            '3264': "3264",
            '3265': "3265",
            '3266': "3266",
            '3267': "3267",
            '3268': "3268",
            '3269': "3269",
            '3270': "3270",
            '3271': "3271",
            '3272': "3272",
            '3273': "3273",
            '3274': "3274",
            '3275': "3275",
            '3276': "3276",
            '3277': "3277",
            '3278': "3278",
            '3279': "3279",
            '3280': "3280",
            '3281': "3281",
            '3282': "3282",
            '3283': "3283",
            '3284': "3284",
            '3285': "3285",
            '3286': "3286",
            '3287': "3287",
            '3288': "3288",
            '3289': "3289",
            '3290': "3290",
            '3291': "3291",
            '3292': "3292",
            '3293': "3293",
            '3294': "3294",
            '3295': "3295",
            '3296': "3296",
            '3297': "3297",
            '3298': "3298",
            '3299': "3299",
            '3351': "3351",
            '3352': "3352",
            '3353': "3353",
            '3354': "3354",
            '3355': "3355",
            '3356': "3356",
            '3357': "3357",
            '3358': "3358",
            '3359': "3359",
            '3360': "3360",
            '3361': "3361",
            '3362': "3362",
            '3363': "3363",
            '3364': "3364",
            '3365': "3365",
            '3366': "3366",
            '3367': "3367",
            '3368': "3368",
            '3369': "3369",
            '3370': "3370",
            '3371': "3371",
            '3372': "3372",
            '3373': "3373",
            '3374': "3374",
            '3375': "3375",
            '3376': "3376",
            '3377': "3377",
            '3378': "3378",
            '3379': "3379",
            '3380': "3380",
            '3381': "3381",
            '3382': "3382",
            '3383': "3383",
            '3384': "3384",
            '3385': "3385",
            '3386': "3386",
            '3387': "3387",
            '3388': "3388",
            '3389': "3389",
            '3390': "3390",
            '3391': "3391",
            '3392': "3392",
            '3393': "3393",
            '3394': "3394",
            '3395': "3395",
            '3396': "3396",
            '3397': "3397",
            '3398': "3398",
            '3399': "3399",
            '3400': "3400",
            '3401': "3401",
            '3402': "3402",
            '3403': "3403",
            '3404': "3404",
            '3405': "3405",
            '3406': "3406",
            '3407': "3407",
            '3408': "3408",
            '3409': "3409",
            '3410': "3410",
            '3411': "3411",
            '3412': "3412",
            '3413': "3413",
            '3414': "3414",
            '3415': "3415",
            '3416': "3416",
            '3417': "3417",
            '3418': "3418",
            '3419': "3419",
            '3420': "3420",
            '3421': "3421",
            '3422': "3422",
            '3423': "3423",
            '3424': "3424",
            '3425': "3425",
            '3426': "3426",
            '3427': "3427",
            '3428': "3428",
            '3429': "3429",
            '3430': "3430",
            '3431': "3431",
            '3432': "3432",
            '3433': "3433",
            '3434': "3434",
            '3435': "3435",
            '3436': "3436",
            '3437': "3437",
            '3438': "3438",
            '3439': "3439",
            '3440': "3440",
            '3441': "3441",
            '3501': "3501",
            '3502': "3502",
            '3503': "3503",
            '3504': "3504",
            '3505': "3505",
            '3506': "3506",
            '3507': "3507",
            '3508': "3508",
            '3509': "3509",
            '3510': "3510",
            '3511': "3511",
            '3512': "3512",
            '3513': "3513",
            '3514': "3514",
            '3515': "3515",
            '3516': "3516",
            '3517': "3517",
            '3518': "3518",
            '3519': "3519",
            '3520': "3520",
            '3521': "3521",
            '3522': "3522",
            '3523': "3523",
            '3524': "3524",
            '3525': "3525",
            '3526': "3526",
            '3527': "3527",
            '3528': "3528",
            '3529': "3529",
            '3530': "3530",
            '3531': "3531",
            '3532': "3532",
            '3533': "3533",
            '3534': "3534",
            '3535': "3535",
            '3536': "3536",
            '3537': "3537",
            '3538': "3538",
            '3539': "3539",
            '3540': "3540",
            '3541': "3541",
            '3542': "3542",
            '3543': "3543",
            '3544': "3544",
            '3545': "3545",
            '3546': "3546",
            '3547': "3547",
            '3548': "3548",
            '3549': "3549",
            '3550': "3550",
            '3551': "3551",
            '3552': "3552",
            '3553': "3553",
            '3554': "3554",
            '3555': "3555",
            '3556': "3556",
            '3557': "3557",
            '3558': "3558",
            '3559': "3559",
            '3560': "3560",
            '3561': "3561",
            '3562': "3562",
            '3563': "3563",
            '3564': "3564",
            '3565': "3565",
            '3566': "3566",
            '3567': "3567",
            '3568': "3568",
            '3569': "3569",
            '3570': "3570",
            '3571': "3571",
            '3572': "3572",
            '3573': "3573",
            '3574': "3574",
            '3575': "3575",
            '3576': "3576",
            '3577': "3577",
            '3578': "3578",
            '3579': "3579",
            '3580': "3580",
            '3581': "3581",
            '3582': "3582",
            '3583': "3583",
            '3584': "3584",
            '3585': "3585",
            '3586': "3586",
            '3587': "3587",
            '3588': "3588",
            '3589': "3589",
            '3590': "3590",
            '3591': "3591",
            '3592': "3592",
            '3593': "3593",
            '3594': "3594",
            '3595': "3595",
            '3596': "3596",
            '3597': "3597",
            '3598': "3598",
            '3599': "3599",
            '3600': "3600",
            '3601': "3601",
            '3602': "3602",
            '3603': "3603",
            '3604': "3604",
            '3605': "3605",
            '3606': "3606",
            '3607': "3607",
            '3608': "3608",
            '3609': "3609",
            '3610': "3610",
            '3611': "3611",
            '3612': "3612",
            '3613': "3613",
            '3614': "3614",
            '3615': "3615",
            '3616': "3616",
            '3617': "3617",
            '3618': "3618",
            '3619': "3619",
            '3620': "3620",
            '3621': "3621",
            '3622': "3622",
            '3623': "3623",
            '3624': "3624",
            '3625': "3625",
            '3626': "3626",
            '3627': "3627",
            '3628': "3628",
            '3629': "3629",
            '3630': "3630",
            '3631': "3631",
            '3632': "3632",
            '3633': "3633",
            '3634': "3634",
            '3635': "3635",
            '3636': "3636",
            '3637': "3637",
            '3638': "3638",
            '3639': "3639",
            '3640': "3640",
            '3641': "3641",
            '3642': "3642",
            '3643': "3643",
            '3644': "3644",
            '3645': "3645",
            '3646': "3646",
            '3647': "3647",
            '3648': "3648",
            '3649': "3649",
            '3650': "3650",
            '3651': "3651",
            '3652': "3652",
            '3653': "3653",
            '3654': "3654",
            '3655': "3655",
            '3656': "3656",
            '3657': "3657",
            '3658': "3658",
            '3659': "3659",
            '3660': "3660",
            '3661': "3661",
            '3662': "3662",
            '3663': "3663",
            '3664': "3664",
            '3665': "3665",
            '3666': "3666",
            '3667': "3667",
            '3668': "3668",
            '3669': "3669",
            '3670': "3670",
            '3671': "3671",
            '3672': "3672",
            '3673': "3673",
            '3674': "3674",
            '3675': "3675",
            '3676': "3676",
            '3677': "3677",
            '3678': "3678",
            '3679': "3679",
            '3680': "3680",
            '3681': "3681",
            '3682': "3682",
            '3683': "3683",
            '3684': "3684",
            '3685': "3685",
            '3686': "3686",
            '3687': "3687",
            '3688': "3688",
            '3689': "3689",
            '3690': "3690",
            '3691': "3691",
            '3692': "3692",
            '3693': "3693",
            '3694': "3694",
            '3695': "3695",
            '3696': "3696",
            '3697': "3697",
            '3698': "3698",
            '3699': "3699",
            '3700': "3700",
            '3701': "3701",
            '3702': "3702",
            '3703': "3703",
            '3704': "3704",
            '3705': "3705",
            '3706': "3706",
            '3707': "3707",
            '3708': "3708",
            '3709': "3709",
            '3710': "3710",
            '3711': "3711",
            '3712': "3712",
            '3713': "3713",
            '3714': "3714",
            '3715': "3715",
            '3716': "3716",
            '3717': "3717",
            '3718': "3718",
            '3719': "3719",
            '3720': "3720",
            '3721': "3721",
            '3722': "3722",
            '3723': "3723",
            '3724': "3724",
            '3725': "3725",
            '3726': "3726",
            '3727': "3727",
            '3728': "3728",
            '3729': "3729",
            '3730': "3730",
            '3731': "3731",
            '3732': "3732",
            '3733': "3733",
            '3734': "3734",
            '3735': "3735",
            '3736': "3736",
            '3737': "3737",
            '3738': "3738",
            '3739': "3739",
            '3740': "3740",
            '3741': "3741",
            '3742': "3742",
            '3743': "3743",
            '3744': "3744",
            '3745': "3745",
            '3746': "3746",
            '3747': "3747",
            '3748': "3748",
            '3749': "3749",
            '3750': "3750",
            '3751': "3751",
            '3752': "3752",
            '3753': "3753",
            '3754': "3754",
            '3755': "3755",
            '3756': "3756",
            '3757': "3757",
            '3758': "3758",
            '3759': "3759",
            '3760': "3760",
            '3761': "3761",
            '3762': "3762",
            '3763': "3763",
            '3764': "3764",
            '3765': "3765",
            '3766': "3766",
            '3767': "3767",
            '3768': "3768",
            '3769': "3769",
            '3770': "3770",
            '3771': "3771",
            '3772': "3772",
            '3773': "3773",
            '3774': "3774",
            '3775': "3775",
            '3776': "3776",
            '3777': "3777",
            '3778': "3778",
            '3779': "3779",
            '3780': "3780",
            '3781': "3781",
            '3782': "3782",
            '3783': "3783",
            '3784': "3784",
            '3785': "3785",
            '3786': "3786",
            '3787': "3787",
            '3788': "3788",
            '3789': "3789",
            '3790': "3790",
            '3816': "3816",
            '3835': "3835",
            '4011': "4011",
            '4111': "4111",
            '4112': "4112",
            '4119': "4119",
            '4121': "4121",
            '4131': "4131",
            '4214': "4214",
            '4215': "4215",
            '4225': "4225",
            '4411': "4411",
            '4457': "4457",
            '4468': "4468",
            '4511': "4511",
            '4582': "4582",
            '4722': "4722",
            '4723': "4723",
            '4784': "4784",
            '4789': "4789",
            '4812': "4812",
            '4814': "4814",
            '4815': "4815",
            '4816': "4816",
            '4821': "4821",
            '4829': "4829",
            '4899': "4899",
            '4900': "4900",
            '5013': "5013",
            '5021': "5021",
            '5039': "5039",
            '5044': "5044",
            '5045': "5045",
            '5046': "5046",
            '5047': "5047",
            '5051': "5051",
            '5065': "5065",
            '5072': "5072",
            '5074': "5074",
            '5085': "5085",
            '5094': "5094",
            '5099': "5099",
            '5111': "5111",
            '5122': "5122",
            '5131': "5131",
            '5137': "5137",
            '5139': "5139",
            '5169': "5169",
            '5172': "5172",
            '5192': "5192",
            '5193': "5193",
            '5198': "5198",
            '5199': "5199",
            '5200': "5200",
            '5211': "5211",
            '5231': "5231",
            '5251': "5251",
            '5261': "5261",
            '5271': "5271",
            '5300': "5300",
            '5309': "5309",
            '5310': "5310",
            '5311': "5311",
            '5331': "5331",
            '5399': "5399",
            '5411': "5411",
            '5422': "5422",
            '5441': "5441",
            '5451': "5451",
            '5462': "5462",
            '5499': "5499",
            '5511': "5511",
            '5521': "5521",
            '5531': "5531",
            '5532': "5532",
            '5533': "5533",
            '5541': "5541",
            '5542': "5542",
            '5551': "5551",
            '5561': "5561",
            '5571': "5571",
            '5592': "5592",
            '5598': "5598",
            '5599': "5599",
            '5611': "5611",
            '5621': "5621",
            '5631': "5631",
            '5641': "5641",
            '5651': "5651",
            '5655': "5655",
            '5661': "5661",
            '5681': "5681",
            '5691': "5691",
            '5697': "5697",
            '5698': "5698",
            '5699': "5699",
            '5712': "5712",
            '5713': "5713",
            '5714': "5714",
            '5718': "5718",
            '5719': "5719",
            '5722': "5722",
            '5732': "5732",
            '5733': "5733",
            '5734': "5734",
            '5735': "5735",
            '5811': "5811",
            '5812': "5812",
            '5813': "5813",
            '5814': "5814",
            '5815': "5815",
            '5816': "5816",
            '5817': "5817",
            '5818': "5818",
            '5832': "5832",
            '5912': "5912",
            '5921': "5921",
            '5931': "5931",
            '5932': "5932",
            '5933': "5933",
            '5935': "5935",
            '5937': "5937",
            '5940': "5940",
            '5941': "5941",
            '5942': "5942",
            '5943': "5943",
            '5944': "5944",
            '5945': "5945",
            '5946': "5946",
            '5947': "5947",
            '5948': "5948",
            '5949': "5949",
            '5950': "5950",
            '5960': "5960",
            '5961': "5961",
            '5962': "5962",
            '5963': "5963",
            '5964': "5964",
            '5965': "5965",
            '5966': "5966",
            '5967': "5967",
            '5968': "5968",
            '5969': "5969",
            '5970': "5970",
            '5971': "5971",
            '5972': "5972",
            '5973': "5973",
            '5975': "5975",
            '5976': "5976",
            '5977': "5977",
            '5978': "5978",
            '5983': "5983",
            '5992': "5992",
            '5993': "5993",
            '5994': "5994",
            '5995': "5995",
            '5996': "5996",
            '5997': "5997",
            '5998': "5998",
            '5999': "5999",
            '6010': "6010",
            '6011': "6011",
            '6012': "6012",
            '6051': "6051",
            '6211': "6211",
            '6300': "6300",
            '6381': "6381",
            '6399': "6399",
            '6513': "6513",
            '7011': "7011",
            '7012': "7012",
            '7032': "7032",
            '7033': "7033",
            '7210': "7210",
            '7211': "7211",
            '7216': "7216",
            '7217': "7217",
            '7221': "7221",
            '7230': "7230",
            '7251': "7251",
            '7261': "7261",
            '7273': "7273",
            '7276': "7276",
            '7277': "7277",
            '7278': "7278",
            '7296': "7296",
            '7297': "7297",
            '7298': "7298",
            '7299': "7299",
            '7311': "7311",
            '7321': "7321",
            '7332': "7332",
            '7333': "7333",
            '7338': "7338",
            '7339': "7339",
            '7342': "7342",
            '7349': "7349",
            '7361': "7361",
            '7372': "7372",
            '7375': "7375",
            '7379': "7379",
            '7392': "7392",
            '7393': "7393",
            '7394': "7394",
            '7395': "7395",
            '7399': "7399",
            '7511': "7511",
            '7512': "7512",
            '7513': "7513",
            '7519': "7519",
            '7523': "7523",
            '7531': "7531",
            '7534': "7534",
            '7535': "7535",
            '7538': "7538",
            '7542': "7542",
            '7549': "7549",
            '7622': "7622",
            '7623': "7623",
            '7629': "7629",
            '7631': "7631",
            '7641': "7641",
            '7692': "7692",
            '7699': "7699",
            '7800': "7800",
            '7801': "7801",
            '7802': "7802",
            '7829': "7829",
            '7832': "7832",
            '7841': "7841",
            '7911': "7911",
            '7922': "7922",
            '7929': "7929",
            '7932': "7932",
            '7933': "7933",
            '7941': "7941",
            '7991': "7991",
            '7992': "7992",
            '7993': "7993",
            '7994': "7994",
            '7995': "7995",
            '7996': "7996",
            '7997': "7997",
            '7998': "7998",
            '7999': "7999",
            '8011': "8011",
            '8021': "8021",
            '8031': "8031",
            '8041': "8041",
            '8042': "8042",
            '8043': "8043",
            '8044': "8044",
            '8049': "8049",
            '8050': "8050",
            '8062': "8062",
            '8071': "8071",
            '8099': "8099",
            '8111': "8111",
            '8211': "8211",
            '8220': "8220",
            '8241': "8241",
            '8244': "8244",
            '8249': "8249",
            '8299': "8299",
            '8351': "8351",
            '8398': "8398",
            '8641': "8641",
            '8651': "8651",
            '8661': "8661",
            '8675': "8675",
            '8699': "8699",
            '8734': "8734",
            '8911': "8911",
            '8931': "8931",
            '8999': "8999",
            '9211': "9211",
            '9222': "9222",
            '9223': "9223",
            '9311': "9311",
            '9399': "9399",
            '9402': "9402",
            '9405': "9405",
            '9700': "9700",
            '9701': "9701",
            '9702': "9702",
            '9950': "9950",
        },
        ('moto_eciindicator',): {
            '5': "5",
            '6': "6",
            '7': "7",
            '8': "8",
        },
        ('pan_entry_mode',): {
            '00': "00",
            '01': "01",
            '02': "02",
            '03': "03",
            '04': "04",
            '05': "05",
            '06': "06",
            '07': "07",
            '08': "08",
            '09': "09",
            '10': "10",
            '80': "80",
            '82': "82",
            '83': "83",
            '90': "90",
            '91': "91",
            '95': "95",
        },
        ('pos_condition_code',): {
            '00': "00",
            '01': "01",
            '02': "02",
            '03': "03",
            '05': "05",
            '06': "06",
            '08': "08",
            '10': "10",
            '51': "51",
            '59': "59",
            '71': "71",
            '73': "73",
        },
    }

    validations = {
        ('ach_settlement_delay_days',): {
            'inclusive_minimum': 0,
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
            'ach_settlement_delay_days': (int, none_type,),  # noqa: E501
            'allow_split_payouts': (bool,),  # noqa: E501
            'allowed_business_application_ids': ([str],),  # noqa: E501
            'card_acceptor_id_code': (str,),  # noqa: E501
            'card_acceptor_terminal_id': (str,),  # noqa: E501
            'configuration_templates': (ProcessorApplicationConfigConfigurationTemplates,),  # noqa: E501
            'default_currencies': ([Currency],),  # noqa: E501
            'default_mcc': (str,),  # noqa: E501
            'default_sender_account_number': (str, none_type,),  # noqa: E501
            'default_sender_address': (str, none_type,),  # noqa: E501
            'default_sender_city': (str, none_type,),  # noqa: E501
            'default_sender_country': (Country,),  # noqa: E501
            'default_sender_country_code': (str, none_type,),  # noqa: E501
            'default_sender_county_code': (str, none_type,),  # noqa: E501
            'default_sender_name': (str, none_type,),  # noqa: E501
            'default_sender_state_code': (str, none_type,),  # noqa: E501
            'default_sender_zip_code': (str, none_type,),  # noqa: E501
            'include_colombia_data': (bool,),  # noqa: E501
            'moto_eciindicator': (str,),  # noqa: E501
            'pan_entry_mode': (str,),  # noqa: E501
            'pos_condition_code': (str,),  # noqa: E501
        }

    @cached_property
    def discriminator():
        return None


    attribute_map = {
        'ach_settlement_delay_days': 'ach_settlement_delay_days',  # noqa: E501
        'allow_split_payouts': 'allow_split_payouts',  # noqa: E501
        'allowed_business_application_ids': 'allowed_business_application_ids',  # noqa: E501
        'card_acceptor_id_code': 'card_acceptor_id_code',  # noqa: E501
        'card_acceptor_terminal_id': 'card_acceptor_terminal_id',  # noqa: E501
        'configuration_templates': 'configuration_templates',  # noqa: E501
        'default_currencies': 'default_currencies',  # noqa: E501
        'default_mcc': 'default_mcc',  # noqa: E501
        'default_sender_account_number': 'default_sender_account_number',  # noqa: E501
        'default_sender_address': 'default_sender_address',  # noqa: E501
        'default_sender_city': 'default_sender_city',  # noqa: E501
        'default_sender_country': 'default_sender_country',  # noqa: E501
        'default_sender_country_code': 'default_sender_country_code',  # noqa: E501
        'default_sender_county_code': 'default_sender_county_code',  # noqa: E501
        'default_sender_name': 'default_sender_name',  # noqa: E501
        'default_sender_state_code': 'default_sender_state_code',  # noqa: E501
        'default_sender_zip_code': 'default_sender_zip_code',  # noqa: E501
        'include_colombia_data': 'include_colombia_data',  # noqa: E501
        'moto_eciindicator': 'moto_eciindicator',  # noqa: E501
        'pan_entry_mode': 'pan_entry_mode',  # noqa: E501
        'pos_condition_code': 'pos_condition_code',  # noqa: E501
    }

    read_only_vars = {
    }

    _composed_schemas = {}

    @classmethod
    @convert_js_args_to_python_args
    def _from_openapi_data(cls, *args, **kwargs):  # noqa: E501
        """ProcessorApplicationConfig - a model defined in OpenAPI

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
            ach_settlement_delay_days (int, none_type): Details how days ACH settlments are delayed by.. [optional]  # noqa: E501
            allow_split_payouts (bool): Details if the `Processor` allows split payouts to `Merchants`.. [optional]  # noqa: E501
            allowed_business_application_ids ([str]): Identifies the `Processors` business application type for VisaNet transaction processing.. [optional]  # noqa: E501
            card_acceptor_id_code (str): An ID for the card acceptor (e.g Visa). . [optional]  # noqa: E501
            card_acceptor_terminal_id (str): The ID for the terminal at a card acceptor location.. [optional]  # noqa: E501
            configuration_templates (ProcessorApplicationConfigConfigurationTemplates): [optional]  # noqa: E501
            default_currencies ([Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            default_mcc (str): The Merchant Category Code of the `Merchan. . [optional]  # noqa: E501
            default_sender_account_number (str, none_type): The default account of the sender.. [optional]  # noqa: E501
            default_sender_address (str, none_type): The sender’s address.. [optional]  # noqa: E501
            default_sender_city (str, none_type): The city saved in the sender's address.. [optional]  # noqa: E501
            default_sender_country (Country): [optional]  # noqa: E501
            default_sender_country_code (str, none_type): The sender's 3 letter ISO 4217 currency code.. [optional]  # noqa: E501
            default_sender_county_code (str, none_type): The sender’s county.. [optional]  # noqa: E501
            default_sender_name (str, none_type): The sender’s name.. [optional]  # noqa: E501
            default_sender_state_code (str, none_type): The sender's 2-letter State code.. [optional]  # noqa: E501
            default_sender_zip_code (str, none_type): The sender’s zip code.. [optional]  # noqa: E501
            include_colombia_data (bool): Must be true if transactions are in Colombia where there are different fees.. [optional]  # noqa: E501
            moto_eciindicator (str): Identifies the level of security used in an electronic commerce transaction (only applies to card-present transactions).. [optional]  # noqa: E501
            pan_entry_mode (str): A 2-digit code that identifies the method used to enter the cardholder account number and card expiration date (only applies to card-present transactions).. [optional]  # noqa: E501
            pos_condition_code (str): Contains a code identifying transaction conditions at the point of sale or point of service (only applies to card-present transactions).. [optional]  # noqa: E501
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
        """ProcessorApplicationConfig - a model defined in OpenAPI

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
            ach_settlement_delay_days (int, none_type): Details how days ACH settlments are delayed by.. [optional]  # noqa: E501
            allow_split_payouts (bool): Details if the `Processor` allows split payouts to `Merchants`.. [optional]  # noqa: E501
            allowed_business_application_ids ([str]): Identifies the `Processors` business application type for VisaNet transaction processing.. [optional]  # noqa: E501
            card_acceptor_id_code (str): An ID for the card acceptor (e.g Visa). . [optional]  # noqa: E501
            card_acceptor_terminal_id (str): The ID for the terminal at a card acceptor location.. [optional]  # noqa: E501
            configuration_templates (ProcessorApplicationConfigConfigurationTemplates): [optional]  # noqa: E501
            default_currencies ([Currency]): ISO 4217 3 letter currency code.. [optional]  # noqa: E501
            default_mcc (str): The Merchant Category Code of the `Merchan. . [optional]  # noqa: E501
            default_sender_account_number (str, none_type): The default account of the sender.. [optional]  # noqa: E501
            default_sender_address (str, none_type): The sender’s address.. [optional]  # noqa: E501
            default_sender_city (str, none_type): The city saved in the sender's address.. [optional]  # noqa: E501
            default_sender_country (Country): [optional]  # noqa: E501
            default_sender_country_code (str, none_type): The sender's 3 letter ISO 4217 currency code.. [optional]  # noqa: E501
            default_sender_county_code (str, none_type): The sender’s county.. [optional]  # noqa: E501
            default_sender_name (str, none_type): The sender’s name.. [optional]  # noqa: E501
            default_sender_state_code (str, none_type): The sender's 2-letter State code.. [optional]  # noqa: E501
            default_sender_zip_code (str, none_type): The sender’s zip code.. [optional]  # noqa: E501
            include_colombia_data (bool): Must be true if transactions are in Colombia where there are different fees.. [optional]  # noqa: E501
            moto_eciindicator (str): Identifies the level of security used in an electronic commerce transaction (only applies to card-present transactions).. [optional]  # noqa: E501
            pan_entry_mode (str): A 2-digit code that identifies the method used to enter the cardholder account number and card expiration date (only applies to card-present transactions).. [optional]  # noqa: E501
            pos_condition_code (str): Contains a code identifying transaction conditions at the point of sale or point of service (only applies to card-present transactions).. [optional]  # noqa: E501
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
