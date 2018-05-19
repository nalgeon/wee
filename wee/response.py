from .http import MimeType, StatusCode


class Response:
    def __init__(self, body, status_code=StatusCode.OK.value,
                 content_type=MimeType.HTML.value):
        self.body = body
        self.status_code = status_code
        self.content_type = content_type


def respond(body, status_code=StatusCode.OK.value,
            content_type=MimeType.HTML.value):
    return Response(body, status_code, content_type)
