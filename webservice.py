from bottle import route, run, debug, default_app, response, request
from urllib.parse import urlencode
import json
import os

TOKEN=os.getenv('TOKEN', None)
PORT=int(os.getenv('PORT', 8000))

@route('/', method='POST')
def index():
    text = request.forms.get('text')
    token = request.forms.get('token')
    if token and token != TOKEN:
        return ""
    if not text:
        return "You should probably tell me to google something for someone."
    lmgtfy_url = "http://lmgtfy.com/?" + urlencode({'q': text})
    response.content_type = 'application/json'
    return json.dumps({'response_type': 'in_channel', 'text': "Please, <"+ lmgtfy_url +"|allow me!>"})

app = default_app()

debug(False)
run(host='0.0.0.0', port=PORT, reloader=True)
