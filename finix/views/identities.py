import pilo
from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict, SubForm, Integer

from finix.forms.addresses import Address
from finix.forms.dates import Date
from finix import enums

from . import ResourceView


class Entity(Form):
    title = String()
    first_name = String()
    last_name = String()
    email = String()
    business_name = String()
    business_type = String()
    business_phone = String()
    doing_business_as = String()
    phone = String()
    personal_address = SubForm(Address)
    mcc = String()
    dob = SubForm(Date)
    max_transaction_amount = Integer()
    url = String()
    annual_card_volume = Integer()
    has_accepted_credit_cards_previously = Boolean()
    incorporation_date = SubForm(Date)
    principal_percentage_ownership = Integer()
    ownership_type = String(choices=enums.OwnershipType)
    short_business_name = String()
    tax_id_provided = Boolean()
    business_tax_id_provided = Boolean()
    default_statement_descriptor = String()
    amex_mid = String(default=pilo.NONE)
    discover_mid = String(default=pilo.NONE)


class Identity(ResourceView):

    id = String()
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    application = String(default=None)
    entity = SubForm(Entity)
    tags = Dict(String(), String())
    links = Dict(String(), Dict(String(), String()), src='_links')

    def set_(self):
        form = forms.applications.ApplicationUpdateForm(processing_enabled=True)
        return self._api_client.applications.id(self.id).put(form)


