import requests
import time
import threading

def send_request():
    url = "https://discord.com/api/v9/channels/762448042011000842/messages"

    auth = {
        'authorization' : 'OTk3MzgyNTcxMzcxNTMyMzUw.GO-7Ef.gssrnKjxmS6vL2ARsqEROte04pbuYzcXQLk6Cg'
    }

    message = '\n'.join(['🟠 Sell FuelPack ⛽  11/1 at ▶️ MAFFF ◀️' for _ in range(3)])
    msg = {
        'content' : message
    }

    requests.post(url, headers = auth, data = msg)

def schedule_send_request():
    threading.Timer(7500, schedule_send_request).start()
    send_request()

schedule_send_request()