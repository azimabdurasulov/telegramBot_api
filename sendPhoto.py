import os 
import requests

TOKEN = os.environ['TOKEN']

def sendPhoto(chat_id:str,photo:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendPhoto'
    param = {
        'chat_id':chat_id,
        'photo':photo
    }
    r = requests.get(url=URL,params=param)
    pass


chat_id ='5575549228'

photo_url='https://random.dog/2bff25d0-c721-4078-8cc9-f3ce6b464428.jpg'

sendPhoto(chat_id=chat_id,photo=photo_url)