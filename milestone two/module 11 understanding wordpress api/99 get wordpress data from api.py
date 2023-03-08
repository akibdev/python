from httpx import get

i = 1
while i < 1000:
    page_url = f'/pages?page={i}'
    base_url = f'https://www.bitcatcha.com/wp-json/wp/v2{page_url}'
    page_r = get(base_url)
    page_api_data = page_r.json()
    for page_data in page_api_data:
        try:
            page_link = page_data.get('link')
            print(page_link)
        except:
            print('end')
    i += 1