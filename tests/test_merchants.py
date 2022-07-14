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
def config01():
    configuration = Configuration(
        username = 'UStxEci4vXxGDWLQhNvao7YY',
        password = '25038781-2369-4113-8187-34780e91052e',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_merchant(config):
    tmp_client = finix.FinixClient(config)
    request_first = CreateIdentityRequest(
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
    response1 = tmp_client.identities.create(create_identity_request=request_first)
    id = response1.id
    request_second = CreatePaymentInstrumentRequest(
        account_type="SAVINGS",
        name="LBC",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        ),
	    country="USA",
	    bank_code="666666666",
	    account_number="123123123",
	    type="BANK_ACCOUNT",
	    identity=id
    )
    tmp_client.payment_instruments.create(create_payment_instrument_request = request_second)
    request_third = CreateMerchantUnderwritingRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response2 = tmp_client.merchants.create(id, create_merchant_underwriting_request=request_third)
    return response2


def test_get_merchant(config, c_merchant):
    tmp_client = finix.FinixClient(config)
    id = c_merchant.id
    response = tmp_client.merchants.get(id)
    assert response.id[:2] == 'MU'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_merchant(config01, c_merchant):
    tmp_client = finix.FinixClient(config01)
    id = c_merchant.id
    request = UpdateMerchantRequest(
        level_two_level_three_data_enabled=True,
        tags=Tags(
	        test_key_101 = "test_val_101"
        )
    )
    response = tmp_client.merchants.update(id, update_merchant_request=request)
    assert response.id[:2] == 'MU'
    assert response.level_two_level_three_data_enabled == True
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create_merchant(config):
    tmp_client = finix.FinixClient(config)
    request_first = CreateIdentityRequest(
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
    response1 = tmp_client.identities.create(create_identity_request=request_first)
    id = response1.id
    request_second = CreatePaymentInstrumentRequest(
        account_type="SAVINGS",
        name="LBC",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        ),
	    country="USA",
	    bank_code="666666666",
	    account_number="123123123",
	    type="BANK_ACCOUNT",
	    identity=id
    )
    tmp_client.payment_instruments.create(create_payment_instrument_request = request_second)
    request_third = CreateMerchantUnderwritingRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_102 = "test_val_102"
        )
    )
    response2 = tmp_client.merchants.create(id, create_merchant_underwriting_request=request_third)
    assert response2.id[:2] == 'MU'
    assert response2.processor == 'DUMMY_V1'
    assert response2.tags['test_key_102'] == 'test_val_102'


# newly created merchant still pending, can't create verification
def test_create_merchant_verification(config, c_merchant):
	tmp_client = finix.FinixClient(config)
	id = c_merchant.id
	request = CreateVerificationRequest()
	with pytest.raises(finix.ApiException) as e:
		tmp_client.merchants.create_merchant_verification(id, create_verification_request=request)
	assert e.value.status == 422
	assert e.value.reason == 'Unprocessable Entity'
	assert 'An existing verification is already PENDING.' in e.value.body