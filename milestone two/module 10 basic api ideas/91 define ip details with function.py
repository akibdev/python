import requests

def res_data(url):
   res = requests.get(url)
   if res.status_code == 200:
      data = res.json()
   return data

ip_find_url = 'https://api.ipify.org?format=json'
ip_data = res_data(ip_find_url)
ip = ip_data.get('ip')


user_locaiton_url = f'https://ipapi.co/{ip}/json/'
user_data = res_data(user_locaiton_url)

user_city = user_data.get('city')
user_region = user_data.get('region')
user_country = user_data.get('country_name')
print(f'{user_city} {user_country} {user_region}')
