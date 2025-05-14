from twilio.rest import Client

# Replace with your real Twilio credentials
TWILIO_ACCOUNT_SID = 'AC182d25ac5a8b45715c12b8b6359e3ded'
TWILIO_AUTH_TOKEN = '60b2477eb5a9b729ee3a98a65349e802'
TWILIO_FROM = '+12313594744'  # Your Twilio number
TWILIO_TO = '+919819329155'  # Your personal phone number

def send_sms(message):
    try:
        client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
        client.messages.create(
            body=message,
            from_=TWILIO_FROM,
            to=TWILIO_TO
        )
        print("✅ SMS sent successfully.")
    except Exception as e:
        print("❌ Failed to send SMS:", e)
