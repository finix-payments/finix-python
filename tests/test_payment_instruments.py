import pytest
import finix
from finix.models import *


def test_get_payment_instrument(client00):
    id = 'PI4gTM3twQ5XyXfM4rTuFvpo'
    response = client00.payment_instruments.get(id)
    assert response.id[:2] == 'PI'
    assert response.type == 'APPLE_PAY'


def test_create_payment_instrument(client00):
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
    response = client00.payment_instruments.create(create_payment_instrument_request=request)
    assert response.id[:2] == 'PI'
    assert response.last_four == "0006"
    assert response.tags['card_name'] == 'Finix Card Python'


def test_update_payment_instrument(client00, bank_account):
    id = bank_account.id
    request = UpdatePaymentInstrumentRequest(
	    tags=Tags(
	        bank_account="Test Python Update"
        ),
    )
    response = client00.payment_instruments.update(id, update_payment_instrument_request=request)
    assert response.id[:2] == 'PI'
    assert response.type == 'BANK_ACCOUNT'
    assert response.tags['bank_account'] == 'Test Python Update'


'''
def test_create_payment_instrument_verification(client00, bank_account):
    id = bank_account.id
    request = CreateVerificationRequest(
        processor='DUMMY_V1',
        tags=Tags(
	        test_key_000='test_val_000'
        )
    )
    response = client00.payment_instruments.create_payment_instrument_verification(id, create_verification_request=request)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_000'] == 'test_val_000'
'''