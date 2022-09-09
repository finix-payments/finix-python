import pytest
import finix
from finix.models import *


def test_get_file(client00, file):
    id = file.id
    response = client00.files.get(id)
    assert response.id[:4] == 'FILE'
    assert response.display_name == 'pytest_file'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_create_file(client00):
    request = CreateFileRequest(
        display_name="pytest_create",
        linked_to="MU2n7BSovtwYsWYZF6rBnnzk",
        type="DRIVERS_LICENSE_FRONT",
        tags=Tags(
            test_key_101 = "test_val_101"
        )
    )
    response = client00.files.create(create_file_request=request)
    assert response.id[:4] == 'FILE'
    assert response.display_name == 'pytest_create'
    assert response.tags['test_key_101'] == 'test_val_101'


def test_get_external_link(client00, external_link):
    file_id = external_link.file_id
    elink_id = external_link.id
    response = client00.files.get_external_link(file_id,elink_id)
    assert response.id[:2] == 'EL'
    assert response.type == 'UPLOAD'
    assert response.tags['test_key_110'] == 'test_val_110'


def test_create_external_link(client00, file):
    fid = file.id
    request = CreateExternalLinkRequest(
        type="UPLOAD",
        duration=30,
        tags=Tags(
            test_key_111 = "test_val_111"
        )
    )
    response = client00.files.create_external_link(fid, create_external_link_request=request)
    assert response.id[:2] == 'EL'
    assert response.type == 'UPLOAD'
    assert response.tags['test_key_111'] == 'test_val_111'


def test_upload_file(client00, file):
    fid = file.id
    request = UploadFileRequest(
        file=open('tests/test_file.png', 'rb')
    )
    response = client00.files.upload(fid, upload_file_request=request)
    assert response.id[:4] == 'FILE'
    assert response.extension == 'png'
    assert response.tags['test_key_100'] == 'test_val_100'


def test_download_file(client00):
    id = 'FILE_bJecqoRPasStEPVpvKHtgA'
    response = client00.files.download(id)
    assert isinstance(response.read(), bytes)