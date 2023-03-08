# person = {
#    'id':'01',
#    'title':'this is a awesome title',
#    'content':'this is a awesome content',
#    'author':'awesome name',
#    'category':'awesome',
#    'slug':'awesome title'
# }


# person['slug'] = 'awesome slug'
# person.update({'category':'awesome category'})
# person.update({'pass':'12345'})

# print(person.get('slug'))


car = {
   'brand':'totota',
   'model':'supra',
   'year':'2000'
}


car.update({'color':'red'})
car['category'] = 'sports'
print(car)
key = car.keys()
print(list(key))
value = car.values()
print(list(value))

print(car.get('model'))