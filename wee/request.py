import json
import urllib.parse
from .http import MimeType


class Request:
    def __init__(self):
        pass

    @staticmethod
    def parse(environ):
        return _parse_request(environ)


def _parse_request(environ):
    request = Request()
    request.environ = environ
    request.method = environ['REQUEST_METHOD']
    request.scheme = environ['wsgi.url_scheme']
    request.host, request.port = environ['HTTP_HOST'].split(':')
    request.path = environ['PATH_INFO']
    request.content_type = environ.get('CONTENT_TYPE')
    request.headers = _parse_headers(environ)
    request.args = _parse_query_string(environ['QUERY_STRING'])
    content_length = int(environ.get('CONTENT_LENGTH', '0'))
    request.data = environ['wsgi.input'].read(content_length)
    request.form = _parse_form(request.content_type, request.data)
    request.json = _parse_json(request.content_type, request.data)
    return request


def _parse_headers(environ):
    headers = {}
    for key in environ.keys():
        if not key.startswith('HTTP_'):
            continue
        header_name = _extract_header_name(key)
        headers[header_name] = environ[key]
    return headers


def _parse_form(content_type, data):
    if content_type != MimeType.FORM.value:
        return {}
    try:
        return _parse_query_string(data)
    except ValueError:
        return {}


def _parse_json(content_type, data):
    if content_type != MimeType.JSON.value:
        return None
    try:
        return json.loads(data)
    except ValueError:
        return None


def _parse_query_string(qs):
    parsed = urllib.parse.parse_qs(qs)
    for key in parsed.keys():
        value = parsed[key]
        if isinstance(value, list) and len(value) == 1:
            parsed[key] = value[0]
    return parsed


def _extract_header_name(environ_key):
    name_parts = environ_key.split('_')[1:]
    name_parts = [part.capitalize() for part in name_parts]
    return '-'.join(name_parts)