from tkinter import FALSE
import pytest
import finix
from finix.models import *

def test_get_compliance_form(client06):
    id = "cf_fEojUGLjwUiqNTBp68JWq8"
    response = client06.compliance_forms.get_compliance_forms(id)
    assert response.linked_to == "MUfnskvHiiDgP7x3TVL2LkG3"
    assert response.linked_type == "MERCHANT"
    assert response.type == "PCI_SAQ_A"
    assert response.pci_saq_a['is_accepted'] == FALSE
    assert response.compliance_form_template == "cft_wua8ua1yLAcHRK9mx2mF9K"
    assert response.files['unsigned_file'] == "FILE_fFGMCY4sxGYTqpjnXh54kC"