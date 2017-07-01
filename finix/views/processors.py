from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict

from . import ResourceView


class Processor(ResourceView):
    id = String()
    identity = String()
    verification = String()
    merchant_profile = String()
    processor = String()
    processing_enabled  = Boolean()
    settlement_enabled = Boolean()
    onboarding_state = String()
    tags = Dict(String(), String())
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')
