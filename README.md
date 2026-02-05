This is a simple WhatsApp Message Scheduler built with Python and Twilio.
It allows you to schedule a WhatsApp message that will be sent automatically at your chosen date and time.

⚙️ Setup Instructions

Clone this repository:

git clone https://github.com/your-username/whatsapp-scheduler.git
cd whatsapp-scheduler


Install dependencies:

pip install -r requirements.txt


Create a .env file in the project root and add your Twilio credentials:

TWILIO_SID=your_account_sid
TWILIO_AUTH_TOKEN=your_auth_token


⚠️ Replace your_account_sid and your_auth_token with your actual Twilio SID and Token.
(Make sure .env is in .gitignore so it doesn’t get uploaded to GitHub!)

Run the script:

python main.py

📌 Notes

This project uses Twilio’s WhatsApp Sandbox. You must join the sandbox from your Twilio dashboard before sending messages.

Only numbers joined in the sandbox can receive messages during testing.
