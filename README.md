# Wee

Toy WSGI-compatible web framework.

Features:

- Basic routing (no pattern matching)
- Request parsing (headers, form data, json etc)

# Usage

Write your app:

```python
from wee import application, respond, route

@route('/hi')
def index(request):
    return respond('Hi there!')

```

Then run it with WSGI server of your choice:

```
uwsgi --http :9090 --wsgi-file your_app.py
```

For more examples see sample_app.py.
