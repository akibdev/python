# number = int(input('enter your number: '))
# if number == 0:
#    print('the number is zero')
# elif number % 2 == 0:
#    print(number, 'is even')
# else:
#    print(number, 'is odd')

number = int(input('number you have got: '))
if number >= 80:
   print('congratulation. you got A+')
elif number >= 70:
   print('congratulation. you got A')
elif number >= 60:
   print('congratulation. you got B')
elif number >= 50:
   print('congratulation. you got C')
elif number >= 40:
   print('congratulation. you got D')
elif number >= 33:
   print('congratulation. you got E')
else:
   print('sorry, better luck next time')