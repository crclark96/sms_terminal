# main.py
# server that listens for HTTP requests from Twilio, processes
#   valid bash commands, and sends responses

import subprocess
from api_credentials import *
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    command = request.form['Body'].split(' ')

    try:
        message = subprocess.check_output(command)
    except Exception, e:
        message = 'invalid command'

    resp.message(message)

    return str(resp)

@app.route("/")
def hello():
    return "Hello World"

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
