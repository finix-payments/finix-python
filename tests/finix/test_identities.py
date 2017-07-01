from base import TestCase

from finix import enums
from finix import forms
from finix.mimes import Json


class TestIdentities(TestCase):

    @classmethod
    def create_identity(cls, api):
        form = forms.identities.Create(
            tags=dict(application_name='test app'),
            entity=dict(
                first_name='dwayne',
                last_name='Sunkhronos',
                has_accepted_creditCards_previously=True,
                email='dwayne@gmail.com',
                tax_id='1234567',
                annual_card_volume='10000000',
                default_statement_descriptor='JS',
                url='http://www.juiceshop.com',
                mcc='0742',
                personal_address=dict(
                    city="San Mateo",
                    country="USA",
                    region="CA",
                    line2="Apartment 7",
                    line1="741 Douglass St",
                    postal_code="94114",
                ),
                dob=dict(
                    year="1978",
                    day="27",
                    month="6",
                ),
                phone='1234567890',
                principal_percentage_ownership=100,
                doing_business_as='juice shop',
                business_phone='7145453213',
                business_tax_id='1234567',
                max_transaction_amount=1000000,
                business_type=enums.BusinessType.INDIVIDUAL_SOLE_PROPRIETORSHIP,
                ownership_type=enums.OwnershipType.PRIVATE,
                business_name='juice shop',
                business_address=dict(
                    city="San Mateo",
                    country="USA",
                    region="CA",
                    line2="Apartment 7",
                    line1="741 Douglass St",
                    postal_code="94114",
                ),
                user="USjtNwkqzupoEXfQD271aQcB",
                title='CEO',
                short_business_name='Juice',
                incorporation_date=dict(
                    year="1978",
                    day="27",
                    month="6",
                ),
            ),

        )
        return api.identities.post(form)

    def test_identities(self):
        api = self.platform_api
        identity = self.create_identity(api)
        identity2 = api.identities.id(identity.id).get()

        print Json.encode(identity)

        self.assertEqual(identity.id, identity2.id)
