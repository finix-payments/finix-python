from __future__ import unicode_literals


class Enum(list):

    def __init__(self, *args, **kwargs):
        for arg in args:
            kwargs[arg] = arg
        super(Enum, self).__init__(kwargs.values())
        for key, value in kwargs.iteritems():
            setattr(self, key, value)


UserRoles = Enum(
    'ROLE_ADMIN',
    'ROLE_PLATFORM',
    'ROLE_PARTNER',
    'ROLE_MERCHANT',
)


BusinessType = Enum(
    'INDIVIDUAL_SOLE_PROPRIETORSHIP',
    'CORPORATION',
    'LIMITED_LIABILITY_COMPANY',
    'PARTNERSHIP',
    'LIMITED_PARTNERSHIP',
    'GENERAL_PARTNERSHIP',
    'ASSOCIATION_ESTATE_TRUST',
    'TAX_EXEMPT_ORGANIZATION',
    'INTERNATIONAL_ORGANIZATION',
    'GOVERNMENT_AGENCY',
    'JOINT_VENTURE',
)

OwnershipType = Enum(
    'PUBLIC',
    'PRIVATE',
)