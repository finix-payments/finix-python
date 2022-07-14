import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USimz3zSq5R2PqiEBXY6rSiJ',
        password = '8bacba32-9550-48ff-b567-fe7648947041',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_profile(config):
    tmp_client = finix.FinixClient(config)
    req = CreateFeeProfileRequest(
        fixed_fee=100,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = tmp_client.fee_profiles.create(create_fee_profile_request=req)
    return response


def test_get(config, c_profile):
    tmp_client = finix.FinixClient(config)
    id = c_profile.id
    response = tmp_client.fee_profiles.get(id)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 100


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateFeeProfileRequest(
        fixed_fee=10,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_110 = "test_val_110"
        )
    )
    response = tmp_client.fee_profiles.create(create_fee_profile_request=req)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 10