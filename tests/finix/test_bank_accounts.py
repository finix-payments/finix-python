import unittest

from base import TestCase

from finix import forms
from finix.mimes import Json

class TestBankAccount(TestCase):

    @classmethod
    def create_bank_account(cls, api, identity_id=None):
        if not identity_id:
            from test_identities import TestIdentities
            identity_id = TestIdentities.create_identity(api).id
        form = forms.bank_account.Create(
            tags=dict(application_name='test app'),
            account_type='SAVINGS',
            name='Frank Serna',
            country='USD',
            bank_code='1233445',
            account_number='1234141',
            type='bank_account',
            identity=identity_id,
        )
        return api.bank_account.post(form)

    def test_bank_account(self):
        api = self.platform_api
        bank_account = TestBankAccount.create_bank_account(api)
        bank_account2 = api.bank_account.id(bank_account.id).get()
        print Json.encode(bank_account)
        self.assertEqual(bank_account.id, bank_account2.id)

