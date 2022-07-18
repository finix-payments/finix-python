import pytest
import finix
from finix.models import *


def test_create_dispute_evidence(client00):
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    request = CreateDisputeEvidenceRequest(
        file=open('tests/test_file.png', 'rb'),
    )
    response = client00.disputes.create_dispute_evidence(id, create_dispute_evidence_request=request)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'


def test_get_dispute(client00):
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = client00.disputes.get(id)
    assert response.id[:2] == 'DI'
    assert response.application == 'APgPDQrLD52TYvqazjHJJchM'
    assert response.reason == 'FRAUD'


def test_get_dispute_evidence(client00, dispute_evidence):
    dispute_id = 'DIs7yQRkHDdMYhurzYz72SFk'
    evidence_id = dispute_evidence.id
    response = client00.disputes.get_dispute_evidence(dispute_id,evidence_id)
    assert response.id[:2] == 'DF'
    assert response.tags['file-name'] == 'test_file.png'
    assert response.tags['content-type'] == 'image/png'