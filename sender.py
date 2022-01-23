import requests as req
import schedule
from time import sleep, time
from datetime import datetime
from websocket import create_connection
import json

def send(self, token, channel_id, message, delay, image):

    def sendMessage(token, channelid, message, image):
        ws = create_connection("wss://gateway.discord.gg/")
        data = '''
        {
            "op": 2,
            "d":{
                "token": "%s",
                "properties": {
                    "$os": "linux",
                    "$browser": "ubuntu",
                    "$device": "ubuntu"
                },
            }
        }
        ''' % token
        ws.send(data)
        if image != '':
            headers = {'authorization': token}
            files = {'files[0]': open(image, 'rb')}
            files['payload_json'] = (None, json.dumps({'content': message}))
            req.post("https://discordapp.com/api/v9/channels/%s/messages" % channelid, headers = headers, files=files)
        else:
            headers = {'authorization': token, 'Content-Type': 'application/json'}
            payload = {"content":message,"tts":False}
            req.post("https://discordapp.com/api/v9/channels/%s/messages" % channelid, headers = headers, json=payload)
        try:
            ws.close()
        except:
            pass
        current_datetime = datetime.now()
        self.logsbeep.emit(f"{current_datetime}  |   MSG sended to {channel_id}")


    def time():
        sendMessage(token, channel_id, message, image)

    schedule.every(int(delay)).minutes.do(time)

    while True:
        schedule.run_pending()
        sleep(1)