#formated string (f'')

country_name = input('Enter country name: ')
country_code = input('Enter country code: ')

# sentance = 'The ' + country_name + ' country code ' + country_code + ' will allow you to call ' + country_name + ' from another country. ' + country_name + ' telephone code ' + country_code + ' is dialed after the IDD. ' + country_name + ' international dialing ' + country_code + ' is followed by an area code.'
# print( sentance)

peragraph = f'ABOUT {country_name}\
CountryCode.org is your complete guide to make a call from anywhere in the world, to anywhere in the world. This page details {country_name} phone code.\
The {country_name} country code {country_code} will allow you to call {country_name} from another country. {country_name} telephone code {country_code} is dialed after the IDD. {country_name}  international dialing {country_code} is followed by an area code.\
The {country_name} area code table below shows the various city codes for {country_name}. {country_name} country codes are followed by these area codes. With the complete {country_name} dialing code, you can make your international call.'
print(peragraph)