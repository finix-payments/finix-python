import pytest
import finix
from finix.apis import *
from finix.models import *
from finix.configuration import Environment, Configuration
from datetime import datetime


@pytest.fixture
def config():
    configuration = Configuration(
        username = 'USsRhsHYZGBPnQw8CByJyEQW',
        password = '8a14c2f9-d94b-4c72-8f5c-a62908e5b30e',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def c_update(config):
    tmp_client = finix.FinixClient(config)
    str_now = str(datetime.now())
    req_string = "{\"merchant\":\"MUucec6fHeaWo3VHYoSkUySM\",  \"idempotency_id\":\"F" + str_now + "\" }"
    req = CreateInstrumentUpdateRequest(
        file=open('tests/test_file.png', 'rb'),
        request=req_string,
    )
    response = tmp_client.instrument_updates.create(create_instrument_update_request=req)
    return response


def test_create(config):
    tmp_client = finix.FinixClient(config)
    str_now = str(datetime.now())
    req_string = "{\"merchant\":\"MUucec6fHeaWo3VHYoSkUySM\",  \"idempotency_id\":\"" + str_now + "\" }"
    req = CreateInstrumentUpdateRequest(
        file=open('tests/test_file.png', 'rb'),
        request=req_string,
    )
    response = tmp_client.instrument_updates.create(create_instrument_update_request=req)
    assert response.id[:2] == 'IU'
    assert response.merchant == 'MUucec6fHeaWo3VHYoSkUySM'
    assert response.state == 'PENDING'


def test_get(config, c_update):
    tmp_client = finix.FinixClient(config)
    id = c_update.id
    response = tmp_client.instrument_updates.get(id)
    assert response.id[:2] == 'IU'
    assert response.merchant == 'MUucec6fHeaWo3VHYoSkUySM'
    assert response.state == 'PENDING'


# newly uploaded file not immediately ready for download
def test_download(config, c_update):
    tmp_client = finix.FinixClient(config)
    id = c_update.id
    with pytest.raises(finix.ApiException) as e:
        tmp_client.instrument_updates.download(id, format='json')
    assert e.value.status == 404
    assert e.value.reason == 'Not Found'