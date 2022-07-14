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
    client = finix.FinixClient(config)
    request = CreateVerificationRequest(
        merchant='MUgWbPVvtKbzjKNNGKqdQYV7',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_100 = "test_val_100"
        )
    )
    response = client.verifications.create(create_verification_request=request)
    return response


def test_get_verification(config, c_verif):
    client = finix.FinixClient(config)
    id = c_verif.id
    response = client.verifications.get(id)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_verification(config):
    client = finix.FinixClient(config)
    request = CreateVerificationRequest(
        merchant='MUucec6fHeaWo3VHYoSkUySM',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = client.verifications.create(create_verification_request=request)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_110'] == 'test_val_110'