from pilo import Form, NONE
from pilo.fields import Boolean, Dict, String

from finix import enums

class Create(Form):

  enabled = Boolean(default=True)
  role = String(choices=enums.UserRoles)
  tags = Dict(String(), String(), default=NONE)

