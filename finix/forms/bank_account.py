import pilo
from pilo import Form
from pilo.fields import Dict, String

class Create(Form):

    tags = Dict(String(), String(), default=pilo)
    account_type = String()
    name = String()
    country = String()
    bank_code = String()
    account_number = String()
    type = String()
    identity = String()



