import pytest
import finix
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
    client = finix.FinixClient(config)
    request = CreateFeeProfileRequest(
        fixed_fee=100,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_100 = "test_val_100"
        )
    )
    response = client.fee_profiles.create(create_fee_profile_request=request)
    return response


def test_get_fee_profile(config, c_profile):
    client = finix.FinixClient(config)
    id = c_profile.id
    response = client.fee_profiles.get(id)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 100


def test_create_fee_profile(config):
    client = finix.FinixClient(config)
    request = CreateFeeProfileRequest(
        fixed_fee=10,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_110 = "test_val_110"
        )
    )
    response = client.fee_profiles.create(create_fee_profile_request=request)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 10