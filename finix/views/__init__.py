from pilo import Form


class ResourceView(Form):

    _api_client = None


from users import User
from applications import Application
from identities import Identity
from bank_account import BankAccount
from merchants import Merchant
from processors import Processor