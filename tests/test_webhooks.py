import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USpumes23XhzHwXqiy9bfX2B',
        password = 'c69d39e3-f9ff-4735-8c3e-abca86441906',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_hook(config):
    tmp_client = finix.FinixClient(config)
    req = CreateWebhookRequest(
        url='https://www.google.com',
        enabled = False
    )
    response = tmp_client.webhooks.create(create_webhook_request=req)
    req01 = UpdateWebhookRequest(
        enabled = False
    )
    tmp_client.webhooks.update(response.id,update_webhook_request=req01)
    return response


def test_get(config, c_hook):
    tmp_client = finix.FinixClient(config)
    id = c_hook.id
    response = tmp_client.webhooks.get(id)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://www.google.com'
    assert response.enabled == False


def test_create_and_update(config):
    tmp_client = finix.FinixClient(config)
    req = CreateWebhookRequest(
        url='https://finix.com/',
        enabled = False
    )
    response = tmp_client.webhooks.create(create_webhook_request=req)
    req01 = UpdateWebhookRequest(
        url='https://www.google.com',
        enabled = False
    )
    response01 = tmp_client.webhooks.update(response.id,update_webhook_request=req01)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://finix.com/'
    assert response01.id[:2] == 'WH'
    assert response01.url == 'https://www.google.com'
    assert response01.enabled == False