# user_one = ['joti', '30', False, 'feni']
# # print(user_one[0], user_one[-1], sep=' - ')
# # print(user_one[3], user_one[-2], sep=' - ')
# name = user_one[0]
# is_male = user_one[2]
# age = user_one[1]
# location = user_one[3]
# if is_male:
#    gender = 'man'
#    pronoun = 'He'
# else:
#    gender = 'woman'
#    pronoun = 'She'
# print(f'{name} is a {gender} of 34 years. {pronoun} lived in {location}.')

user_one = ['joti', 30, False, 'Feni']
name = user_one[0]
age = user_one[1]
is_male = user_one[2]
locaiton = user_one[3]

if is_male:
   pronoun = 'he'
   gender = 'man'
else:
   pronoun = 'she'
   gender = 'woman'

print(f'{name} is a {gender}. {gender} is {age} years old. {pronoun} lived in {locaiton}')