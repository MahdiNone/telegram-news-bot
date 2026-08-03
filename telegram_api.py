import requests
from config import *

def send(text):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
        data={
            "chat_id":CHANNEL_ID,
            "text":text,
            "parse_mode":"HTML"
        }
    )

def send_photo(photo,caption):

    requests.post(
        f"https://api.telegram.org/bot{BOT_TOKEN}/sendPhoto",
        data={
            "chat_id":CHANNEL_ID,
            "photo":photo,
            "caption":caption
        }
    )
