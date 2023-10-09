import websocket
import json
import time
import math
  

def on_message(ws, message):
    try:
        logfile = open("/home/jupyter/logs/writelog.txt", 'r')
        lines = list(logfile)
        value = lines[-1]
        logfile.close()
    except:
        logfile = open("/home/jupyter/logs/readlog.txt", 'r')
        lines = list(logfile)
        value = lines[0]
        logfile.close()
    while value!=0:
        folder = math.floor(value/100)
        attempts = 0
        success = False
        while attempts < 5 and not success:
            try:
                datafile = open("/home/jupyter/data/"+str(folder)+"/"+str(value)+".json")
                data = json.load(datafile)
                ws.send(data)
                datafile.close()
                logfile = open("/home/jupyter/logs/writelog.txt", 'a')
                logfile.write(str(value)+"\n")
                logfile.close
                success = true
            except:
                time.sleep(5)
                attempts += 1
                if attempts == 12: 
                    data=json.dumps({"id": int(value), "text": "message not sended from server for 1 minute"})
                    ws.send(data)
                    logfile = open("/home/jupyter/logs/errorlog.txt", 'a')
                    logfile.write(str(value)+"\n")
                    logfile.close
                    success = true
        value = value+1

wsapp = websocket.WebSocketApp("wss://test-ws.skns.dev/ordered-messages/babakhanov",on_message=on_message)
wsapp.run_forever() 