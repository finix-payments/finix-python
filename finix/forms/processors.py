import pilo
from pilo import Form
from pilo.fields import Field, String, Dict

class Create(Form):
    type = String()
    config = Dict(String(), Field())
