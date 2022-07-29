import pytest
import finix
from finix.models import *


def test_get_fee_profile(client03, fee_profile):
    id = fee_profile.id
    response = client03.fee_profiles.get(id)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 100


def test_create_fee_profile(client03):
    request = CreateFeeProfileRequest(
        fixed_fee=10,
        application = 'APmuwPBaW8pVcwb4vCTHQH32',
        tags=Tags(
	        test_key_110 = "test_val_110"
        )
    )
    response = client03.fee_profiles.create(create_fee_profile_request=request)
    assert response.id[:2] == 'FP'
    assert response.application == 'APmuwPBaW8pVcwb4vCTHQH32'
    assert response.fixed_fee == 10