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
def c_bank(config):
    tmp_client = finix.FinixClient(config)
    req = CreatePaymentInstrumentRequest(
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
    response = tmp_client.payment_instruments.create(create_payment_instrument_request=req)
    return response


def test_get(config):
    tmp_client = finix.FinixClient(config)
    id = 'PI4gTM3twQ5XyXfM4rTuFvpo'
    response = tmp_client.payment_instruments.get(id)
    assert response.id[:2] == 'PI'
    assert response.type == 'APPLE_PAY'


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreatePaymentInstrumentRequest(
	    name="LBC Finix",
	    expiration_year=2049,
	    tags=Tags(
	    	card_name="Finix Card Python"
		),
	    number="4895142232120006",
	    expiration_month=12,
	    address=CreatePaymentInstrumentRequestAddress(
	        city="San Francisco",
	        region="CA",
	        postal_code="94404",
	        line1="900 Metro Center Blv",
	        country="USA"
		),
	    security_code="002",
	    type="PAYMENT_CARD",
	    identity="IDgWxBhfGYLLdkhxx2ddYf9K"
    )
    response = tmp_client.payment_instruments.create(create_payment_instrument_request=req)
    assert response.id[:2] == 'PI'
    assert response.last_four == '0006'
    assert response.tags['card_name'] == 'Finix Card Python'


def test_update(config, c_bank):
    tmp_client = finix.FinixClient(config)
    id = c_bank.id
    req = UpdatePaymentInstrumentRequest(
	    tags=Tags(
	        bank_account="Test Python Update"
        ),
    )
    response = tmp_client.payment_instruments.update(id, update_payment_instrument_request=req)
    assert response.id[:2] == 'PI'
    assert response.type == 'BANK_ACCOUNT'
    assert response.tags['bank_account'] == 'Test Python Update'


def test_create_payment_instrument_verification(config, c_bank):
    tmp_client = finix.FinixClient(config)
    id = c_bank.id
    req = CreateVerificationRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_000='test_val_000'
        )
    )
    response = tmp_client.payment_instruments.create_payment_instrument_verification(id, create_verification_request=req)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_000'] == 'test_val_000'