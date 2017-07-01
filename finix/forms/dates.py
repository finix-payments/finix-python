import pilo
from pilo import Form
from pilo.fields import String, Integer


class Date(Form):

    year = Integer()
    day = Integer()
    month = Integer()
