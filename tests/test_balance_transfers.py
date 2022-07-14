import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USbkjk46XqUTQHN3i2jaVnc1',
        password = 'ac915962-2757-49ea-aeee-10960a408b99',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_btransfer(config):
    tmp_client = finix.FinixClient(config)
    req = CreateBalanceTransferRequest(
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
    response = tmp_client.balance_transfers.create(create_balance_transfer_request=req)
    return response


def test_get(config, c_btransfer):
    tmp_client = finix.FinixClient(config)
    id = c_btransfer.id
    response = tmp_client.balance_transfers.get(id)
    assert response.id[:2] == 'BT'
    assert response.amount == 100
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateBalanceTransferRequest(
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
    response = tmp_client.balance_transfers.create(create_balance_transfer_request=req)
    assert response.id[:2] == 'BT'
    assert response.amount == 101
    assert response.tags['test_key_101'] == 'test_val_101'