import requests
import time
import threading

def send_request():
    world = {}
    url = "https://discord.com/api/v9/channels/762448042011000842/messages"
    auth_link = ""
    auth = {
        'authorization' : auth_link
    }

    message = "\n".join([f"🟠 Sell FuelPack ⛽  15/1 at ▶️ {world} ◀️" for _ in range (3)])
    msg = {
        'content' : message
    }

    requests.post(url, headers = auth, data = msg)

def schedule_send_request():
    threading.Timer(7500, schedule_send_request).start()
    send_request()
    print("sended")

schedule_send_request()
print("done")