import inotify.adapters
import json
import os
import requests
import telebot

FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DEVICE_IP = os.getenv('DEVICE_IP')
LOGIN = os.getenv('LOGIN', 'mp4')
PASSWORD = os.getenv('PASSWORD')

notifier = inotify.adapters.InotifyTree(FOLDER)

data = f'\n\t\n\t\"login\":\"{LOGIN}\",\n\t\"password\":\"{PASSWORD}\"\n\t\n'
payload = '{' + data + '}'
payload2 = ("{\n\t\"actions\":[{"
    + "\n\t\t\"action\":\"sec_box\","
    + "\n\t\t\"parameters\":\"id=65793,reason=3\"\n\t\n}]}"
)
headers = {
    'content-type': "application/json"
}

for event in notifier.event_gen():
    if event is not None:
        if 'IN_CLOSE_WRITE' in event[1] and EXTENSION in event[3]:
            url1 = 'http://{}/login.fcgi'.format(DEVICE_IP)
            response = requests.request("POST", url1, data=payload, headers=headers)
            session = json.loads(response.text)['session']
            url2 = "http://{}/execute_actions.fcgi?session={}".format(DEVICE_IP, session)
            response = requests.request("POST", url2, data=payload2, headers=headers)
