# student = []
# while True:
#    name = input('enter student name: ')
#    if name == 'sesh':
#       print(student)
#       print('total', len(student))
#       break
#    else:
#       student.append(name)
#       print(student)
      

import random

number_list = [1,2,3,4,5,6,7,8,9]
computer_number = random.choice(number_list)
while True:
   your_number = int(input('Enter your number: '))
   if your_number == computer_number:
      print('congrats you choose the right number')
      break
   else:
      print('sorry')


# # student = []
# # while True:
# #    name = input('enter your name: ')
# #    if name == 'sesh':
# #       print(student)
# #       print('total', len(student))
# #       break
# #    else:
# #       student.append(name)

# import random
# print('Game start. guess a number.')
# print('*'*25)

# number = [1,2,3,4,5,6,7,8,9]
# computer_number = random.choice(number)
# while True:
#    user_number = int(input('Enter your number: '))
#    if user_number == computer_number:
#       print('congratulation. your number is correct')
#       break
#    else:
#       print('sorry')

# # import random
# # print('Game start')
# # print('*'*25)

# # number = [1,2,3,4,5,6,7,8,9]
# # computer_number = random.choice(number)
# # while True:
# #     user_number = int(input('enter your number: '))
# #     if user_number == computer_number:
# #       print('congratulation. your number is correct')
# #       break
# #     else:
# #       print('sorry')
        
     