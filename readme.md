Alert to Call and SMS
This application allows you to receive alerts from TradingView in the form of both call and SMS. It uses Twilio for sending SMS and making phone calls, Flask for creating a web server and ngrok for exposing the localhost to the internet.

Prerequisites
A Twilio account. You can sign up for a free trial account here.

A TradingView account. You can sign up for a free account here.

ngrok installed on your machine. You can download it here.

Python 3 installed on your machine.

Installation
Clone this repository and navigate to the cloned directory.

```
git clone https://github.com/chang-pro/Trading-Alert-Notification-System.git
cd Trading-Alert-Notification-System

Create a virtual environment

python -m venv venv

Activate the virtual environment

source venv/bin/activate 

Install the requirements

pip install -r requirements.txt
```
Configuration
Replace the placeholder values in the script such as 'your_account_sid', 'your_auth_token', 'your_twilio_number', 'receiver_phone_number' with your actual Twilio account details, Twilio phone number and receiver's phone number.

Run ngrok on your localhost and copy the generated URL.

```
ngrok http 5000
```
Go to your TradingView alert settings and paste the ngrok URL in the webhook URL field and append the endpoint path, for example, if the endpoint path is "/alert", then you should paste https://a1b2c3d4.ngrok.io/alert in the webhook URL field.

Run the script by executing the command

```
python alert.py
```
Whenever the alert is triggered, TradingView will send a POST request to the ngrok URL which will forward the request to your localhost and the script will handle it by sending a SMS and making a phone call with the contents of the alert.
Note: You will need to update the ngrok URL and paste it again in the alert webhook settings in TradingView every time you restart the ngrok

Note: Make sure you are appending the endpoint path in the URL, as it should match the endpoint path that you have in your Flask app.