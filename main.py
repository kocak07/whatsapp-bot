from fastapi import FastAPI, Request
import requests
import os
from openai import OpenAI

app = FastAPI()

VERIFY_TOKEN = os.getenv(VERIFY_TOKEN)
ACCESS_TOKEN = os.getenv(ACCESS_TOKEN)
PHONE_NUMBER_ID = os.getenv(PHONE_NUMBER_ID)

client = OpenAI(api_key=os.getenv(OPENAI_API_KEY))

@app.get(webhook)
def verify(mode str = , challenge str = , verify_token str = )
    if verify_token == VERIFY_TOKEN
        return int(challenge)
    return Hata

@app.post(webhook)
async def receive_message(req Request)
    data = await req.json()

    try
        message = data[entry][0][changes][0][value][messages][0][text][body]
        from_number = data[entry][0][changes][0][value][messages][0][from]

        cevap = ai_cevap(message)
        send_message(from_number, cevap)

    except Exception as e
        print(Hata, e)

    return {status ok}

def ai_cevap(message)
    response = client.chat.completions.create(
        model=gpt-5-mini,
        messages=[
            {role system, content Sen Ulu Resort Hotel müşteri temsilcisisin. Kısa ve net Türkçe cevap ver.},
            {role user, content message}
        ]
    )
    return response.choices[0].message.content

def send_message(to, text)
    url = fhttpsgraph.facebook.comv18.0{PHONE_NUMBER_ID}messages

    headers = {
        Authorization fBearer {ACCESS_TOKEN},
        Content-Type applicationjson
    }

    data = {
        messaging_product whatsapp,
        to to,
        type text,
        text {body text}
    }

    requests.post(url, headers=headers, json=data)