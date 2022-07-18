import pytest
import finix
from finix.models import *


def test_get_verification(client00, verification):
    id = verification.id
    response = client00.verifications.get(id)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_verification(client00):
    request = CreateVerificationRequest(
        merchant='MUucec6fHeaWo3VHYoSkUySM',
        processor='DUMMY_V1',
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = client00.verifications.create(create_verification_request=request)
    assert response.id[:2] == 'VI'
    assert response.processor == 'DUMMY_V1'
    assert response.tags['test_key_110'] == 'test_val_110'