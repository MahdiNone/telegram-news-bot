from config import *
from rss import *
from database import *
from telegram_api import *
from gemini_api import *
from logger import *

count=0

for feed in RSS_FEEDS:

    log(feed)

    news=get_news(feed)

    for item in news:

        if count>=MAX_POSTS:

            quit()

        if is_sent(item["link"]):

            continue

        source=item["text"]

        if len(source)<200:

            source=item["summary"]

        if len(source)<50:

            source=item["title"]

        try:

            final=rewrite(source)

        except Exception as e:

            log(e)

            continue

        try:

            if item["image"]:

                send_photo(

                    item["image"],

                    final

                )

            else:

                send(final)

        except Exception as e:

            log(e)

            continue

        add(item["link"])

        count+=1

        log("sent")
