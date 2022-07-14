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
def c_hook(config):
    tmp_client = finix.FinixClient(config)
    req = CreateWebhookRequest(
        url='https://example.com'
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
    assert response.url == 'https://example.com'
    assert response.enabled == False


def test_update(config,c_hook):
    tmp_client = finix.FinixClient(config)
    id = c_hook.id
    req01 = UpdateWebhookRequest(
        enabled = True
    )
    req02 = UpdateWebhookRequest(
        enabled = False
    )
    response01 = tmp_client.webhooks.update(id,update_webhook_request=req01)
    response02 = tmp_client.webhooks.update(id,update_webhook_request=req02)
    assert response01.id[:2] == 'WH'
    assert response01.url == 'https://example.com'
    assert response01.enabled == True
    assert response02.id[:2] == 'WH'
    assert response02.url == 'https://example.com'
    assert response02.enabled == False


def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateWebhookRequest(
        url='https://example.com'
    )
    response = tmp_client.webhooks.create(create_webhook_request=req)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://example.com'
    assert response.enabled == True