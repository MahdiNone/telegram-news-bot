import feedparser
import requests
from bs4 import BeautifulSoup

from config import HEADERS

def extract_image(soup):

    og=soup.find("meta",property="og:image")

    if og:

        return og.get("content","")

    tw=soup.find("meta",attrs={"name":"twitter:image"})

    if tw:

        return tw.get("content","")

    img=soup.find("img")

    if img:

        return img.get("src","")

    return ""

def extract_text(soup):

    paragraphs=[]

    for p in soup.find_all("p"):

        text=p.get_text(" ",strip=True)

        if len(text)>40:

            paragraphs.append(text)

    return "\n".join(paragraphs[:20])

def fetch_article(url):

    try:

        html=requests.get(
            url,
            headers=HEADERS,
            timeout=20
        ).text

        soup=BeautifulSoup(html,"lxml")

        return {

            "text":extract_text(soup),

            "image":extract_image(soup)

        }

    except:

        return {

            "text":"",

            "image":""

        }

def get_news(feed_url):

    feed=feedparser.parse(feed_url)

    items=[]

    for item in feed.entries:

        article=fetch_article(item.link)

        items.append({

            "title":item.title,

            "link":item.link,

            "summary":item.get("summary",""),

            "text":article["text"],

            "image":article["image"]

        })

    return items
