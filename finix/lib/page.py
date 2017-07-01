from pilo import Form
from pilo.fields import Dict, Field, String, Integer, SubForm


class Link(Form):
    href = String()


class PageInfo(Form):
    count = Integer()
    limit = Integer()
    offset = Integer()


class Links(Form):
    first = SubForm(Link)
    last = SubForm(Link)
    prev = SubForm(Link)
    next = SubForm(Link)
    self = SubForm(Link)


def ApiPage(api_client, view, raw):

    class Page(Form):

        _view = view

        _api_client = api_client

        page = SubForm(PageInfo)
        links = Dict(String(), Dict(String(), String()), src='_links')
        embedded = Field(src='_embedded')
        contents = Field(default=None)

        @contents.compute
        def contents(self):
            keys = self.embedded.keys()
            if keys:
                views = map(self._view, self.embedded.get(keys[0]))
                for view in views:
                    view._api_client = self._api_client
            return []

    return Page(raw)
