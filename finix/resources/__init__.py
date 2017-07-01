import json

import requests
from finix import lib
from finix import mimes


headers = {'Content-Type': 'application/json'}


class Index(object):

    def __init__(self, client, path, view, subindexes):
        self.client = client
        self.path = path
        self.view = view
        self.subindexes = subindexes

    def nest(self, path):
        self.path = lib.path.join(path, self.path)
        return self

    def id(self, value):
        print '--------------------------'
        print self.client
        print self.path
        print self.view
        print self.subindexes
        print '--------------------------'
        return Resource(self.client, self.path, self.view, value, self.subindexes)

    def get(self):
        url = lib.path.join(self.client.url, self.path)
        if self.client.user and self.client.password:
            response = requests.get(
                url,
                auth=(self.client.user, self.client.password),
                headers=headers,
            )
        else:
            response = requests.get(url, headers=headers)
        return lib.ApiPage(self.client, self.view, response.json())


    def post(self, form):
        url = lib.path.join(self.client.url, self.path)
        body = mimes.Json.encode(form)
        print 'Request:'
        print body

        if self.client.user and self.client.password:
            response = requests.post(
                url,
                body,
                auth=(self.client.user, self.client.password),
                headers=headers,
            )
        else:
            response = requests.post(url, body, headers=headers)
        if response.status_code >= 300:
            payload = json.dumps(response.json(), indent=4)
            message = "\n  HTTP {} \n  API Response:\n    {}\n\n".format(
                response.status_code,
                payload)
            raise Exception(message)
        print 'Response:'
        print mimes.Json.encode(response.json())
        resource_view = self.view(response.json())
        resource_view._api_client = self.client
        return resource_view


class Resource(object):

    def __init__(self, client, path, view, id, indicies):
        self.client = client
        self.path = lib.path.join(path, id)
        self.view = view
        self.id = id
        self.indicies = indicies
        for index in self.indicies:
            index_name = index.path.replace('/', '')
            setattr(self, index_name, index.nest(self.path))

    def get(self):
        url = lib.path.join(self.client.url, self.path)
        if self.client.user and self.client.password:
            response = requests.get(
                url,
                auth=(self.client.user, self.client.password),
                headers=headers,
            )
        else:
            response = requests.get(url, headers=headers)
        resource_view = self.view(response.json())
        resource_view._api_client = self.client
        return resource_view

    def put(self, form):
        url = lib.path.join(self.client.url, self.path)
        body = mimes.Json.encode(form)
        if self.client.user and self.client.password:
            response = requests.put(
                url,
                body,
                auth=(self.client.user, self.client.password),
                headers=headers,
            )
        else:
            response = requests.put(url, body, headers=headers)
        if response.status_code >= 300:
            payload = json.dumps(response.json(), indent=4)
            message = "\n  HTTP {} \n  API Response:\n    {}\n\n".format(
                response.status_code,
                payload)
            raise Exception(message)
        resource_view = self.view(response.json())
        resource_view._api_client = self.client
        return resource_view


class User(object):

    def __init__(self, api):
        self.api = api

    @classmethod
    def api(cls, api_client):
        return User(api_client)

    def get(self, id):
        return self.api.users.id(id).get()

    def save(self, form):
        return self.api.users.post(form)
