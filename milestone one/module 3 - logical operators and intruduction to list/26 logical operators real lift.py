user = 'hello'
password = '123445'

input_user = input('Username: ')
input_pass = input('Password: ')

# if input_user == username and input_pass == password:
#    print('welcome')
# else:d
#    print('something went wrong')

# if input_user != "a" and input_pass != "a":
#    print('something went wrong')
# else:
#    print('welcome')

if not( input_user == user and input_pass == password):
   print('wrong')
else:
   print('welcome')
