import requests
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from flask import Flask, request
import json

# Twilio API credentials
account_sid = 'replace with your account sid'
auth_token = 'replace with your auth token'
client = Client(account_sid, auth_token)

# Flask server
app = Flask(__name__)
to_number = 'replace with your number'

# Send SMS message
def send_sms(to_number, message):
    message = client.messages.create(
        body=message,
        from_='replace with your twilio number',
        to=to_number
    )

def make_call(to_number, message):
    resp = VoiceResponse()
    resp.pause(length=2)
    resp.say(message, voice='alice', language='en-GB', slow=True)
    client.calls.create(
        twiml=resp,
        to=to_number,
        from_='replace with your twilio number'
    )


# Webhook endpoint
@app.route("/alert", methods=["POST"])
def handle_alert():
    message_data = request.data.decode().split(" ")
    json_data = {"status": "triggered", "condition": message_data[1], "symbol": message_data[0], "price": message_data[2]}

    if json_data['status'] == 'triggered':
        message = f"alert triggered: {json_data['condition']} on {json_data['symbol']} at {json_data['price']}"
        send_sms(to_number, message)
        make_call(to_number, message)
    return "OK"


if __name__ == "__main__":
    app.run()



