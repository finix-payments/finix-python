import pytest
import finix
from finix.models import *


def test_get_settlement(client04):
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = client04.settlements.get(id)
    assert response.id[:2] == 'ST'
    assert response.type == 'MERCHANT_REVENUE'
    assert response.currency == 'USD'


# testing on deleted resource resulting in Conflict exception
def test_delete_settlement_transfers(client04):
    sid = 'STmCc8GbjjX33SdymwNhb9Et'
    tid = 'TRr61njQxaa7AJf6E1C3QwCc'
    request = RemoveSettlementTransfer(
        transfers=[tid]
    )
    with pytest.raises(finix.ApiException) as e:
        client04.settlements.remove_transfers_from_settlement(sid,remove_settlement_transfer = request)
    assert e.value.status == 409
    assert e.value.reason == 'Conflict'
    assert 'Entries [TRr61njQxaa7AJf6E1C3QwCc] not found in settlement STmCc8GbjjX33SdymwNhb9Et' in e.value.body[0].message


# try to create a settlement for everything settled, expect 422
def test_create_settlement(client04):
    id = 'IDqvpp6sfYBLxDsYNeFRdYeF'
    request = CreateSettlementRequest(
        processor='DUMMY_V1',
        currency= Currency("USD"),
        merchant_id=id,
        tags=Tags(
            test_key_200 = "test_val_200"
        )
    )
    with pytest.raises(finix.ApiException) as e:
        client04.settlements.create(id,create_settlement_request=request)
    assert e.value.status == 422
    assert e.value.reason == 'Unprocessable Entity'
    assert 'There are no unsettled SUCCEEDED transfers to be settled.' in e.value.body[0].message

