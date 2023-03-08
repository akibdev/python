egg_price = 12.50
egg_quantity = 20
print ('total egg price is', egg_price*egg_quantity, 'bdt')



bdt_exchange_rate = 106.5
usd = 100
print(usd, '$ in BDT', bdt_exchange_rate*usd, 'Taka')

banana_rate = 5.5
banana_quantity = 8
potato_quantity = 5
potato_rate = 30
rice_rate = 80
rice_quantity = 5


banana_price = banana_quantity*banana_rate
potato_price = potato_rate*potato_quantity
rice_price = rice_rate*rice_quantity


#method one
print('total cost of banana, rice and potato is', banana_price + potato_price + rice_price, 'BDT')   
#method Two
print ('total cost of banana, rice and potato is', banana_quantity*banana_rate + potato_rate*potato_quantity + rice_rate*rice_quantity, 'BDT')

#triangle calculation
height = 20
base = 25
print('tarea of triangle is', (height*base)/2) 


#  modulus operator (%)
first_number = 100
second_number = 3
reminder = first_number % second_number
print ('the remainder value is', reminder)