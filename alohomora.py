import inotify.adapters
import os
import requests

FOLDER = os.getenv('FOLDER', '/tmp/')
EXTENSION = os.getenv('EXTENSION', 'mp4')
DEVICE_IP = os.getenv('DEVICE_IP')
LOGIN = os.getenv('LOGIN', 'admin')
PASSWORD = os.getenv('PASSWORD')

notifier = inotify.adapters.InotifyTree(FOLDER)

login_payload = {
    'login': LOGIN,
    'password': PASSWORD,
}
sec_box_payload = {
    'actions': [{
        'action': 'sec_box',
        'parameters': 'id=65793,reason=3',
    }]
}

for event in notifier.event_gen():
    if not event:
        continue
        
    if 'IN_CREATE' in event[1] and EXTENSION in event[3]:
        login_url = f'http://{DEVICE_IP}/login.fcgi'
        response = requests.post(login_url, json=login_payload)
        session = response.json()['session']
        
        actions_url = f'http://{DEVICE_IP}/execute_actions.fcgi?session={session}'
        response = requests.post(actions_url, json=sec_box_payload)
