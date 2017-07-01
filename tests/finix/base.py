import unittest

from finix import ApiClient
from finix import enums
from finix import forms


class TestCase(unittest.TestCase):

    def setUp(self):
        url = 'https://api-staging.finix.io'
        self.url = url
        self.unauthenticated_api = ApiClient(url=url, user=None, password=None)

        # Create an admin user without authenticating to the API
        form = forms.users.Create(
            role=enums.UserRoles.ROLE_ADMIN,
            enabled=True,
            tags={'type': 'admin'}
        )
        admin_user = self.unauthenticated_api.users.post(form)

        # Instantiate a new API client using our newly created admin credentials
        self.admin_api = ApiClient(url=url, user=admin_user.id, password=admin_user.password)

        # platform api
        form = forms.users.Create(role=enums.UserRoles.ROLE_PLATFORM)
        platform_user = self.admin_api.users.post(form)
        self.platform_api = ApiClient(url=url, user=platform_user.id, password=platform_user.password)

        # partner api
        form = forms.users.Create(role=enums.UserRoles.ROLE_PARTNER)
        partner_user = self.admin_api.users.post(form)
        self.partner_api = ApiClient(url=url, user=partner_user.id, password=partner_user.password)

        # merchant api
        form = forms.users.Create(role=enums.UserRoles.ROLE_MERCHANT)
        merchant_user = self.admin_api.users.post(form)
        self.merchant_api = ApiClient(url=url, user=merchant_user.id, password=merchant_user.password)
