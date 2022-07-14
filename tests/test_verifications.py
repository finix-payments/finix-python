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


def test_create_and_get(config):
    tmp_client = finix.FinixClient(config)
    req = CreateVerificationRequest(
        merchant='MUgWbPVvtKbzjKNNGKqdQYV7',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = tmp_client.verifications.create(create_verification_request=req)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_110'] == 'test_val_110'
    response01 = tmp_client.verifications.get(response.id)
    assert response01.id[:2] == 'VI'
    assert response01.processor == 'DUMMY_V1'
    assert response01.tags['test_key_110'] == 'test_val_110'