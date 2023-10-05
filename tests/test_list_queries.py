import pytest
import finix
from finix.models import *
from finix.model.finix_utils import FinixList, PaginationException


def test_list_transfers(client00):
    response = client00.transfers.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'TR'
    next_list1 = response.list_next()
    next_list2 = next_list1.list_next()
    next_list3 = next_list2.list_next()
    assert isinstance(next_list1, FinixList)
    assert len(next_list1) <= 5
    assert next_list1[0].id[:2] == 'TR'
    assert isinstance(next_list2, FinixList)
    assert len(next_list2) <= 5
    assert next_list2[0].id[:2] == 'TR'
    assert isinstance(next_list3, FinixList)
    assert len(next_list3) <= 5
    assert next_list3[0].id[:2] == 'TR'
    assert response[0].id != next_list1[0].id
    assert next_list1[0].id != next_list2[0].id
    assert next_list2[0].id != next_list3[0].id


def test_list_reversals(client00):
    id = 'TRacB6Q6GcW6yvFUKawSnMEP'
    response = client00.transfers.list_transfers_reversals(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].type == 'REVERSAL'


def test_list_authorizations(client00):
    response = client00.authorizations.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'AU'


def test_list_identities(client00):
    response = client00.identities.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'ID'
    next_list1 = response.list_next()
    next_list2 = next_list1.list_next()
    next_list3 = next_list2.list_next()
    assert isinstance(next_list1, FinixList)
    assert len(next_list1) <= 5
    assert next_list1[0].id[:2] == 'ID'
    assert isinstance(next_list2, FinixList)
    assert len(next_list2) <= 5
    assert next_list2[0].id[:2] == 'ID'
    assert isinstance(next_list3, FinixList)
    assert len(next_list3) <= 5
    assert next_list3[0].id[:2] == 'ID'
    assert response[0].id != next_list1[0].id
    assert next_list1[0].id != next_list2[0].id
    assert next_list2[0].id != next_list3[0].id


def test_list_associated_identities(client00):
    id ='IDpYDM7J9n57q849o9E9yNrG'
    response = client00.identities.list_associated_identities(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'ID'


def test_list_merchants(client00):
    response = client00.merchants.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'MU'


def test_list_balance_transfers(client01):
    response = client01.balance_transfers.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'BT'


def test_list_disputes(client00):
    response = client00.disputes.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'DI'


def test_list_dispute_evidences(client00):
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = client00.disputes.list_dispute_evidence_by_dispute_id(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'DF'


def test_list_dispute_adjustment_transfers(client00):
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = client00.disputes.list_disputes_adjustments(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'TR'


def test_list_files(client00):
    response = client00.files.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:4] == 'FILE'


def test_list_external_links(client00):
    id = 'FILE_bJecqoRPasStEPVpvKHtgA'
    response = client00.files.list_external_links(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'EL'


def test_list_settlements(client04):
    response = client04.settlements.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'ST'


def test_list_settlements_funding_transfers(client04):
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = client04.settlements.list_funding_transfers(id,limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response.has_more == False
    with pytest.raises(PaginationException) as e:
        response.list_next()
    assert e.value.message == 'list_next() fails: either pagination information is missing or there is no more resource to fetch!'


def test_list_settlements_transfers(client04):
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = client04.settlements.list_transfers_by_settlement_id(id, limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response.has_more == False
    with pytest.raises(PaginationException) as e:
        response.list_next()
    assert e.value.message == 'list_next() fails: either pagination information is missing or there is no more resource to fetch!'


def test_list_webhooks(client00):
    response = client00.webhooks.list()
    assert isinstance(response, FinixList)
    assert response[0].id[:2] == 'WH'


def test_list_verifications(client00):
    response = client00.verifications.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'VI'


def test_list_merchant_verifications(client00):
    id = 'MUgWbPVvtKbzjKNNGKqdQYV7'
    response = client00.verifications.list_by_merchant_id(id,limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'VI'
    next_list1 = response.list_next()
    next_list2 = next_list1.list_next()
    next_list3 = next_list2.list_next()
    assert isinstance(next_list1, FinixList)
    assert len(next_list1) <= 5
    assert next_list1[0].id[:2] == 'VI'
    assert isinstance(next_list2, FinixList)
    assert len(next_list2) <= 5
    assert next_list2[0].id[:2] == 'VI'
    assert isinstance(next_list3, FinixList)
    assert len(next_list3) <= 5
    assert next_list3[0].id[:2] == 'VI'
    assert response[0].id != next_list1[0].id
    assert next_list1[0].id != next_list2[0].id
    assert next_list2[0].id != next_list3[0].id


def test_list_merchant_profiles(client02):
    response = client02.merchant_profiles.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'MP'


def test_list_fee_profiles(client03):
    response = client03.fee_profiles.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'FP'


def test_list_payment_instruments(client00):
    response = client00.payment_instruments.list(limit=5)
    assert isinstance(response, FinixList)
    assert len(response) <= 5
    assert response[0].id[:2] == 'PI'
