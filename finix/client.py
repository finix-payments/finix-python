from finix import resources
from finix import views


class ApiClient(object):

    def __init__(self, url, user, password):

        self.url = url
        self.user = user
        self.password = password

        self.users = resources.Index(self, '/users', views.User, [])
        self.applications = resources.Index(self, '/applications', views.Application, [
            resources.Index(self, '/processors', views.Processor, [])
        ]),
        # self.processors = resources.Index(self, '/applications', views.Application, [
        #     resources.Index(self,'/processors',views.Processor)
        # ]),
        self.identities = resources.Index(self, '/identities', views.Identity, [
            resources.Index(self, '/merchants', views.Merchant, [])
        ])
        self.bank_account = resources.Index(self, '/payment_instruments', views.BankAccount, [])
