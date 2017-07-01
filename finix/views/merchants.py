from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict, SubForm

from . import ResourceView

class Config(ResourceView):
    canDebitBankAccount = Boolean()
    key1 = String()

class Merchant(ResourceView):
    id = String()
    application = String()
    default_merchant_profile = String()
    processor = String()
    config = SubForm(Config)
    enabled  = Boolean()
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')
