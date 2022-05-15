import requests as req
import schedule
from time import sleep
from datetime import datetime
from websocket import create_connection

def slash_send(self, token, channel_id, application_id, guild_id, version_id, command_id, command, delay):

    def sendMessage(token, channel_id, application_id, guild_id, version_id, command_id, command):
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

        headers = {'authorization': token, 'Content-Type': 'application/json'}
        payload = {
                "type": 2,
                "application_id": str(application_id),
                "guild_id": str(guild_id),
                "channel_id": str(channel_id),
                "session_id": '1',
                "data": {
                    "version": str(version_id),
                    "id": str(command_id),
                    "name": str(command),
                    "type": 1
                }
            }
        response = req.post("https://discord.com/api/v9/interactions", headers=headers, json=payload)
        print(response.text)
        if response.status_code == 400:
            payload = {
                "type": 2,
                "application_id": str(application_id),
                "guild_id": str(guild_id),
                "channel_id": str(channel_id),
                "session_id": '1',
                "data": {
                    "version": str(version_id),
                    "id": str(command_id),
                    "guild_id": str(guild_id),
                    "name": str(command),
                    "type": 1
                }
            }
            response = req.post("https://discord.com/api/v9/interactions", headers=headers, json=payload)
            print(response.text)

        try:
            ws.close()
        except:
            pass
        current_datetime = datetime.now()
        self.logsbeep.emit(f"{current_datetime}  |   MSG sended to {channel_id}")


    def time():
        sendMessage(token, channel_id, application_id, guild_id, version_id, command_id, command)

    tokens = token.split()
    for token in tokens:    
        sendMessage(token, channel_id, application_id, guild_id, version_id, command_id, command)
        schedule.every(int(delay)).seconds.do(time)

    while True:
        schedule.run_pending()
        sleep(1)