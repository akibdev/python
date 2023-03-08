import requests
key = 'AIzaSyAKgJAazcgGrwKx0ivk4rDb0tFSBV3P7x4'
your_address = input('enter your website address(with https): ')
psi_url = f'https://www.googleapis.com/pagespeedonline/v5/runPagespeed?url={your_address}&{key}'
psi_score = requests.get(psi_url)
if psi_score.status_code == 200:
    data = psi_score.json()
    cls = data.get('loadingExperience').get('metrics').get('FIRST_CONTENTFUL_PAINT_MS').get('percentile')
    print(cls)
else:
    print('something went wrong')