from google import genai
from config import GEMINI_KEY

print("KEY =", GEMINI_KEY)
print("TYPE =", type(GEMINI_KEY))

client = genai.Client(api_key=GEMINI_KEY)

PROMPT = open("prompt.txt", encoding="utf8").read()

def rewrite(news):
    prompt = PROMPT.replace("{news}", news)

    r = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return r.text
