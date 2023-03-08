import requests

api_find_url = 'https://api.ipify.org?format=json'
req = requests.get(api_find_url)
if req.status_code == 200:
   data = req.json()
   ip = data.get('ip')

ip_locaiton_url = f'https://ipapi.co/{ip}/json/'
ip_api = requests.get(ip_locaiton_url)
data = ip_api.json()
user_ip = data.get('ip')
user_city = data.get('city')
user_region = data.get('region')
user_country = data.get('country_name')
user_currency = data.get('currency')
user_population = data.get('country_population')
sentance = f'{user_ip} is is located at {user_city} in {user_country} in {user_region}. valided currency is {user_currency} and population is {user_population}'

if ip_api.status_code == 200:
   print(sentance)
   


