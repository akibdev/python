# import requests
# ip = requests.get('https://api.ipify.org?format=json')
# print(ip.json())
# data = ip.json()
# ip_code = data.get('ip')
# print (ip_code)


import requests

ip = requests.get('https://api.ipify.org?format=json')
data = ip.json()
ip_code = data.get('ip')
print(ip_code)