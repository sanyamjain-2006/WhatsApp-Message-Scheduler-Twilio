from twilio.rest import Client
from datetime import datetime
import time

# Your Twilio credentials
account_sid = ""# Twilio Sid Number
token = ""# Twilio Token No

client = Client(account_sid, token)

def send_message(recipient_no, message_):
    try:
        message = client.messages.create(
            from_='whatsapp:+',  # Twilio Sandbox WhatsApp number
            body=message_,
            to=f'whatsapp:{recipient_no}'
        )
        print(f'Message sent successfully to {recipient_no}')
    except Exception as e:
        print(f'An error occurred: {e}')

# User inputs
name = input("Enter Your Name: ")
recipient_no = input("Enter Your Number with country code (e.g. +91XXXXXXXXXX): ")
message_ = input("Enter your message: ")
date_str = input("Enter the date to send the message (YYYY-MM-DD): ")
time_str = input("Enter the time to send the message (HH:MM in 24hr format): ")

# Convert input to datetime
schedule_datetime = datetime.strptime(f"{date_str} {time_str}", "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

# Calculate delay
difference = schedule_datetime - current_datetime
delay_seconds = difference.total_seconds()

if delay_seconds <= 0:
    print("The specified time has already passed. Cannot schedule the message.")
else:
    print(f"The message is scheduled for {schedule_datetime}")
    time.sleep(delay_seconds)
    send_message(recipient_no, message_)
