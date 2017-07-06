from base import TestCase

from finix import enums
from finix import forms
from finix import ApiClient
from finix.mimes import Json


class TestApplications(TestCase):

    @classmethod
    def create_application(cls, api):
        form = forms.applications.Create(
            tags=dict(application_name='test app'),
            entity=dict(
                doing_business_as='juice shop',
                business_phone='7145453213',
                business_name='juice shop',
                business_tax_id='1234567',
                max_transaction_amount=1000000,
                business_type=enums.BusinessType.INDIVIDUAL_SOLE_PROPRIETORSHIP,

                business_address=dict(
                    city="San Mateo",
                    country="USA",
                    region="CA",
                    line2="Apartment 7",
                    line1="741 Douglass St",
                    postal_code="94114",
                ),
            ),
            user="USjtNwkqzupoEXfQD271aQcB",
            title='CEO',
            first_name='dwayne',
            last_name='Sunkhronos',
            email='dwayne@gmail.com',
            phone='7145453213',
            tax_id='1234567',
            personal_address=dict(
                city="San Mateo",
                country="USA",
                region="CA",
                line2="Apartment 7",
                line1="741 Douglass St",
                postal_code="94114",
            ),
            mcc='0742',
            dob= dict(
                year= "1978",
                day="27",
                month="6",
            ),
            has_accepted_creditCards_previously=True,
            url='http://www.juiceshop.com',
            annual_card_volume='10000000',
            default_statement_descriptor='JS',
            short_business_name='Juice',
            incorporation_date=dict(
                year= "1978",
                day="27",
                month="6",
            ),
            principal_percentage_ownership='100',
            ownership_type = enums.OwnershipType.PRIVATE,
        )
        return api.applications.post(form)

    @classmethod
    def create_application_user(self):
        api = self.platform_api
        form = forms.applications.CreateApplicationUser.Create(tags=dict(application_name='test app python'))
        return api.applications.post(form)

    def test_applications(self):
        api = self.platform_api

        application = self.create_application(api)
        application2 = api.applications.id(application.id).get()

        print Json.encode(application)
        self.assertEqual(application.id, application2.id)
        updated_application = application.enable_processing()

        application_with_enabled_processor = application.register_processor()

        # how can i make an api call w/ a nested resource -
        # application_user = api.applications.id(application.id)
        # application_user = api.applications.id(application.id)

        print "#################################"
        # print application_user
        print "#################################"
        print application_with_enabled_processor

        self.assertTrue(updated_application.processing_enabled)
        # self.assertEqual('DUMMY_V1', application_with_enabled_processor.type)



