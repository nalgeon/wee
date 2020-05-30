import wee
from wee import application


@wee.route('/')
def index(request):
    body = """
<h1>Sample Wee application</h1>
<ul>
  <li>
    <code>/<a href="/hello">hello</a>?name={your_name}</code>
      — prints welcome message
  </li>
  <li>
    <code>/<a href="/request">request</a></code>
      — prints request object
  </li>
</ul>
"""
    return wee.respond(_render_html(body))


@wee.route('/hello')
def hello(request):
    name = request.args.get('name')
    body = f'Hello, {name}!' if name else f'Hello, my anonymous friend!'
    return wee.respond(_render_html(body))


@wee.route('/request')
def help(request):
    import pprint
    body = '<pre>{}</pre>'.format(pprint.pformat(request.__dict__))
    return wee.respond(_render_html(body))


def _render_html(body):
    template = """
<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    {}
  </body>
</html>
"""
    return template.format(body)
