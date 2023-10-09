import websocket
import math
import os
import json

def on_message(ws, msg):
    print(msg)
    resp = json.loads(msg)
    value = (resp["id"]) 
    folder = math.floor(value/100)
    os.system("mkdir /home/jupyter/data/"+str(folder))
    with open("/home/jupyter/data/"+str(folder)+"/"+str(value)+".json", 'w') as datafile:
        datafile.write(msg)
        datafile.close
    with open("/home/jupyter/logs/readlog.txt", 'a') as logfile:
        logfile.write(str(value)+"\n")
        logfile.close
if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://test-ws.skns.dev/raw-messages", on_message=on_message)
    ws.run_forever()