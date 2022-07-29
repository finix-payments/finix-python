import pytest
import finix
from finix.models import *
from datetime import datetime


def test_create_instrument_update(client00):
    str_now = str(datetime.now())
    req_string = "{\"merchant\":\"MUucec6fHeaWo3VHYoSkUySM\",  \"idempotency_id\":\"" + str_now + "\" }"
    request = CreateInstrumentUpdateRequest(
        file=open('tests/test_file.png', 'rb'),
        request=req_string,
    )
    response = client00.instrument_updates.create(create_instrument_update_request=request)
    assert response.id[:2] == 'IU'
    assert response.merchant == 'MUucec6fHeaWo3VHYoSkUySM'
    assert response.state == 'PENDING'


def test_get_instrument_update(client00, instrument_update):
    id = instrument_update.id
    response = client00.instrument_updates.get(id)
    assert response.id[:2] == 'IU'
    assert response.merchant == 'MUucec6fHeaWo3VHYoSkUySM'
    assert response.state == 'PENDING'


# newly uploaded file not immediately ready for download
def test_download_instrument_update_fail(client00, instrument_update):
    id = instrument_update.id
    with pytest.raises(finix.ApiException) as e:
        client00.instrument_updates.download(id, format='json')
    assert e.value.status == 404
    assert e.value.reason == 'Not Found'
    assert e.value.body.no_error_body == True


def test_download_instrument_update_success(client00):
    id = 'IUp9oSWhWUF31DPrJ8CojQeQ'
    response = client00.instrument_updates.download(id, format='json')
    assert isinstance(response.read(), bytes)