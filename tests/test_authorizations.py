import pytest
import finix
from finix.models import *


def test_create_authorization(client00):
    request = CreateAuthorizationRequest(
        source="PIe2YvpcjvoVJ6PzoRPBK137",
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    tags=Tags(
	        test_key_101 = "test_val_101"
        ),
	    currency=Currency("USD"),
	    amount=118,
	    processor="DUMMY_V1"
    )
    response = client00.authorizations.create(create_authorization_request=request)
    assert response.id[:2] == 'AU'
    assert response.amount == 118
    assert response.tags['test_key_101'] == 'test_val_101'


def test_get_authorization(client00, authorization):
    id = authorization.id
    response = client00.authorizations.get(id)
    assert response.id[:2] == 'AU'
    assert response.amount == 108
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_authorization(client00, authorization):
    id = authorization.id
    request = UpdateAuthorizationRequest(
        fee=1,
        capture_amount=70,
    )
    response = client00.authorizations.update(id, update_authorization_request=request)
    assert response.id[:2] == 'AU'
    assert response.state == 'SUCCEEDED'
    assert response.tags['test_key_100'] == 'test_val_100'