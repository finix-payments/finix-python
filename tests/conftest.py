import pytest
import finix
from finix.models import *
from finix.configuration import Environment, Configuration
from datetime import datetime


@pytest.fixture
def client00(): # used for most APIs
    configuration = Configuration(
        username = 'USsRhsHYZGBPnQw8CByJyEQW',
        password = '8a14c2f9-d94b-4c72-8f5c-a62908e5b30e',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client


@pytest.fixture
def client01(): # used for balance transfer APIs
    configuration = Configuration(
        username = 'USbkjk46XqUTQHN3i2jaVnc1',
        password = 'ac915962-2757-49ea-aeee-10960a408b99',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client


@pytest.fixture
def client02(): # used for device APIs
    configuration = Configuration(
        username = 'USjHFGYvecE4LBitYG8KDE2g',
        password = 'b698f403-d9b7-4157-82d8-162cea8c8cc3',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client


@pytest.fixture
def client03(): # used for fee profile and merchant profile APIs
    configuration = Configuration(
        username = 'USimz3zSq5R2PqiEBXY6rSiJ',
        password = '8bacba32-9550-48ff-b567-fe7648947041',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client


@pytest.fixture
def client04(): # used for settlement APIs
    configuration = Configuration(
        username = 'USpumes23XhzHwXqiy9bfX2B',
        password = 'c69d39e3-f9ff-4735-8c3e-abca86441906',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client


@pytest.fixture
def client05(): # used for merchant update endpoint
    configuration = Configuration(
        username = 'UStxEci4vXxGDWLQhNvao7YY',
        password = '25038781-2369-4113-8187-34780e91052e',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client

@pytest.fixture
def client06(): # used for merchant update endpoint
    configuration = Configuration(
        username = 'USj46WbwgnjapmdYFnEDP3Ec',
        password = 'b9b4042c-9621-438d-a84b-8557d4bda84d',
        environment = Environment.SANDBOX
    )
    client = finix.FinixClient(configuration)
    return client

@pytest.fixture
def authorization(client00):
    request = CreateAuthorizationRequest(
        source="PIe2YvpcjvoVJ6PzoRPBK137",
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        ),
	    currency=Currency("USD"),
	    amount=108,
	    processor="DUMMY_V1"
    )
    response = client00.authorizations.create(create_authorization_request=request)
    return response


@pytest.fixture
def balance_transfer(client01):
    request = CreateBalanceTransferRequest(
        currency=Currency("USD"),
        amount=100,
        source='FOR_BENEFIT_OF_ACCOUNT',
        destination='OPERATING_ACCOUNT',
        processor_type='LITLE_V1',
        description='setup balance transfer for testing',
        tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = client01.balance_transfers.create(create_balance_transfer_request=request)
    return response


@pytest.fixture
def device(client02):
    id = 'MUu56ZGx3Xb6U9gAqKfgNisd'
    request = CreateDevice(
        description='setup for testing',
        tags=Tags(
	        test_key_100 = "test_val_100"
        ),
        merchant_id = id,
        model='MX915',
        name='pytest_device',
        configuration=ConfigurationDetails(
            allow_debit=True
        )
    )
    response = client02.devices.create(id, create_device = request)
    return response


@pytest.fixture
def dispute_evidence(client00):
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    request = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = client00.disputes.create_dispute_evidence(id, create_dispute_evidence_request=request)
    return response


@pytest.fixture
def fee_profile(client03):
    request = CreateFeeProfileRequest(
        fixed_fee=100,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = client03.fee_profiles.create(create_fee_profile_request=request)
    return response


@pytest.fixture
def file(client00):
    request = CreateFileRequest(
        display_name="pytest_file",
        linked_to="MU2n7BSovtwYsWYZF6rBnnzk",
        type="DRIVERS_LICENSE_FRONT",
        tags=Tags(
            test_key_100 = "test_val_100"
        )
    )
    response = client00.files.create(create_file_request=request)
    return response


@pytest.fixture
def external_link(client00, file):
    fid = file.id
    request = CreateExternalLinkRequest(
        type="UPLOAD",
        duration=30,
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = client00.files.create_external_link(fid, create_external_link_request=request)
    return response


@pytest.fixture
def identity_merchant(client00):
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
	        test_key_100 = "test_val_100"
        ),
	    entity=CreateIdentityRequestEntity(
	        last_name="lbc",
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
    return response


@pytest.fixture
def instrument_update(client00):
    str_now = str(datetime.now())
    req_string = "{\"merchant\":\"MUucec6fHeaWo3VHYoSkUySM\",  \"idempotency_id\":\"F" + str_now + "\" }"
    request = CreateInstrumentUpdateRequest(
        file=open('tests/test_file.png', 'rb'),
        request=req_string,
    )
    response = client00.instrument_updates.create(create_instrument_update_request=request)
    return response


@pytest.fixture
def merchant(client00):
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
	        test_key_100 = "test_val_100"
        )
    )
    response2 = client00.merchants.create(id, create_merchant_underwriting_request=request_third)
    return response2


@pytest.fixture
def bank_account(client00):
    request = CreatePaymentInstrumentRequest(
        account_type="SAVINGS",
        name="test_python",
	    tags=Tags(
	        bank_account="Test Python Account"
        ),
	    country="USA",
	    bank_code="666666666",
	    account_number="123123123",
	    type="BANK_ACCOUNT",
	    identity="IDpYDM7J9n57q849o9E9yNrG"
    )
    response = client00.payment_instruments.create(create_payment_instrument_request=request)
    return response


@pytest.fixture
def transfer(client00):
    request = CreateTransferRequest(
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    currency=Currency("USD"),
	    amount=666666,
	    source="PIe2YvpcjvoVJ6PzoRPBK137",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = client00.transfers.create(create_transfer_request=request)
    return response


@pytest.fixture
def verification(client00):
    request = CreateVerificationRequest(
        merchant='MUgWbPVvtKbzjKNNGKqdQYV7',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_100 = "test_val_100"
        )
    )
    response = client00.verifications.create(create_verification_request=request)
    return response


@pytest.fixture
def webhook(client00):
    request = CreateWebhookRequest(
        url='https://example.com'
    )
    response = client00.webhooks.create(create_webhook_request=request)
    request_next = UpdateWebhookRequest(
        enabled = False
    )
    client00.webhooks.update(response.id,update_webhook_request=request_next)
    return response

@pytest.fixture
def onboarding_form(client00):
    request = CreateOnboardingFormRequest(
        onboarding_data = CreateOnboardingFormRequestOnboardingData(
            max_transaction_amount = 100000
        ),
        merchant_processors = [CreateOnboardingFormRequestMerchantProcessorsInner(
            processor = "LITLE_V1"
        )],
        onboarding_link_details = CreateOnboardingFormRequestOnboardingLinkDetails(
            return_url = "https://www.finix.com/docs",
            expired_session_url = "https://www.finix.com/",
            terms_of_service_url = "https://www.finix.com/terms-and-policies",
            fee_details_url = "https://www.finix.com/docs",
            expiration_in_minutes = "30"
        )
    )
    response = client00.onboarding_forms.create_onboarding_form(create_onboarding_form_request=request)
    return response