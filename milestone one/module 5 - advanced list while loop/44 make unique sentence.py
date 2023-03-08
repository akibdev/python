# import random
# parson = ['Moris', 'chittagong']
# name = parson[0]
# location = parson[1]

# sentance_group_one = [
#    f'My name is {name}',
#    f'This is {name}',
#    f'Hello I am {name}',
#    f'{name} is my name'
# ]
# sentance_gorup_two = [
#    f'i live in {location}',
#    f'i reside in {location}',
#    f'i was raised in {location}',
#    f'{location} is the place, where i reside'
# ]

# person_one_name = random.choice(sentance_group_one)
# person_one_location = random.choice(sentance_gorup_two)

# peragraph = f'{person_one_name}. {person_one_location}'

# print(peragraph)

import random

person_one_details = ['moris', 'chittogong', 34]
name = person_one_details[0]
location = person_one_details[1]
age = person_one_details[2]
sentance_group_one = [
   f'Hello my name is {name}',
   f'My name is {name}',
   f'Hi, I am {name}',
   f'This is {name}',
   f'I am {name}'
]
sentance_group_two = [
   f'I live in {location}',
   f'I was raised in {location}',
   f'I reside in {location}',
   f'{location} is the place, where i reside'
]
sentance_group_three = [
   f'I am {age}',
   f'I am {age} years old'
]
sentance_one = random.choice(sentance_group_one)
sentance_two = random.choice(sentance_group_two)
sentance_three = random.choice(sentance_group_three)
peragraph = f'{sentance_one} {sentance_two} {sentance_three}'
print(peragraph)
