import os
import requests

TOKEN = os.environ['TOKEN']

def sendMessage(chat_id:str,text:str):
    URL = f'https://api.telegram.org/bot{TOKEN}/sendMessage'
    button1 = {
        'text':'11'
    }
    button2 = {
        'text':'21'
    }
    button3 = {
        'text':'HOME'
    }
    keyboard =  [[button1, button2], [button3]]
    reply_markup = {
        'keyboard':keyboard
    }

    payload = {
        'chat_id':chat_id,
        'text':'Salom',
        'reply_markup':reply_markup
    }
    r = requests.get(url=URL,json=payload)
    
chat_id ='5075065217'

sendMessage(chat_id=chat_id,text='Salom')

