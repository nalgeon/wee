from enum import Enum


class StatusCode(Enum):
    OK = '200 OK'
    NOT_FOUND = '404 Not Found'
    SERVER_ERROR = '500 Internal Server Error'


class Header(Enum):
    CONTENT_TYPE = 'Content-Type'


class MimeType(Enum):
    FORM = 'multipart/form-data'
    JSON = 'application/json'
    HTML = 'text/html'
    PLAIN = 'text/plain'
