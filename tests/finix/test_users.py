from unittest import TestCase

from finix import enums
from finix import forms
from finix import ApiClient
from finix.resources import User


class TestUsers(TestCase):

    def test_suite(self):

        url = 'https://api-staging.finix.io'
        api = ApiClient(url=url, user=None, password=None)

        # Create an admin user without authenticating to the API
        form = forms.users.Create(
            role=enums.UserRoles.ROLE_ADMIN,
            enabled=True,
            tags={'type': 'admin'}
        )
        user = api.users.post(form)

        # Instantiate a new API client using our newly created admin credentials
        api = ApiClient(url=url, user=user.id, password=user.password)

        # Fetch /users index
        page = api.users.get()
        self.assertEqual(page.page.count, 1)
        for user in page.contents:
            print user.id
            print user.role
            print user.created_at

        # Fetch /users/<id>
        api_user = api.users.id(user.id).get()
        self.assertEqual(user.id, api_user.id)

        form = forms.users.Create(
            role=enums.UserRoles.ROLE_PLATFORM
        )
        platform_user = api.users.post(form)
        self.assertEqual(platform_user.role, 'ROLE_PLATFORM')
