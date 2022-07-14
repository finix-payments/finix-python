import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USpumes23XhzHwXqiy9bfX2B',
        password = 'c69d39e3-f9ff-4735-8c3e-abca86441906',
        environment = Environment.SANDBOX
    )
    return configuration


def test_get(config):
    tmp_client = finix.FinixClient(config)
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = tmp_client.settlements.get(id)
    assert response.id[:2] == 'ST'
    assert response.type == 'MERCHANT_REVENUE'
    assert response.currency == 'USD'


# testing on deleted resource resulting in Conflict exception
def test_delete_exception(config):
    tmp_client = finix.FinixClient(config)
    sid = 'STmCc8GbjjX33SdymwNhb9Et'
    tid = 'TRr61njQxaa7AJf6E1C3QwCc'
    req = RemoveSettlementTransfer(
        transfers=[tid]
    )
    with pytest.raises(finix.ApiException) as e:
        tmp_client.settlements.remove_transfers_from_settlement(sid,remove_settlement_transfer = req)
    assert e.value.status == 409
    assert e.value.reason == 'Conflict'


# try to create a settlement for everything settled, expect 422
def test_create(config):
    tmp_client = finix.FinixClient(config)
    id = 'IDqvpp6sfYBLxDsYNeFRdYeF'
    req = CreateSettlementRequest(
        processor='DUMMY_V1',
        currency= Currency("USD"),
        merchant_id=id,
        tags=Tags(
            test_key_200 = "test_val_200"
        )
    )
    with pytest.raises(finix.ApiException) as e:
        tmp_client.settlements.create(id,create_settlement_request=req)
    assert e.value.status == 422
    assert e.value.reason == 'Unprocessable Entity'
    assert 'There are no unsettled SUCCEEDED transfers to be settled.' in e.value.body


def test_update(config):
    tmp_client = finix.FinixClient(config)
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    req = UpdateSettlementRequest(
        tags=Tags(
            test_key_201 = "test_val_201"
        ),
        destination = 'PIxnmQc5LPYMZWKbbp3K3weX'
    )
    response = tmp_client.settlements.update(id,update_settlement_request=req)
    assert response.id[:2] == 'ST'
    assert response.type == 'MERCHANT_REVENUE'
    #assert response.destination == 'PIxnmQc5LPYMZWKbbp3K3weX'
    #assert response.tags['test_key_201'] == 'test_val_201'