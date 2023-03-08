# len and count

pthon = 'hello, my name is alamin. I am 28 years old, my number is 0192837465'

print('total character count is ',len(pthon))

substr = 'is'
print(substr, 'present',pthon.count(substr),'times')

subs2 = 'a'
print(subs2,'present', pthon.count(subs2), 'times')

subs3 = 'e'
print(subs3, 'is present', pthon.count(subs3,20,40),'times')


# string.count(substring) --- return total number of substring
# string.count(substring,strart_number,end_number) --- return total number between start and end number