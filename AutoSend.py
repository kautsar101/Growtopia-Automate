import requests
import time
import threading

def send_request():
    url = "https://discord.com/api/v9/channels/762448042011000842/messages"

    auth = {
        'authorization' : 'NjE2NTY2OTAwNDkwNTAyMTU0.Gvs1T5.POGsn3Ms_sck03gBhsvz88Umy7X-xh7eSSWd34'
    }

    message = "\n".join(["🟠 Sell FuelPack ⛽  15/1 at ▶️ EXLOD ◀️" for _ in range (3)])
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