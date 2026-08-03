from google import genai
from config import GEMINI_KEY

client=genai.Client(api_key=GEMINI_KEY)

def rewrite(text):

    prompt=open("prompt.txt",encoding="utf8").read()

    prompt=prompt.replace("{news}",text)

    r=client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return r.text
