from requests import get
file = open('imageUrlList.txt', 'r+')
url_list = file.readlines()
file.close()
new_url = []
i = 0
for url in url_list:
    single_url = url.strip('\n')
    new_url.append(single_url)
    single_url = new_url[i]
    r = get(single_url)
    file = open(f'images/{i}.jpg', 'wb')
    file.write(r.content)
    file.close()
    i += 1

