import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USsRhsHYZGBPnQw8CByJyEQW',
        password = '8a14c2f9-d94b-4c72-8f5c-a62908e5b30e',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_merchant(config):
    tmp_client = finix.FinixClient(config)
    req = CreateIdentityRequest(
 	    additional_underwriting_data=CreateIdentityRequestAdditionalUnderwritingData(
	        merchant_agreement_accepted=True,
	        merchant_agreement_ip_address="42.1.1.113",
	        volume_distribution_by_business_type=CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType(
	            other_volume_percentage=0,
	            consumer_to_consumer_volume_percentage=0,
	            business_to_consumer_volume_percentage=0,
	            business_to_business_volume_percentage=100,
	            person_to_person_volume_percentage=0
            ),
	        average_ach_transfer_amount=200000,
	        annual_ach_volume=200000,
	        credit_check_user_agent="Mozilla 5.0(Macintosh; IntelMac OS X 10 _14_6)",
	        refund_policy="MERCHANDISE_EXCHANGE_ONLY",
	        credit_check_timestamp="2021-04-28T16:42:55Z",
	        credit_check_allowed=True,
	        merchant_agreement_timestamp="2021-04-28T16:42:55Z",
	        business_description="BCSB3 vegan cafe",
	        average_card_transfer_amount=200000,
	        credit_check_ip_address="42.1.1.113",
	        merchant_agreement_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)",
	        card_volume_distribution=CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution(
	            card_present_percentage=30,
	            mail_order_telephone_order_percentage=10,
	            ecommerce_percentage=60,
            )
        ),
	    tags=Tags(
	        test_key_100 = "test_val_100"
        ),
	    entity=CreateIdentityRequestEntity(
	        last_name="lbc",
	        max_transaction_amount=12000000,
	        has_accepted_credit_cards_previously=True,
	        default_statement_descriptor="Petes Coffee",
	        personal_address=CreateIdentityRequestEntityPersonalAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 7",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        incorporation_date=CreateIdentityRequestEntityIncorporationDate(
	            year=1978,
	            day=27,
	            month=6
            ),
	        business_address=CreateIdentityRequestEntityBusinessAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 8",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        ownership_type="PRIVATE",
	        first_name="dwayne",
	        title="CEO",
	        business_tax_id="123456789",
	        doing_business_as="Petes Coffee",
	        principal_percentage_ownership=50,
	        email="user@example.org",
	        mcc="0742",
	        phone="1234567890",
	        business_name="Petes Coffee",
	        tax_id="123456789",
	        business_type="INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        business_phone="+1 (408) 756-4497",
	        dob=CreateIdentityRequestEntityDob(
	            year=1978,
	            day=27,
	            month=6
            ),
	        url="www.PetesCoffee.com",
	        annual_card_volume=12000000,
        )
    ) 
    response = tmp_client.identities.create(create_identity_request=req)
    return response


