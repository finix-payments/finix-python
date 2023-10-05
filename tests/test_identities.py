import pytest
import finix
from finix.models import *


def test_get_identity(client00, identity_merchant):
    id = identity_merchant.id
    response = client00.identities.get(id)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'lbc'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_identity(client00, identity_merchant):
    id = identity_merchant.id
    request = UpdateIdentityRequest(
        tags=Tags(
            test_key_101 = "test_val_101"
        )
    )
    response = client00.identities.update(id, update_identity_request=request)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'lbc'
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create_identity(client00):
    request = CreateIdentityRequest(
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
	        last_name="abc",
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
    response = client00.identities.create(create_identity_request=request)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'abc'
    assert response.tags['test_key_102'] == 'test_val_102'


def test_create_associated_identity(client00, business_identity_merchant):
    id = business_identity_merchant.id
    request = CreateAssociatedIdentityRequest(
	    tags=Tags(
	        test_key_103 = "test_val_103"
        ),
	    entity=CreateAssociatedIdentityRequestEntity(
	        last_name="xbc",
	        personal_address=CreateAssociatedIdentityRequestEntityPersonalAddress(
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
    response = client00.identities.create_associated_identity(id, create_associated_identity_request=request)
    assert response.id[:2] == 'ID'
    assert response.entity['last_name'] == 'xbc'
    assert response.tags['test_key_103'] == 'test_val_103'
