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


def test_get(config):
    tmp_client = finix.FinixClient(config)
    id = 'WH9MorNnDCgvVnyZQ3MXqiVM'
    response = tmp_client.webhooks.get(id)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://eohzjuj2prziycz.m.pipedream.net'
    assert response.enabled == False


def test_update(config):
    tmp_client = finix.FinixClient(config)
    id = 'WH9MorNnDCgvVnyZQ3MXqiVM'
    req01 = UpdateWebhookRequest(
        enabled = True
    )
    req02 = UpdateWebhookRequest(
        enabled = False
    )
    response01 = tmp_client.webhooks.update(id,update_webhook_request=req01)
    response02 = tmp_client.webhooks.update(id,update_webhook_request=req02)
    assert response01.id[:2] == 'WH'
    assert response01.url == 'https://eohzjuj2prziycz.m.pipedream.net'
    assert response01.enabled == True
    assert response02.id[:2] == 'WH'
    assert response02.url == 'https://eohzjuj2prziycz.m.pipedream.net'
    assert response02.enabled == False


# no always open webhook for repetitive testing, expect error
def test_create(config):
    tmp_client = finix.FinixClient(config)
    req = CreateWebhookRequest(
        url='https://finix.com'
    )
    with pytest.raises(finix.ApiException) as e:
        tmp_client.webhooks.create(create_webhook_request=req)
    assert e.value.status == 422
    assert e.value.reason == 'Unprocessable Entity'
    assert 'Unable to call the configured URL with an empty payload' in e.value.body