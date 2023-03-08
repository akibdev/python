name = input('enter name: ')
gender = input('gender (m/f): ')
if gender == 'm':
   profession = 'actor'
   pronoun = 'him'
else:
   profession = 'actress'
   pronoun = 'her'
print(f'{name} is a {profession}, i know {pronoun}')

f