import pilo
from pilo import Form
from pilo.fields import Boolean, Dict, String, SubForm, Integer

class Create(Form):
    tags = Dict(String(), String(), default=pilo)
    processor = String(default=pilo.NONE)


