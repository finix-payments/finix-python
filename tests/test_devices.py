import pytest
import finix
from finix.models import *


def test_get_device(client02, device):
    id = device.id
    response = client02.devices.get(id)
    assert response.id[:2] == 'DV'
    assert response.name == 'pytest_device'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_device(client02):
    id = 'MUu56ZGx3Xb6U9gAqKfgNisd'
    request = CreateDevice(
        description='setup testing',
        tags=Tags(
	        test_key_101 = "test_val_101"
        ),
        merchant_id = id,
        model='MX915',
        name='pytest_device01',
        configuration=ConfigurationDetails(
            allow_debit=True
        )
    )
    response = client02.devices.create(id, create_device = request)
    assert response.id[:2] == 'DV'
    assert response.name == 'pytest_device01'
    assert response.tags['test_key_101'] == 'test_val_101'