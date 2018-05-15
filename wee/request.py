class Request:
    def __init__(self):
        pass

    @staticmethod
    def parse(environ):
        return _parse_request(environ)


def _parse_request(environ):
    request = Request()
    request.environ = environ
    request.path = environ['PATH_INFO']
    request.args = {}
    request.headers = {}
    request.method = ''
    request.url = ''
    request.form = {}
    request.data = ''
    request.json = {}
    return request
