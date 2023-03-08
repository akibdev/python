from httpx import get
from pprint import pprint
#
# api_key = 'c9de1f4c8f81454519f23734d6c5e905'
# city_name = 'dhaka'
# weather_api_url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'
# weather_api_data = get(weather_api_url)
# data = weather_api_data.json()
# pprint(data)

url_list = {
    'https://www.digitaltrends.com/computing/best-wireless-mice/',
    'https://www.nytimes.com/wirecutter/reviews/best-wireless-mouse/',
    'https://simplicityhunter.com/minimalist-mouse/',
    'https://www.techradar.com/news/best-small-mouse',
    'https://www.tomshardware.com/best-picks/best-wireless-mouse',
    'https://www.rtings.com/mouse/reviews/best/work',
    'https://www.pcmag.com/picks/the-best-computer-mice',
    'https://www.eurogamer.net/digitalfoundry-best-ultra-light-mouse-for-fps-csgo-valorant'
}
for url in url_list:
    r = get(url)
    print(url, r.status_code, sep='------')