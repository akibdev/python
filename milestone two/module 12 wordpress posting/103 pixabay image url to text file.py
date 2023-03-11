from httpx import get
from pprint import pprint

api_key = '34226848-b4a8967f9683376be694834ca'
quary = 'yellow+flowers'
api_url = f'https://pixabay.com/api/?key={api_key}&q={quary}'

r = get(api_url)
api_data = r.json().get('hits')
for image in api_data:
    img = image.get('webformatURL')
    # image_file = open('imageUrlList.txt', 'a+')
    # image_file.writelines(img+'\n')
    # image_file.close()
    print(img)
