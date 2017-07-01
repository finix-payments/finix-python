from base import TestCase

from finix import forms
from finix.mimes import Json

from test_applications import TestApplications
from test_bank_accounts import TestBankAccount
from test_identities import TestIdentities



class TestMerchants(TestCase):

    def test_merchants(self):
        api = self.platform_api
        TestApplications.create_application(api)


        identity = TestIdentities.create_identity(api)
        bank_account = TestBankAccount.create_bank_account(api, identity_id=identity.id)

        form = forms.merchants.Create(
            tags=dict(key_1='value_1'),
            processor=None

        )
        merchant = api.identities.id(identity.id).merchants.post(form)

        # merchant2 = api.merchants.id(merchant.id).get()

        # print Json.encode(merchant)

        # self.assertEqual(merchant.id, merchant2.id)

