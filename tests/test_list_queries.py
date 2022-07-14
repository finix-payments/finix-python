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
def config01():
    configuration = Configuration(
        username = 'USbkjk46XqUTQHN3i2jaVnc1',
        password = 'ac915962-2757-49ea-aeee-10960a408b99',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def config02():
    configuration = Configuration(
        username = 'USpumes23XhzHwXqiy9bfX2B',
        password = 'c69d39e3-f9ff-4735-8c3e-abca86441906',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def config03():
    configuration = Configuration(
        username = 'USjHFGYvecE4LBitYG8KDE2g',
        password = 'b698f403-d9b7-4157-82d8-162cea8c8cc3',
        environment = Environment.SANDBOX
    )
    return configuration


@pytest.fixture
def config04():
    configuration = Configuration(
        username = 'USimz3zSq5R2PqiEBXY6rSiJ',
        password = '8bacba32-9550-48ff-b567-fe7648947041',
        environment = Environment.SANDBOX
    )
    return configuration


def test_list_transfers(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.transfers.list(limit=5)
    assert isinstance(response, TransfersList)
    assert response.page['limit'] == 5
    assert response.embedded['transfers'][0]['id'][:2] == 'TR'


def test_list_reversals(config):
    tmp_client = finix.FinixClient(config)
    id = 'TRacB6Q6GcW6yvFUKawSnMEP'
    response = tmp_client.transfers.list_transfers_reversals(id, limit=5)
    assert isinstance(response, TransfersList)
    assert response.page['limit'] == 5
    assert response.embedded['transfers'][0]['type'] == 'REVERSAL'


def test_list_authorizations(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.authorizations.list(limit=5)
    assert isinstance(response, AuthorizationsList)
    assert response.page['limit'] == 5
    assert response.embedded['authorizations'][0]['id'][:2] == 'AU'


def test_list_identities(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.identities.list(limit=5)
    assert isinstance(response, IdentitiesList)
    assert response.page['limit'] == 5
    assert response.embedded['identities'][0]['id'][:2] == 'ID'


def test_list_associated_identities(config):
    tmp_client = finix.FinixClient(config)
    id ='IDpYDM7J9n57q849o9E9yNrG'
    response = tmp_client.identities.list_assocaiated_identities(id, limit=5)
    assert isinstance(response, IdentitiesList)
    assert response.page['limit'] == 5
    assert response.embedded['identities'][0]['id'][:2] == 'ID'


def test_list_merchants(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.merchants.list(limit=5)
    assert isinstance(response, MerchantsList)
    assert response.page['limit'] == 5
    assert response.embedded['merchants'][0]['id'][:2] == 'MU'


def test_list_balance_transfers(config01):
    tmp_client = finix.FinixClient(config01)
    response = tmp_client.balance_transfers.list(limit=5)
    assert isinstance(response, BalanceTransferList)
    assert response.page['limit'] == 5
    assert response.embedded['balance_transfers'][0]['id'][:2] == 'BT'


def test_list_disputes(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.disputes.list(limit=5)
    assert isinstance(response, DisputesList)
    assert response.page['limit'] == 5
    assert response.embedded['disputes'][0]['id'][:2] == 'DI'


def test_list_dispute_evidences(config):
    tmp_client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = tmp_client.disputes.list_dispute_evidence_by_dispute_id(id, limit=5)
    assert isinstance(response, DisputeEvidenceList)
    assert response.page['limit'] == 5
    assert response.embedded['evidences'][0]['id'][:2] == 'DF'


def test_list_dispute_adjustment_transfers(config):
    tmp_client = finix.FinixClient(config)
    id = 'DIs7yQRkHDdMYhurzYz72SFk'
    response = tmp_client.disputes.list_disputes_adjustments(id, limit=5)
    assert isinstance(response, AdjustmentTransfersList)
    assert response.page['limit'] == 5
    assert response.embedded['transfers'][0]['id'][:2] == 'TR'


def test_list_files(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.files.list(limit=5)
    assert isinstance(response, FilesList)
    assert response.page['limit'] == 5
    assert response.embedded['files'][0]['id'][:4] == 'FILE'


def test_list_external_links(config):
    tmp_client = finix.FinixClient(config)
    id = 'FILE_bJecqoRPasStEPVpvKHtgA'
    response = tmp_client.files.list_external_links(id, limit=5)
    assert isinstance(response, ExternalLinksList)
    assert response.page['limit'] == 5
    assert response.embedded['external_links'][0]['id'][:2] == 'EL'   


def test_list_settlements(config02):
    tmp_client = finix.FinixClient(config02)
    response = tmp_client.settlements.list(limit=5)
    assert isinstance(response, SettlementsList)
    assert response.page['limit'] == 5
    assert response.embedded['settlements'][0]['id'][:2] == 'ST'


def test_list_settlements_funding_transfers(config02):
    tmp_client = finix.FinixClient(config02)
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = tmp_client.settlements.list_funding_transfers(id,limit=5)
    assert isinstance(response, TransfersList)
    assert response.page['limit'] == 5


def test_list_settlements_transfers(config02):
    tmp_client = finix.FinixClient(config02)
    id = 'STmCc8GbjjX33SdymwNhb9Et'
    response = tmp_client.settlements.list_transfers_by_settlement_id(id, limit=5)
    assert isinstance(response, TransfersList)
    assert response.page['limit'] == 5


def test_list_webhooks(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.webhooks.list()
    assert isinstance(response, WebhooksList)
    assert response.embedded['webhooks'][0]['id'][:2] == 'WH'


def test_list_verifications(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.verifications.list(limit=5)
    assert isinstance(response, VerificationsList)
    assert response.page['limit'] == 5
    assert response.embedded['verifications'][0]['id'][:2] == 'VI'


def test_list_merchant_verifications(config):
    tmp_client = finix.FinixClient(config)
    id = 'MUgWbPVvtKbzjKNNGKqdQYV7'
    response = tmp_client.verifications.list_by_merchant_id(id,limit=5)
    assert isinstance(response, VerificationsList)
    assert response.page['limit'] == 5
    assert response.embedded['verifications'][0]['id'][:2] == 'VI'


def test_list_merchant_profiles(config03):
    tmp_client = finix.FinixClient(config03)
    response = tmp_client.merchant_profiles.list(limit=5)
    assert isinstance(response, MerchantProfilesList)
    assert response.page['limit'] == 5
    assert response.embedded['merchant_profiles'][0]['id'][:2] == 'MP'


def test_list_fee_profiles(config04):
    tmp_client = finix.FinixClient(config04)
    response = tmp_client.fee_profiles.list(limit=5)
    assert isinstance(response, FeeProfilesList)
    assert response.page['limit'] == 5
    assert response.embedded['fee_profiles'][0]['id'][:2] == 'FP'


def test_list_payment_instruments(config):
    tmp_client = finix.FinixClient(config)
    response = tmp_client.payment_instruments.list(limit=5)
    assert isinstance(response, PaymentInstrumentsList)
    assert response.page['limit'] == 5
    assert response.embedded['payment_instruments'][0]['id'][:2] == 'PI'