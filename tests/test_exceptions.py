import pytest
import finix
from finix.models import *


# provide wrong authentication information (code is UNKNOWN)
def test_http401():
    client = finix.FinixClient()
    request = CreateTransferRequest(
        hello = 2 * 3,
        currency=Currency("USD"),
	    amount=666
    )
    with pytest.raises(finix.ApiException) as e:
        client.transfers.create(create_transfer_request=request)
    assert e.value.status == 401
    assert e.value.reason == 'Unauthorized'
    assert e.value.body[0].message == 'Unauthorized'


# access an endpoint without permission (code is UNKNOWN)
def test_http403(client00):
    request = CreateBalanceTransferRequest(
        currency=Currency("USD"),
        amount=101,
        source='FOR_BENEFIT_OF_ACCOUNT',
        destination='OPERATING_ACCOUNT',
        processor_type='LITLE_V1',
        description='setup balance transfer for testing',
        tags=Tags(
	        test_key_101 = "test_val_101"
        )
    )
    with pytest.raises(finix.ApiException) as e:
        client00.balance_transfers.create(create_balance_transfer_request=request)
    assert e.value.status == 403
    assert e.value.reason == 'Forbidden'
    assert e.value.body[0].message == 'Access is denied'


# access non-existing resource
def test_http404(client00):
    id = 'TRnH7FkSB7zePeHExNZwSb9H666'
    with pytest.raises(finix.ApiException) as e:
        client00.transfers.get(id)
    assert e.value.status == 404
    assert e.value.reason == 'Not Found'
    assert e.value.body[0].code == 'NOT_FOUND'
    assert e.value.body[0].message == 'TRnH7FkSB7zePeHExNZwSb9H666 was not found'


# include invalid field in request body
def test_http422(client00):
    request = CreatePaymentInstrumentRequest(
	    name="LBC Finix",
	    expiration_year=1988,
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
    with pytest.raises(finix.ApiException) as e:
        client00.payment_instruments.create(create_payment_instrument_request=request)
    assert e.value.status == 422
    assert e.value.reason == 'Unprocessable Entity'
    assert e.value.body[0].code == 'INVALID_FIELD'
    assert e.value.body[0].field == 'expiration_year'
    assert e.value.body[0].message == 'Expiration year 1988 is expired'