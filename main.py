# main.py
# server that listens for HTTP requests from Twilio, processes
#   valid bash commands, and sends responses

from api_credentials import *
from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_reply():
    resp = MessagingResponse()

    resp.message("test2")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
