#!/usr/bin/env python2.7

import os
import sys
from flask import Flask, request, Response
from werkzeug.utils import secure_filename
import json
from chatbot import ask

json_encode = json.JSONEncoder().encode
app = Flask(__name__)

@app.route('/', methods=['POST'])
def chat():
    data = request.get_json()
    botname = data['botname']
    question = data['question']
    session = data['session']
    answer, ret, botname = ask(botname, question, session)
    return Response(json_encode(
        {'ret': ret, 'answer': answer, 'botname': botname}),
        mimetype="application/json")

if __name__ == '__main__':
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    else:
        port = 8001
    app.run(host='0.0.0.0', debug=False, use_reloader=False, port=port)
