def area_volume(length, height, width):
   area = length*height
   volume = height*length*width
   return area, volume, height, width, length

calculation = area_volume(40, 40, 20)
calculation_list = list(calculation)
calculation_list[0]=10
calculation_tuple = tuple(calculation_list)
print(calculation_tuple)
print(calculation_tuple[0])
print(calculation_tuple[1])
print(calculation_tuple[2])
print(calculation_tuple[3])


fruts = ['apple', 'banana', 'kola']
x,y,z = fruts

print(x)
print(y)
print(z)
print(type(z))