from requests import get
from pprint import pprint

api_key = 'c9de1f4c8f81454519f23734d6c5e905'
city_name = 'dhaka'
weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
weather_api_data = get(weather_api_url)
data = weather_api_data.json()
main = data.get('main')
feels_like = main.get('feels_like')
humidity = main.get('humidity')
pressure = main.get('pressure')
temp = main.get('temp')

sentance = f'the current temperature of {city_name} city is now {temp} degree. feels like {feels_like}. humidity is {humidity}. air pressure is {pressure}'
print(sentance)

print('*'*20)
pprint(data)