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
def c_file(config):
    client = finix.FinixClient(config)
    request = CreateFileRequest(
        display_name="pytest_file",
        linked_to="MU2n7BSovtwYsWYZF6rBnnzk",
        type="DRIVERS_LICENSE_FRONT",
        tags=Tags(
            test_key_100 = "test_val_100"
        )
    )
    response = client.files.create(create_file_request=request)
    return response


@pytest.fixture
def c_elink(config, c_file):
    client = finix.FinixClient(config)
    fid = c_file.id
    request = CreateExternalLinkRequest(
        type="UPLOAD",
        duration=30,
        tags=Tags(
            test_key_110 = "test_val_110"
        )
    )
    response = client.files.create_external_link(fid, create_external_link_request=request)
    return response


def test_get_file(config, c_file):
    client = finix.FinixClient(config)
    id = c_file.id
    response = client.files.get(id)
    assert response.id[:4] == 'FILE'
    assert response.display_name == 'pytest_file'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_file(config):
    client = finix.FinixClient(config)
    request = CreateFileRequest(
        display_name="pytest_create",
        linked_to="MU2n7BSovtwYsWYZF6rBnnzk",
        type="DRIVERS_LICENSE_FRONT",
        tags=Tags(
            test_key_101 = "test_val_101"
        )
    )
    response = client.files.create(create_file_request=request)
    assert response.id[:4] == 'FILE'
    assert response.display_name == 'pytest_create'
    assert response.tags['test_key_101'] == 'test_val_101'


def test_get_external_link(config, c_elink):
    client = finix.FinixClient(config)
    fid = c_elink.file_id
    eid = c_elink.id
    response = client.files.get_external_link(fid,eid)
    assert response.id[:2] == 'EL'
    assert response.type == 'UPLOAD'
    assert response.tags['test_key_110'] == 'test_val_110'


def test_create_external_link(config, c_file):
    client = finix.FinixClient(config)
    fid = c_file.id
    request = CreateExternalLinkRequest(
        type="UPLOAD",
        duration=30,
        tags=Tags(
            test_key_111 = "test_val_111"
        )
    )
    response = client.files.create_external_link(fid, create_external_link_request=request)
    assert response.id[:2] == 'EL'
    assert response.type == 'UPLOAD'
    assert response.tags['test_key_111'] == 'test_val_111'


def test_upload_file(config, c_file):
    client = finix.FinixClient(config)
    fid = c_file.id
    request = UploadFileRequest(
        file=open('tests/test_file.png', 'rb')
    )
    response = client.files.upload_file(fid, upload_file_request=request)
    assert response.id[:4] == 'FILE'
    assert response.extension == 'png'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_download_file(config):
    client = finix.FinixClient(config)
    id = 'FILE_bJecqoRPasStEPVpvKHtgA'
    response = client.files.download_file(id)
    assert isinstance(response.read(), bytes)