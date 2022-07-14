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
    tmp_client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    req = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = tmp_client.disputes.create_dispute_evidence(id, create_dispute_evidence_request=req)
    return response


def test_create_dispute_evidence(config):
    tmp_client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    req = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = tmp_client.disputes.create_dispute_evidence(id, create_dispute_evidence_request=req)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'


def test_get(config):
    tmp_client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = tmp_client.disputes.get(id)
    assert response.id[:2] == 'DI'
    assert response.application == 'APgPDQrLD52TYvqazjHJJchM'
    assert response.reason == 'FRAUD'


def test_get_dispute_evidence(config, c_evidence):
    tmp_client = finix.FinixClient(config)
    did = 'DIs7yQRkHDdMYhurzYz72SFk'
    eid = c_evidence.id
    response = tmp_client.disputes.get_dispute_evidence(did,eid)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'