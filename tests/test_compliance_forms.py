from ipaddress import ip_address
import pytest
import finix
from finix.models import *

def test_get_compliance_form(client06):
    id = "cf_fEojUGLjwUiqNTBp68JWq8"
    response = client06.compliance_forms.get(id)
    assert response.linked_to == "MUfnskvHiiDgP7x3TVL2LkG3"
    assert response.linked_type == "MERCHANT"
    assert response.type == "PCI_SAQ_A"
    assert response.pci_saq_a['is_accepted'] == False
    assert response.compliance_form_template == "cft_wua8ua1yLAcHRK9mx2mF9K"
    assert response.files['unsigned_file'] == "FILE_fFGMCY4sxGYTqpjnXh54kC"

def test_update_compliance_form(client07):
    id = "cf_pzJCPAqrt9Z5653V3iXRDv"
    request = UpdateComplianceFormRequest(
        pci_saq_a = UpdateComplianceFormRequestPciSaqA(
            name = "test-python",
            signed_at = "2022-03-18T16:42:55Z", 
            user_agent = "Mozilla 5.0(Macintosh; IntelMac OS X 10 _14_6)", 
            ip_address = "42.1.1.113", 
            title = "cto"
        )
    )
    response = client07.compliance_forms.update(id, update_compliance_form_request = request)
    print(response)
    assert response.pci_saq_a['name'] == request.pci_saq_a['name']
    assert response.pci_saq_a['title'] == request.pci_saq_a['title'] 
    assert response.pci_saq_a['signed_at'] == request.pci_saq_a['signed_at']
    assert response.pci_saq_a['user_agent'] == request.pci_saq_a['user_agent']
    assert response.pci_saq_a['ip_address'] == request.pci_saq_a['ip_address']
