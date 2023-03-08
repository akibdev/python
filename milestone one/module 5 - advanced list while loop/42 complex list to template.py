# person = [
#    ['Jennifer', 'female', '9/1/1965', 'Hayhurst Lane', 'Michigan', '248-764-8187'],
#    ['John R', 'male', '1/6/1972', 'Deegan Lake', 'New York', '607-244-7240'],
#    ['Leroy', 'female', '6/7/1992', 'Granville Lane', 'New Jersey', '973-445-4325'],
#    ['James P ', 'male', '10/9/1988', 'Rosemont Avenue', 'Florida', '321-867-1002'],
#    ['Tashia', 'female', '9/23/1985', 'Smithfield Avenue', 'Texas', '806-755-1676'],
#    ['Jorge C', 'male', '12/21/1984', 'Poe Road', 'Carolina', '843-246-5598'],
# ]

# i = 0
# while i < len(person):
#    name = person[i][0]
#    gender = person[i][1]
#    date_of_birth = person[i][2]
#    area = person[i][3]
#    city = person[i][4]
#    phone_number = person[i][4]
#    if person[i][1] == 'male':
#       pronoun = 'he'
#       relative = 'his'
#    else:
#       pronoun = 'she'
#       relative = 'her'
#    sentance = f'{name} is {gender}, {pronoun} lives in {area} at {city}. {relative} date of birth is {date_of_birth}. {relative} contact number is {phone_number}.' 
#    print(sentance)
#    i = i+1

person = [
   ['Jennifer', 'female', '9/1/1965', 'Hayhurst Lane', 'Michigan', '248-764-8187'],
   ['John R', 'male', '1/6/1972', 'Deegan Lake', 'New York', '607-244-7240'],
   ['Ler1oy', 'female', '6/7/1992', 'Granville Lane', 'New Jersey', '973-445-4325'],
   ['James P ', 'male', '10/9/1988', 'Rosemont Avenue', 'Florida', '321-867-1002'],
   ['Tashia', 'female', '9/23/1985', 'Smithfield Avenue', 'Texas', '806-755-1676'],
   ['Jorge C', 'male', '12/21/1984', 'Poe Road', 'Carolina', '843-246-5598'],
]

i = 0
while i < len(person):
   name = person[i][0]
   gender = person[i][1]
   date_of_birth = person[i][2]
   area = person[i][3]
   city = person[i][4]
   phone = person[i][5]
   if person[i][1] == 'male':
      pronoun = 'he'
      relative = 'his'
   else:      
      pronoun = 'she'
      relative = 'her'
   sentance = f'{name} is {gender}, {pronoun.title()} lives in {area} at {city}. {relative} date of birth is {date_of_birth}. {relative.title()} contact number is {phone}.'
   print(sentance)
   i = i+1