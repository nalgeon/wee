import traceback
from .http import Header, MimeType, StatusCode
from .request import Request

_routes = {}


def route(path):
    def decorator(func):
        _routes[path] = func
        return func
    return decorator


def application(environ, start_response):
    try:
        request = Request.parse(environ)
        if request.path not in _routes:
            return _handle_error(start_response,
                                 StatusCode.NOT_FOUND.value)
        return _handle_route(request, start_response)
    except Exception as exc:
        traceback.print_exc()
        return _handle_error(start_response,
                             StatusCode.SERVER_ERROR.value, str(exc))


def _handle_route(request, start_response):
    response = _routes[request.path](request)
    headers = [(Header.CONTENT_TYPE.value, response.content_type)]
    start_response(response.status_code, headers)
    return [_to_bytestr(response.body)]


def _handle_error(start_response, status_code, message=''):
    headers = [(Header.CONTENT_TYPE.value, MimeType.PLAIN.value)]
    start_response(status_code, headers)
    return [_to_bytestr(message)]


def _to_bytestr(string):
    return string.encode('utf-8')
