import requests
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse
from flask import Flask, request

# Twilio API credentials
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

# Flask server
app = Flask(__name__)

# Send SMS message
def send_sms(to_number, message):
    message = client.messages.create(
        body=message,
        from_='your_twilio_number',
        to=to_number
    )

# Send phone call
def make_call(to_number, message):
    resp = VoiceResponse()
    resp.say(message)
    client.calls.create(
        twiml=resp,
        to=to_number,
        from_='your_twilio_number'
    )

# Webhook endpoint
@app.route("/alert", methods=["POST"])
def handle_alert():
    json_data = request.get_json()
    if json_data['status'] == 'triggered':
        message = f"alert triggered: {json_data['condition']} on {json_data['symbol']} at {json_data['price']} "
        send_sms('receiver_phone_number', message)
        make_call('receiver_phone_number', message)
    return "OK"

if __name__ == "__main__":
    app.run()
