import pilo
from pilo import Form
from pilo.fields import String


class Address(Form):

    line1 = String()
    line2 = String(default=pilo.NONE)
    city = String()
    region = String()
    postal_code = String()
    country = String()
