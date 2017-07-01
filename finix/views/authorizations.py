from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict, Integer, List

from . import ResourceView


class Application(ResourceView):

    id = String()
    amount = Integer()
    tags = Dict(String(), String())
    state = String()
    currency = String()
    transfer = String()
    raw = String()
    messages =  List()
    trace_id = String()
    source = String()
    merchant_identity = String()
    is_void = String()
    expires_at = String()
    idempotency_id = String()
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')
