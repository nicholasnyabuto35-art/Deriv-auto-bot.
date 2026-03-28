
import time
import requests
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

def send_telegram(msg):
    if TOKEN and CHAT_ID:
        url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"
        requests.post(url, data={"chat_id": CHAT_ID, "text": msg})

def strategy():
    import random
    return random.choice(["BUY", "SELL"])

while True:
    signal = strategy()
    print("Signal:", signal)

    send_telegram(f"📊 Signal: {signal}")

    time.sleep(60)
