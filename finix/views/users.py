from pilo import Form
from pilo.fields import String, Boolean, Datetime, Dict

from finix import enums

from . import ResourceView


class User(ResourceView):

    id = String()
    application = String(default=None)
    password = String()
    identity = String()
    enabled = Boolean()
    role = String(choices=enums.UserRoles)
    tags = Dict(String(), String())
    created_at = Datetime(format='iso8601')
    updated_at = Datetime(format='iso8601')
    links = Dict(String(), Dict(String(), String()), src='_links')
