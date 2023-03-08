# user = {
#    'id':'01',
#    'frist_name':'akib',
#    'last_name':'alamin',
#    'password':'123456',
#    'username':'admin',
#    'role':'admin'
# }
# first_name = user.get('frist_name')
# last_name = user.get('last_name')
# print(first_name, last_name)

# keys = user.keys()
# print(list(keys))

# value = user.values()
# print(list(value))
user = {
   'id':'01',
   'first_name':'akib',
   'last_name':'alamin',
   'pass':'123456',
   'username':'akibdev',
   'role':'admin'
}

print(user['id'])
print(user.get('first_name'))
print(user['last_name'])
print(user.get('pass'))
print(user['username'])
print(user.get('role'))