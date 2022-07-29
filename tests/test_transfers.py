import pytest
import finix
from finix.models import *


def test_create_transfer(client00):
    request = CreateTransferRequest(
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    currency=Currency("USD"),
	    amount=666,
	    source="PIe2YvpcjvoVJ6PzoRPBK137",
	    tags=Tags(
	        test_key_101 = "test_val_101"
        )
    )
    response = client00.transfers.create(create_transfer_request=request)
    assert response.type == 'DEBIT'
    assert response.amount == 666
    assert response.tags['test_key_101'] == 'test_val_101'


def test_create_transfer_reversal(client00, transfer):
    id = transfer.id
    request = CreateReversalRequest(
        refund_amount=666666,
        tags=Tags(
            test_key_102 = "test_val_102"
        )
    )
    response = client00.transfers.create_transfer_reversal(id, create_reversal_request=request)
    assert response.type == 'REVERSAL'
    assert response.amount == 666666
    assert response.tags['test_key_102'] == 'test_val_102'


def test_get_transfer(client00, transfer):
    id = transfer.id
    response = client00.transfers.get(id)
    assert response.type == 'DEBIT'
    assert response.amount == 666666
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_transfer(client00, transfer):
    id = transfer.id
    request = UpdateTransferRequest(
        tags=Tags(
            test_key_200 = "test_val_200"
        )
    )
    response = client00.transfers.update(id, update_transfer_request=request)
    assert response.type == 'DEBIT'
    assert response.amount == 666666
    assert response.tags['test_key_200'] == 'test_val_200'