# body_temparature = 98.6
# user_body_temparature = float(input('Enter your body temperature: '))
# if user_body_temparature >= body_temparature:
#    print('Peracitamol 2 bela')
# else:
#    print('Dont worry, your are okey')

# Shakib Khan born 28 March 1979. He is a Bangladeshi actor, he works in Bengali films. In his career spanning about 10 years,

name = input('Enter actress name: ')
gender = input('Gender (M/F): ')
born = input('Born in: ')
country = input('country name: ')
experience_year = input('Experience year in film industry (years): ')
films_industry = input('which film indurstry he/she work in: ')

if gender == 'M':
   profession = 'actor'
   known_as = 'nayok'
   pronoun = 'He'
   pronoun2 = 'his'
else:
   profession = 'actrss'
   known_as = 'naika'
   pronoun = 'She'
   pronoun2 = 'her'
print (f'{name} born {born}. {pronoun} is a {country} {profession}. {pronoun} works in {films_industry} films. In {pronoun2} career spanning about {experience_year} years.')