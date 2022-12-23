import requests
TOKEN = '5355192064:AAEbylzYMrRsWJCqufKA6H2leOWhH3kIcdg'
BASE_URL = f'https://api.telegram.org/bot{TOKEN}/getMe'

response = requests.get(url=BASE_URL)
user=response.json()['result']
 
print(user['first_name'])