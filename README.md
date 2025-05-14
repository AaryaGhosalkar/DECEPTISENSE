📌 Project Name: DeceptiSense – Decoy Document Alert System
🧩 Objective:
To create a decoy document that looks legitimate but sends a stealth alert (SMS) when opened or clicked, helping detect unauthorized access or data theft.

🔧 Core Components:
app.py – Flask server that listens for requests when a link in the decoy is clicked. It logs the access and triggers the alert.

decoy_generator.py – Python script that creates a .docx decoy file containing:

Fake confidential content

A clickable hyperlink pointing to the Flask server

sms_alert.py – Sends an SMS alert via Twilio when the decoy is triggered.

📤 Alert Mechanism Flow:
You run the project once to generate the decoy and start the Flask server.

When someone opens the .docx and clicks the hidden hyperlink:

A GET request is sent to your Flask server.

The server logs IP and time.

The sms_alert.py is triggered to send an SMS to your phone.

📶 Enhancements Made:
Made the link in the Word document clickable and hidden under "Click here" text.

Ensured SMS alerts are sent via Twilio (with error logging).

Ensured the Flask server runs silently in the background (via .vbs or task scheduler).

Attempted to send device location, though this requires an external IP (not always available locally).

🔍 Troubleshooting Done:
Ensured the server listens on 0.0.0.0 (or used Ngrok for public access).

Verified Twilio credentials and checked for authentication issues.

Tested the /beacon endpoint manually for response.

Handled Python exceptions and logging to get better debugging info.

Added backup methods to test SMS independently.

🚀 Final Outcome:
Your decoy document works with a clickable alert link.

When the link is clicked:

Flask logs the access

SMS is sent to your phone

Flask runs in the background automatically even if you restart the system.
