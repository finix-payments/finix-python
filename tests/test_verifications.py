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
def c_verif(config):
    tmp_client = finix.FinixClient(config)
    req = CreateVerificationRequest(
        merchant='MUgWbPVvtKbzjKNNGKqdQYV7',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_100 = "test_val_100"
        )
    )
    response = tmp_client.verifications.create(create_verification_request=req)
    return response


def test_get(config, c_verif):
    tmp_client = finix.FinixClient(config)
    id = c_verif.id
    response = tmp_client.verifications.get(id)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateVerificationRequest(
        merchant='MUucec6fHeaWo3VHYoSkUySM',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = tmp_client.verifications.create(create_verification_request=req)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_110'] == 'test_val_110'