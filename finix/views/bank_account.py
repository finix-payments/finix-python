from pilo import Form
from pilo.fields import String, Datetime, Dict

from . import ResourceView


class BankAccount(ResourceView):

    id = String()
    fingerprint = String()
    bank_code = String()
    country = String()
    masked_account_number = String()
    name = String()
    account_type = String()
    instrument_type = String()
    type = String()
    currency = String ()
    identity = String ()
    tags = Dict(String(), String())
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')
