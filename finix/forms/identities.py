import pilo
from pilo import Form
from pilo.fields import Boolean, Dict, String, SubForm, Integer

from finix import enums

from finix.forms.addresses import Address
from finix.forms.dates import Date

class Entity(Form):

    first_name = String()
    last_name = String()
    email = String()
    tax_id = String()
    personal_address = SubForm(Address)
    mcc = String()
    dob = SubForm(Date)
    has_accepted_credit_cards_previously = Boolean(default=False)
    url = String()
    annual_card_volume = String()
    default_statement_descriptor = String()
    phone = String()
    business_name = String()
    business_type = String(choices=enums.BusinessType)
    business_tax_id = String(default='12345567')
    business_phone = String(default='1234567899')
    business_address = SubForm(Address)
    max_transaction_amount = Integer()
    doing_business_as = String()
    title = String()
    short_business_name = String()
    incorporation_date = SubForm(Date)
    principal_percentage_ownership = Integer()
    ownership_type = String(choices=enums.OwnershipType)


class Create(Form):
    tags = Dict(String(), String(), default=pilo)
    entity = SubForm(Entity)
