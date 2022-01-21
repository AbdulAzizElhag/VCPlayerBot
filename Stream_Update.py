import requests
from dotenv import load_dotenv
import os
import time

#globle variables
BOT_TOKEN="1825930059:AAFbb5Q4aIxKqHT3QG9w2KP97Xjk7_S-YXM"
#chat id for Idbot by /getId 
CHAT="-1001578206827"
# api_key="4126f2bb-41c7-4c6b-bda8-c795c9952ce8"
time_interval = 15*60
def send_update(chat_id,msg):
        url= f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT}&text={msg}"
        requests.get(url)

while True:
        send_update(CHAT, f"/stream http://n05.radiojar.com/8s5u5tpdtwzuv?rj-ttl=5&rj-tok=AAABeray1BUAaNFktO4VGQX0CQ")
        time.sleep(time_interval)
