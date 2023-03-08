pthon = 'hello, i am alamin, i am 28 years old. \nI live in narayangonj. I love python.'

print(pthon)
print(pthon.split()) # the defaut arguement of separator is space
print(pthon.split(','))
print(pthon.split(',', maxsplit=1))
print(pthon.splitlines(True)) #false in default situation for line break (\n). if select true then print the code of line break