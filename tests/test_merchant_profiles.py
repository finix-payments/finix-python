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


def test_get_merchant_profile(config):
    tmp_client = finix.FinixClient(config)
    id = 'MP9J4ALZHx4pa5i1p5G5jeKY'
    response = tmp_client.merchant_profiles.get(id)
    assert response.id[:2] == 'MP'
    assert response.application == 'AP7yJr75Zycq9Fz6CpK8h9gn'


def test_update_merchant_profile(config):
    tmp_client = finix.FinixClient(config)
    id = 'MP9J4ALZHx4pa5i1p5G5jeKY'
    req = {
        'tags':{'test_key_100':'test_val_100'}
    }
    response = tmp_client.merchant_profiles.update(id,body=req)
    assert response.id[:2] == 'MP'
    assert response.application == 'AP7yJr75Zycq9Fz6CpK8h9gn'
    assert response.tags['test_key_100'] == 'test_val_100'