from requests import get
item = input('which item you want: ')
color = input('color of that item: ')
api_key = '34226848-b4a8967f9683376be694834ca'
quary = f'{color}+{item}'
api_url = f'https://pixabay.com/api/?key={api_key}&q={quary}'

url_r = get(api_url).json()
image_list = url_r.get('hits')
i = 0
image_url_list = []
for image in image_list:
    img_url = image.get('webformatURL')
    image_url_list.append(img_url)
for img in image_url_list:
    single_image = get(image_url_list[i]).content
    with open(f'images/{i}.jpg', 'wb') as file:
        file.write(single_image)
    i += 1

