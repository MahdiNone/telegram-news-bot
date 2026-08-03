import requests
from config import BOT_TOKEN, CHANNEL_ID

API_URL = f"https://api.telegram.org/bot{BOT_TOKEN}"

def send(text):
    requests.post(
        f"{API_URL}/sendMessage",
        data={
            "chat_id": CHANNEL_ID,
            "text": text[:4000],
            "parse_mode": "HTML",
            "disable_web_page_preview": False
        },
        timeout=20
    )

def send_photo(photo, caption):
    requests.post(
        f"{API_URL}/sendPhoto",
        data={
            "chat_id": CHANNEL_ID,
            "photo": photo,
            "caption": caption[:1024],
            "parse_mode": "HTML"
        },
        timeout=20
    )
