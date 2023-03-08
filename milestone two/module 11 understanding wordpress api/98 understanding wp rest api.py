from httpx import get
from pprint import pprint

domain_url = 'https://gearsvine.com/wp-json/wp/v2'
post_url = f'{domain_url}/posts'
r = get(post_url)
post_api = r.json()
for post_data in post_api:
    post_link = post_data.get('link')
    post_title = post_data.get('title').get('rendered')
    post_date = post_data.get('date')
    print(post_link)