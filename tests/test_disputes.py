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
def c_evidence(config):
    client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    request = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = client.disputes.create_dispute_evidence(id, create_dispute_evidence_request=request)
    return response


def test_create_dispute_evidence(config):
    client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    request = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = client.disputes.create_dispute_evidence(id, create_dispute_evidence_request=request)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'


def test_get_dispute(config):
    client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = client.disputes.get(id)
    assert response.id[:2] == 'DI'
    assert response.application == 'APgPDQrLD52TYvqazjHJJchM'
    assert response.reason == 'FRAUD'


def test_get_dispute_evidence(config, c_evidence):
    client = finix.FinixClient(config)
    did = 'DIs7yQRkHDdMYhurzYz72SFk'
    eid = c_evidence.id
    response = client.disputes.get_dispute_evidence(did,eid)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'