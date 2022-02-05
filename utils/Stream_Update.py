import requests
from dotenv import load_dotenv
import os
import time

#globle variables
load_dotenv()
CHAT_ID = os.getenv("CHAT_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
time_interval = 15*60

def send_update(chat_id,msg):
        url= f"https://api.telegram.org/bot{BOT_TOKEN=}/sendMessage?chat_id={CHAT_ID}&text={msg}"
        requests.get(url)

while True:
        send_update(CHAT_ID, f"/stream http://n05.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABeray1BUAaNFktO4VGQX0CQ")
        time.sleep(time_interval)
