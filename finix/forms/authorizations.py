from pilo import Form, NONE
from pilo.fields import Boolean, Dict, String, Integer

from finix import enums

class Create(Form):

    merchant_identity=String()
    currency=String()
    amount=Integer()
    source=String()
    tags=Dict(String(), String(), default=NONE)
