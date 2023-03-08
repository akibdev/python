# grade calculator
number = int(input('Enter the number you got: '))
if number >= 80 and number <= 100:
   print('congratulation, you got A+ and grade point is 5')
elif number >= 70 and number <= 79:
   print('congratulation, you got A and grade point is 4')
elif number >= 60 and number <= 69:
   print('congratulation, you got A- and grade point is 3.5')
elif number >= 50 and number <= 59:
   print('congratulation, you got B and grade point is 3')
elif number >= 40 and number <= 49:
   print('congratulation, you got C and grade point is 2')
elif number >= 33 and number <= 39:
   print('congratulation, you got D and grade point is 1')
elif number >=0 and number <= 32:
   print('sorry, better luck next time')
else:
   print('Number is invalids')