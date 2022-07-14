import pytest
import finix
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
    client = finix.FinixClient(config)
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
    response = client.payment_instruments.create(create_payment_instrument_request=request)
    return response


def test_get_payment_instrument(config):
    client = finix.FinixClient(config)
    id = 'PI4gTM3twQ5XyXfM4rTuFvpo'
    response = client.payment_instruments.get(id)
    assert response.id[:2] == 'PI'
    assert response.type == 'APPLE_PAY'


def test_create_payment_instrument(config):
    client = finix.FinixClient(config)
    request = CreatePaymentInstrumentRequest(
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
    response = client.payment_instruments.create(create_payment_instrument_request=request)
    assert response.id[:2] == 'PI'
    assert response.last_four == '0006'
    assert response.tags['card_name'] == 'Finix Card Python'


def test_update_payment_instrument(config, c_bank):
    client = finix.FinixClient(config)
    id = c_bank.id
    request = UpdatePaymentInstrumentRequest(
	    tags=Tags(
	        bank_account="Test Python Update"
        ),
    )
    response = client.payment_instruments.update(id, update_payment_instrument_request=request)
    assert response.id[:2] == 'PI'
    assert response.type == 'BANK_ACCOUNT'
    assert response.tags['bank_account'] == 'Test Python Update'


def test_create_payment_instrument_verification(config, c_bank):
    client = finix.FinixClient(config)
    id = c_bank.id
    request = CreateVerificationRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_000='test_val_000'
        )
    )
    response = client.payment_instruments.create_payment_instrument_verification(id, create_verification_request=request)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_000'] == 'test_val_000'