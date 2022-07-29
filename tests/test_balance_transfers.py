import pytest
import finix
from finix.models import *


def test_get_balance_transfer(client01, balance_transfer):
    id = balance_transfer.id
    response = client01.balance_transfers.get(id)
    assert response.id[:2] == 'BT'
    assert response.amount == 100
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_balance_transfer(client01):
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
    response = client01.balance_transfers.create(create_balance_transfer_request=request)
    assert response.id[:2] == 'BT'
    assert response.amount == 101
    assert response.tags['test_key_101'] == 'test_val_101'