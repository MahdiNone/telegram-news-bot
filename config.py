import os
from feeds import RSS_FEEDS

BOT_TOKEN=os.getenv("BOT_TOKEN")
CHANNEL_ID=os.getenv("CHANNEL_ID")
GEMINI_KEY=os.getenv("GEMINI_KEY")

MAX_POSTS=8
REQUEST_TIMEOUT=20

HEADERS={
"User-Agent":"Mozilla/5.0"
}
