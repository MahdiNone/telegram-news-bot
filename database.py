import json
import hashlib

FILE="sent.json"

def load():
    try:
        with open(FILE,"r") as f:
            return json.load(f)
    except:
        return []

def save(data):
    with open(FILE,"w") as f:
        json.dump(data,f)

def is_sent(url):
    h=hashlib.md5(url.encode()).hexdigest()
    data=load()
    return h in data

def add(url):
    h=hashlib.md5(url.encode()).hexdigest()
    data=load()
    data.append(h)
    save(data)
