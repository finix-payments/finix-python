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
def c_auth(config):
    client = finix.FinixClient(config)
    request = CreateAuthorizationRequest(
        source="PIe2YvpcjvoVJ6PzoRPBK137",
	    merchant="MUeDVrf2ahuKc9Eg5TeZugvs",
	    tags=Tags(
	        test_key_100 = "test_val_100"
        ),
	    currency=Currency("USD"),
	    amount=108,
	    processor="DUMMY_V1"
    )
    response = client.authorizations.create(create_authorization_request=request)
    return response


def test_create_authorization(config):
    client = finix.FinixClient(config)
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
    response = client.authorizations.create(create_authorization_request=request)
    assert response.id[:2] == 'AU'
    assert response.amount == 118
    assert response.tags['test_key_101'] == 'test_val_101'


def test_get_authorization(config, c_auth):
    client = finix.FinixClient(config)
    id = c_auth.id
    response = client.authorizations.get(id)
    assert response.id[:2] == 'AU'
    assert response.amount == 108
    assert response.tags['test_key_100'] == 'test_val_100'


def test_update_authorization(config, c_auth):
    client = finix.FinixClient(config)
    id = c_auth.id
    request = UpdateAuthorizationRequest(
        fee=1,
        capture_amount=70,
    )
    response = client.authorizations.update(id, update_authorization_request=request)
    assert response.id[:2] == 'AU'
    assert response.state == 'SUCCEEDED'
    assert response.tags['test_key_100'] == 'test_val_100'