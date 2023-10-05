import pytest
import finix
from finix.models import *


def test_get_merchant(client00, merchant):
    id = merchant.id
    response = client00.merchants.get(id)
    assert response.id[:2] == 'MU'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_merchant(client05, merchant):
    id = merchant.id
    request = UpdateMerchantRequest(
        level_two_level_three_data_enabled=True,
        tags=Tags(
	        test_key_101 = "test_val_101"
        )
    )
    response = client05.merchants.update(id, update_merchant_request=request)
    assert response.id[:2] == 'MU'
    assert response.level_two_level_three_data_enabled == True
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create_merchant(client00):
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
            annual_card_volume=12000000,
            business_address=CreateIdentityRequestEntityBusinessAddress(
				city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 7",
	            line1="741 Douglass St",
	            postal_code="94114"
			),
			business_name="Finix Flowers",
			business_phone="+1 (408) 756-4497",
			business_tax_id="123456789",
			business_type="INDIVIDUAL_SOLE_PROPRIETORSHIP",
			default_statement_descriptor="Finix Flowers",
			dob=CreateIdentityRequestEntityDob(
				year=1978,
				day=27,
				month=6
			),
			doing_business_as="Finix Flowers",
			incorporation_date=CreateIdentityRequestEntityIncorporationDate(
				year=1978,
				day=27,
				month=6
			),
	        last_name="lbc",
	        max_transaction_amount=12000000,
            ach_max_transaction_amount=1000000,
            mcc="4900",
            ownership_type="PRIVATE",
            principal_percentage_ownership=50,
            tax_id="123456789",
            title="CEO",
            url="https://www.finix.com",
	        has_accepted_credit_cards_previously=True,
	        personal_address=CreateIdentityRequestEntityPersonalAddress(
	            city="San Mateo",
	            country="USA",
	            region="CA",
	            line2="Apartment 7",
	            line1="741 Douglass St",
	            postal_code="94114"
            ),
	        first_name="dwayne",
	        email="user@example.org",
	        phone="1234567890"
        )
    ) 
    response1 = client00.identities.create(create_identity_request=request_first)
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
    client00.payment_instruments.create(create_payment_instrument_request = request_second)
    request_third = CreateMerchantUnderwritingRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_102 = "test_val_102"
        )
    )
    response2 = client00.merchants.create(id, create_merchant_underwriting_request=request_third)
    assert response2.id[:2] == 'MU'
    assert response2.processor == 'DUMMY_V1'
    assert response2.tags['test_key_102'] == 'test_val_102'


# newly created merchant still pending, can't create verification
def test_create_merchant_verification(client00, merchant):
	id = merchant.id
	request = CreateVerificationRequest()
	with pytest.raises(finix.ApiException) as e:
		client00.merchants.create_merchant_verification(id, create_verification_request=request)
	assert e.value.status == 422
	assert e.value.reason == 'Unprocessable Entity'
	assert 'An existing verification is already PENDING.' in e.value.body[0].message
