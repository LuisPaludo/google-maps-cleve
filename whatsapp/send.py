from decouple import config
import requests

def envio_whatsapp():
    url = "https://graph.facebook.com/v21.0/470929182781074/messages"

    headers = {
        "Authorization": f"Bearer {config('WHATSAPP_API_KEY')}",
        "Content-Type": "application/json"
    }

    data = {
        "messaging_product": "whatsapp",
        "to": "5546999099928",
        "type": "text",
        "text": {
            "body": "hello_world"
        }
    }

    response = requests.post(url, headers=headers, json=data)

    if response.status_code == 200:
        print("Mensagem enviada com sucesso!")
        print(response.json())
    else:
        print(f"Erro ao enviar mensagem: {response.status_code}")
        print(response.text)