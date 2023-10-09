import websocket
import math
import os
import json
#operation on a received message to write to a file
def on_message(ws, msg):
    print(msg)
    resp = json.loads(msg)
    value = (resp["id"]) 
    folder = math.floor(value/100)# the number of messages we write in one folder. if (value/100) then 100 pieces each
    os.system("mkdir /home/jupyter/data/"+str(folder))
    datafile = open("/home/jupyter/data/"+str(folder)+"/"+str(value)+".json", 'w')
    datafile.write(msg)
    datafile.close
    #record the recorded message in the log
    logfile = open("/home/jupyter/logs/readlog.txt", 'a')
    logfile.write(str(value)+"\n")
    logfile.close
if __name__ == "__main__":
    ws = websocket.WebSocketApp("wss://test-ws.skns.dev/raw-messages", on_message=on_message)
    ws.run_forever()
