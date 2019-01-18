from __future__ import unicode_literals
import collections
import datetime
import logging
import json as _json
import uuid

import pilo


logger = logging.getLogger(__name__)


MIME = collections.namedtuple('MIME', [
    'accept_type',
    'content_type',
    'encode',
    'source',
])


_JSONSource = pilo.source.JsonSource


class _JSONEncoder(_json.JSONEncoder):

    def __init__(self, indent=4, sort_keys=True):
        super(_JSONEncoder, self).__init__(indent=indent, sort_keys=sort_keys)

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.isoformat()
        if isinstance(obj, uuid.UUID):
            return str(obj.hex)
        raise TypeError(repr(obj) + ' is not JSON serializable')


Json = MIME(
    accept_type='application/vnd.json+api',
    content_type='application/vnd.json+api',
    encode=_JSONEncoder().encode,
    source=_JSONSource,
)
