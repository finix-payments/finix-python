import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USjHFGYvecE4LBitYG8KDE2g',
        password = 'b698f403-d9b7-4157-82d8-162cea8c8cc3',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_device(config):
    tmp_client = finix.FinixClient(config)
    id = 'MUu56ZGx3Xb6U9gAqKfgNisd'
    req = CreateDevice(
        description='setup for testing',
        tags=Tags(
	        test_key_100 = "test_val_100"
        ),
        merchant_id = id,
        model='BBPOS',
        name='pytest_device',
        configuration=ConfigurationDetails(
            allow_debit=True
        )
    )
    response = tmp_client.devices.create(id, create_device = req)
    return response


def test_get(config, c_device):
    tmp_client = finix.FinixClient(config)
    id = c_device.id
    response = tmp_client.devices.get(id)
    assert response.id[:2] == 'DV'
    assert response.name == 'pytest_device'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create(config):
    tmp_client = finix.FinixClient(config)
    id = 'MUu56ZGx3Xb6U9gAqKfgNisd'
    req = CreateDevice(
        description='setup testing',
        tags=Tags(
	        test_key_101 = "test_val_101"
        ),
        merchant_id = id,
        model='BBPOS',
        name='pytest_device01',
        configuration=ConfigurationDetails(
            allow_debit=True
        )
    )
    response = tmp_client.devices.create(id, create_device = req)
    assert response.id[:2] == 'DV'
    assert response.name == 'pytest_device01'
    assert response.tags['test_key_101'] == 'test_val_101'


# no test for update