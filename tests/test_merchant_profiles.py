import pytest
import finix
from finix.models import *


def test_get_merchant_profile(client03):
    id = 'MP9J4ALZHx4pa5i1p5G5jeKY'
    response = client03.merchant_profiles.get(id)
    assert response.id[:2] == 'MP'
    assert response.application == 'AP7yJr75Zycq9Fz6CpK8h9gn'


def test_update_merchant_profile(client03):
    id = 'MP9J4ALZHx4pa5i1p5G5jeKY'
    request = {
        'tags':{'test_key_100':'test_val_100'}
    }
    response = client03.merchant_profiles.update(id,update_merchant_profile_request=request)
    assert response.id[:2] == 'MP'
    assert response.application == 'AP7yJr75Zycq9Fz6CpK8h9gn'
    assert response.tags['test_key_100'] == 'test_val_100'