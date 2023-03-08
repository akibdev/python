cars = {
   'brand':'mahindra',
   'model':'thar',
   'category':'adventure'
}

cars.pop('model')

for car in cars:
   print(car)

cars.update({'drive':'four wheel drive'})
cars['seat'] = '4 seat'
print(cars)
keys = cars.keys()
print(list(keys))
value = cars.values()
print(list(value))
print(cars.get('seat'))
print(len(cars))