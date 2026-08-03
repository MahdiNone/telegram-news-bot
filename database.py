import hashlib
import json

FILE="sent.json"

def load():

    try:

        with open(FILE,"r",encoding="utf8") as f:

            return json.load(f)

    except:

        return []

def save(data):

    with open(FILE,"w",encoding="utf8") as f:

        json.dump(data,f,ensure_ascii=False)

def md5(text):

    return hashlib.md5(
        text.encode()
    ).hexdigest()

def is_sent(link):

    data=load()

    return md5(link) in data

def add(link):

    data=load()

    data.append(md5(link))

    save(data)
