import pytest
import finix
from finix.models import *


def test_get_webhook(client00, webhook):
    id = webhook.id
    response = client00.webhooks.get(id)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://example.com'
    assert response.enabled == False


def test_update_webhook(client00, webhook):
    id = webhook.id
    request_first = UpdateWebhookRequest(
        enabled = True
    )
    request_second = UpdateWebhookRequest(
        enabled = False
    )
    response01 = client00.webhooks.update(id,update_webhook_request=request_first)
    response02 = client00.webhooks.update(id,update_webhook_request=request_second)
    assert response01.id[:2] == 'WH'
    assert response01.url == 'https://example.com'
    assert response01.enabled == True
    assert response02.id[:2] == 'WH'
    assert response02.url == 'https://example.com'
    assert response02.enabled == False


def test_create_webhook(client00):
    request = CreateWebhookRequest(
        url='https://example.com'
    )
    response = client00.webhooks.create(create_webhook_request=request)
    request_next = UpdateWebhookRequest(
        enabled = False
    )
    client00.webhooks.update(response.id,update_webhook_request=request_next)
    assert response.id[:2] == 'WH'
    assert response.url == 'https://example.com'
    assert response.enabled == True