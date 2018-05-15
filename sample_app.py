from wee import application
from wee import route


@route('/')
def hello(request):
    return 'Hi there'


@route('/help')
def help(request):
    return 'How may I help you?'
