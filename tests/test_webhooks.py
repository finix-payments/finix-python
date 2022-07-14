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
    request = CreateWebhookRequest(
        url='https://example.com'
    )
    response = tmp_client.webhooks.create(create_webhook_request=request)
    request_next = UpdateWebhookRequest(
        enabled = False
    )
    tmp_client.webhooks.update(response.id,update_webhook_request=request_next)
    return response


def test_get_webhook(config, c_hook):
    tmp_client = finix.FinixClient(config)
    id = c_hook.id
    response = tmp_client.webhooks.get(id)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://example.com'
    assert response.enabled == False


def test_update_webhook(config,c_hook):
    tmp_client = finix.FinixClient(config)
    id = c_hook.id
    request_first = UpdateWebhookRequest(
        enabled = True
    )
    request_second = UpdateWebhookRequest(
        enabled = False
    )
    response01 = tmp_client.webhooks.update(id,update_webhook_request=request_first)
    response02 = tmp_client.webhooks.update(id,update_webhook_request=request_second)
    assert response01.id[:2] == 'WH'
    assert response01.url == 'https://example.com'
    assert response01.enabled == True
    assert response02.id[:2] == 'WH'
    assert response02.url == 'https://example.com'
    assert response02.enabled == False


def test_create_webhook(config):
    tmp_client = finix.FinixClient(config)
    request = CreateWebhookRequest(
        url='https://example.com'
    )
    response = tmp_client.webhooks.create(create_webhook_request=request)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://example.com'
    assert response.enabled == True