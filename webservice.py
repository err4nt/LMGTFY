from bottle import route, run, debug, default_app, response, BaseRequest, request
from requests import post
from urllib.parse import urlencode
import json

TOKEN=""

@route('/', method='POST')
def index():
    channel = request.forms.get('channel')
    text = request.forms.get('text')
    token = request.forms.get('token')
    response_url = request.forms.get('response_url')
    if not text:
        pass
    lmgtfy_url = "http://lmgtfy.com/?" + urlencode({'q': text})
    response.content_type = 'application/json'
    return json.dumps({'response_type': 'in_channel', 'text': "Please, <"+ lmgtfy_url +"|allow me!>"})

app = default_app()

debug(True)
run(host='0.0.0.0', port=8000, reloader=True)
