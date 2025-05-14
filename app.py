from flask import Flask, request
from sms_alert import send_sms
import requests

app = Flask(__name__)

@app.route('/beacon', methods=['GET'])
def beacon():
    decoy_id = request.args.get('id', 'unknown')
    ip = request.remote_addr

    # Get location from IP
    try:
        response = requests.get(f'https://ipinfo.io/{ip}/json')
        location_data = response.json()
        city = location_data.get('city', 'Unknown')
        region = location_data.get('region', 'Unknown')
        country = location_data.get('country', 'Unknown')
        location = f"{city}, {region}, {country}"
    except:
        location = "Location unknown"

    print(f"[{decoy_id}] Alert from IP: {ip}, Location: {location}")
    
    # Send SMS
    send_sms(f"📢 Decoy triggered!\nID: {decoy_id}\nIP: {ip}\nLocation: {location}")
    
    return "Decoy accessed", 200

if __name__ == '__main__':
    app.run(port=5000)

