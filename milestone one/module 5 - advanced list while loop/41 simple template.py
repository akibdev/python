person1 = [
   'al amin',
   'male',
   'bangladesh',
   '30 jul 1994',
   'akibalamin007@gmail.com',
   '01931366141'
]
gender = person1[1]
if gender == 'male':
   pronoun = 'he'
   relative = 'his'
else:
   pronoun = 'she'
   relative = 'her'

sentance = f'{person1[0].title()} is born in {person1[2].title()}. {relative.title()} date of birth is {person1[3]} {pronoun.title()} is available at {person1[4]} and {relative.title()} phone number is {person1[5]}'

print(sentance)