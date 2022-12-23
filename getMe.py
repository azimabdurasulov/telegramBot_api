import requests
TOKEN = '5355192064:AAGJspb34MbW0qTD1P2c0kpDRnu4dlmtyYE'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url=BASE_URL)
print(response.json())