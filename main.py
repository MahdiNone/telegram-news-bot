from config import *
from rss import *
from database import *
from gemini_api import *
from telegram_api import *

for feed in RSS_FEEDS:

    news=get_news(feed)

    for n in news:

        if is_sent(n["link"]):
            continue

        text=n["title"]+"\n\n"+n["summary"]

        final=rewrite(text)

        if n["image"]:

            send_photo(n["image"],final)

        else:

            send(final)

        add(n["link"])

        break
