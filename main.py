import os
import requests

token = os.environ["BOT_TOKEN"]
channel = os.environ["CHANNEL_ID"]

url = f"https://api.telegram.org/bot{token}/sendMessage"

requests.post(url, data={
    "chat_id": channel,
    "text": "✅ سلام! ربات با موفقیت از GitHub Actions اجرا شد."
})
