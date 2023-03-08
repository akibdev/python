
# text = 'hello my name is akibalamin'
# file = open('intro.txt', 'w')  # w, r, a, w+, r+, a+
# file.writelines(text)
# file.close()

# text = 'hello jonogon'
# file = open('intru.txt', 'w')
# file.writelines(text)
# file.close()

# text = 'hello jonogon'
# file = open('intro.txt', 'w')
# file.writelines(text)
# file.close()

# text = 'hello vailog'
# file = open('text.txt', 'a+')
# file.writelines(text+'\n')
# file.close()

# text = 'hello lonojon'
# file = open('filename.txt', 'a+')
# file.writelines(text+'\n')
# file.close()

# from httpx import get
#
# url_list = [
#     'https://www.digitaltrends.com/computing/best-wireless-mice/',
#     'https://www.nytimes.com/wirecutter/reviews/best-wireless-mouse/',
#     'https://simplicityhunter.com/minimalist-mouse/',
#     'https://www.techradar.com/news/best-small-mouse'
# ]
# for url in url_list:
#     r = get(url)
#     data = f'{url} --- {r.status_code}'
#     file = open('200 code url.txt', 'a+')
#     file.writelines(data+'\n')
#     file.close()



# file = open('200 code url.txt', 'r+')
# readfile = file.readlines()
# file.close()
# print(readfile)

file = open('200 code url.txt', 'r+')
read_file = file.readlines()
file.close()
print(read_file)