import feedparser

def get_news(url):

    feed=feedparser.parse(url)

    news=[]

    for item in feed.entries:

        image=""

        if "media_content" in item:
            image=item.media_content[0]["url"]

        news.append({
            "title":item.title,
            "link":item.link,
            "summary":item.get("summary",""),
            "image":image
        })

    return news