def test_get(config, c_merchant):
    tmp_client = finix.FinixClient(config)
    id = c_merchant.id
    response = tmp_client.identities.get(id)
    assert response.id[:2] == 'ID'
    assert response.entity['mcc'] == '0742'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update(config, c_merchant):
    tmp_client = finix.FinixClient(config)
    id = c_merchant.id
    req = UpdateIdentityRequest(
        tags=Tags(
            test_key_101 = "test_val_101"
        )
    )
    response = tmp_client.identities.update(id, update_identity_request=req)
    assert response.id[:2] == 'ID'
    assert response.entity['mcc'] == '0742'
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateIdentityRequest(
 	    additional_underwriting_data=CreateIdentityRequestAdditionalUnderwritingData(
	        merchant_agreement_accepted=True,
	        merchant_agreement_ip_address="42.1.1.113",
	        volume_distribution_by_business_type=CreateIdentityRequestAdditionalUnderwritingDataVolumeDistributionByBusinessType(
	            other_volume_percentage=0,
	            consumer_to_consumer_volume_percentage=0,
	            business_to_consumer_volume_percentage=0,
	            business_to_business_volume_percentage=100,
	            person_to_person_volume_percentage=0
            ),
	        average_ach_transfer_amount=200000,
	        annual_ach_volume=200000,
	        credit_check_user_agent="Mozilla 5.0(Macintosh; IntelMac OS X 10 _14_6)",
	        refund_policy="MERCHANDISE_EXCHANGE_ONLY",
	        credit_check_timestamp="2021-04-28T16:42:55Z",
	        credit_check_allowed=True,
	        merchant_agreement_timestamp="2021-04-28T16:42:55Z",
	        business_description="BCSB3 vegan cafe",
	        average_card_transfer_amount=200000,
	        credit_check_ip_address="42.1.1.113",
	        merchant_agreement_user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6)",
	        card_volume_distribution=CreateIdentityRequestAdditionalUnderwritingDataCardVolumeDistribution(
	            card_present_percentage=30,
	            mail_order_telephone_order_percentage=10,
	            ecommerce_percentage=60,
            )
        ),
	    tags=Tags(
	        test_key_102 = "test_val_102"
        ),
	    entity=CreateIdentityRequestEntity(
	        last_name="abc",
	        max_transaction_amount=12000000,
	        has_accepted_credit_cards_previously=True,
	        default_statement_descriptor="Petes Coffee",
	        personal_address=CreateIdentityRequestEntityPersonalAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 7",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        incorporation_date=CreateIdentityRequestEntityIncorporationDate(
	            year=1978,
	            day=27,
	            month=6
            ),
	        business_address=CreateIdentityRequestEntityBusinessAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 8",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        ownership_type="PRIVATE",
	        first_name="dwayne",
	        title="CEO",
	        business_tax_id="123456789",
	        doing_business_as="Petes Coffee",
	        principal_percentage_ownership=50,
	        email="user@example.org",
	        mcc="0742",
	        phone="1234567890",
	        business_name="Petes Coffee",
	        tax_id="123456789",
	        business_type="INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        business_phone="+1 (408) 756-4497",
	        dob=CreateIdentityRequestEntityDob(
	            year=1978,
	            day=27,
	            month=6
            ),
	        url="www.PetesCoffee.com",
	        annual_card_volume=12000000,
        )
    ) 
    response = tmp_client.identities.create(create_identity_request=req)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'abc'
    assert response.tags['test_key_102'] == 'test_val_102'


def test_create_associated_identity(config, c_merchant):
    tmp_client = finix.FinixClient(config)
    id = c_merchant.id
    req = CreateIdentityRequest(
	    tags=Tags(
	        test_key_103 = "test_val_103"
        ),
	    entity=CreateIdentityRequestEntity(
	        last_name="xbc",
	        max_transaction_amount=12000000,
	        has_accepted_credit_cards_previously=True,
	        default_statement_descriptor="Petes Coffee",
	        personal_address=CreateIdentityRequestEntityPersonalAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 7",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        incorporation_date=CreateIdentityRequestEntityIncorporationDate(
	            year=1978,
	            day=27,
	            month=6
            ),
	        business_address=CreateIdentityRequestEntityBusinessAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 8",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        ownership_type="PRIVATE",
	        first_name="dwayne",
	        title="CEO",
	        business_tax_id="123456789",
	        doing_business_as="Petes Coffee",
	        principal_percentage_ownership=50,
	        email="user@example.org",
	        mcc="0742",
	        phone="1234567890",
	        business_name="Petes Coffee",
	        tax_id="123456789",
	        business_type="INDIVIDUAL_SOLE_PROPRIETORSHIP",
	        business_phone="+1 (408) 756-4497",
	        dob=CreateIdentityRequestEntityDob(
	            year=1978,
	            day=27,
	            month=6
            ),
	        url="www.PetesCoffee.com",
	        annual_card_volume=12000000,
        )
    ) 
    response = tmp_client.identities.create_associated_identity(id, create_identity_request=req)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'xbc'
    assert response.tags['test_key_103'] == 'test_val_103'


def test_create_identity_verification(config, c_merchant):
    tmp_client = finix.FinixClient(config)
    id = c_merchant.id
    req = CreateVerificationRequest(
		processor='DUMMY_V1',
		tags=Tags(
	        test_key_104 = "test_val_104"
        )
	)
    response = tmp_client.identities.create_identity_verification(id, create_verification_request=req)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_104'] == 'test_val_104'