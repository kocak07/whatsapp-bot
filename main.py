from fastapi import FastAPI, Request
import requests
import os
from openai import OpenAI

app = FastAPI()

# ENV değişkenleri
VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
ACCESS_TOKEN = os.getenv("ACCESS_TOKEN")
PHONE_NUMBER_ID = os.getenv("PHONE_NUMBER_ID")

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ✅ ANA SAYFA (Render için gerekli)
@app.get("/")
def home():
    return {"status": "bot çalışıyor"}

# ✅ Webhook doğrulama
@app.get("/webhook")
def verify(mode: str = "", challenge: str = "", verify_token: str = ""):
    if verify_token == VERIFY_TOKEN:
        return int(challenge)
    return "Hata"

# ✅ Mesaj yakalama
@app.post("/webhook")
async def receive_message(req: Request):
    data = await req.json()

    try:
        message = data["entry"][0]["changes"][0]["value"]["messages"][0]["text"]["body"]
        from_number = data["entry"][0]["changes"][0]["value"]["messages"][0]["from"]

        # Şimdilik sabit cevap (AI sonra ekleyeceğiz)
        cevap = "Merhaba 👋 Ulu Resort Hotel'e hoş geldiniz. Size nasıl yardımcı olabilirim?"

        send_message(from_number, cevap)

    except Exception as e:
        print("Hata:", e)

    return {"status": "ok"}

# ✅ WhatsApp mesaj gönderme
def send_message(to, text):
    if not ACCESS_TOKEN or not PHONE_NUMBER_ID:
        print("Token veya Phone ID eksik")
        return

    url = f"https://graph.facebook.com/v18.0/{PHONE_NUMBER_ID}/messages"

    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": to,
        "type": "text",
        "text": {"body": text}
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)
