from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict

from finix import forms
from . import ResourceView


class Application(ResourceView):

    id = String()
    enabled = Boolean()
    tags = Dict(String(), String())
    owner = String()
    processing_enabled = Boolean()
    settlement_enabled = Boolean()
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')

    def enable_processing(self):
        form = forms.applications.ApplicationUpdateForm(processing_enabled=True)
        return self._api_client.applications.id(self.id).put(form)

    def register_processor(self):

        form = forms.processors.Create(type='DUMMY_V1', config=dict(canDebitBankAccount=True))
        response = self._api_client.applications.id(self.id).put(form)
        print '2222222222222222222222222222'
        print response
        return response



