# # '''
# # istitle(), isupper(), islower(), isspece(), isidentifier(), encode, 

# # '''

# # pthon1 = 'i am alamin'
# # pthon2 = 'I Am Alamin'
# # pthon3 = ' '
# # pthon4 = 'hello'
# pthon5 = '34section'
# pthon6 = 'My name is Ståle'


# print(pthon6.encode())
# print(pthon4.isidentifier(), pthon5.isidentifier())

# # # print(pthon3.isspace())
# # # print(pthon2.isidentifier())
# # # print(pthon1.istitle())
# # # print(pthon1.isupper())
# # # print(pthon1.islower())
# # # print(pthon2.isupper())
# # # print(pthon2.istitle())
# # # print(pthon2.islower())
# # # txt = 'demo'
# # # print(txt.isidentifier())

str="Hello! Welcome to Tutorialspoint."
str_encoded= str.encode()
print("The encoded string is: ", str_encoded)
str_decoded=str_encoded.decode()
print("The decoded string is: ", str_decoded)