import pytest
import finix
from finix.models import *


def test_create_onboarding_form(client00):
    request = CreateOnboardingFormRequest(
        onboarding_data = OnboardingFormOnboardingData(
            max_transaction_amount = 100000
        ),
        merchant_processors = [CreateOnboardingFormRequestMerchantProcessors(
            processor = "LITLE_V1"
        )],
        onboarding_link_details = CreateOnboardingFormRequestOnboardingLinkDetails(
            return_url = "https://www.finix.com/docs",
            expired_session_url = "https://www.finix.com/",
            terms_of_service_url = "https://www.finix.com/terms-and-policies",
            fee_details_url = "https://www.finix.com/docs",
            expiration_in_minutes = "30"
        )
    )
    response = client00.onboarding_forms.create(create_onboarding_form_request=request)
    assert response.onboarding_data['max_transaction_amount'] == 100000
    
    assert response.merchant_processors[0]['processor'] == "LITLE_V1"


def test_create_onboarding_form_link(client00, onboarding_form):
    id = onboarding_form.id
    request = CreateOnboardingFormLinkRequest(
        terms_of_service_url = "https://www.finix.com/terms-and-policies",
        return_url = "https://www.finix.com/docs",
        fee_details_url = "https://www.finix.com/docs",
        expired_session_url = "https://www.finix.com/",
        expiration_in_minutes = 30
    )
    response = client00.onboarding_forms.create_link(id, create_onboarding_form_link_request=request)
    assert response['link_url'].find(id) != -1


def test_get_onboarding_form(client00, onboarding_form):
    id = onboarding_form.id
    response = client00.onboarding_forms.get(id)
    assert response.onboarding_data['max_transaction_amount'] == 100000
    assert response.id == id
    assert response.merchant_processors[0]['processor'] == "LITLE_V1"
