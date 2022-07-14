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
def c_transfer(config):
    tmp_client = finix.FinixClient(config)
    req = CreateTransferRequest(
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    currency=Currency("USD"),
	    amount=666666,
	    source="PIe2YvpcjvoVJ6PzoRPBK137",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = tmp_client.transfers.create(create_transfer_request=req)
    return response


def test_create_transfer(config):
    tmp_client = finix.FinixClient(config)
    req = CreateTransferRequest(
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    currency=Currency("USD"),
	    amount=666,
	    source="PIe2YvpcjvoVJ6PzoRPBK137",
	    tags=Tags(
	        test_key_101 = "test_val_101"
        )
    )
    response = tmp_client.transfers.create(create_transfer_request=req)
    assert response.type == 'DEBIT'
    assert response.amount == 666
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create_transfer_reversal(config, c_transfer):
    tmp_client = finix.FinixClient(config)
    id = c_transfer.id
    req = CreateReversalRequest(
        refund_amount=666666,
        tags=Tags(
            test_key_102 = "test_val_102"
        )
    )
    response = tmp_client.transfers.create_transfer_reversal(id, create_reversal_request=req)
    assert response.type == 'REVERSAL'
    assert response.amount == 666666
    assert response.tags['test_key_102'] == 'test_val_102'


def test_get_transfer(config, c_transfer):
    tmp_client = finix.FinixClient(config)
    id = c_transfer.id
    response = tmp_client.transfers.get(id)
    assert response.type == 'DEBIT'
    assert response.amount == 666666
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_transfer(config, c_transfer):
    tmp_client = finix.FinixClient(config)
    id = c_transfer.id
    req = UpdateTransferRequest(
        tags=Tags(
            test_key_200 = "test_val_200"
        )
    )
    response = tmp_client.transfers.update(id, update_transfer_request=req)
    assert response.type == 'DEBIT'
    assert response.amount == 666666
    assert response.tags['test_key_200'] == 'test_val_200'