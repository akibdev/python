pthon = 'alamin'
pthon2 = 'md al \tamin'
pthon3 = 'hello world'
pthon4 = 'my name is alamin'

print(pthon.center(20,'*'))
print(pthon.center(60,'-'))
print(pthon.ljust(30,'-'))
print(pthon.rjust(30,'-'))
print(len(pthon))

print(pthon2.expandtabs(30))
print(pthon2.expandtabs(20))
print(pthon2.expandtabs(8))
print(pthon2)

pthonlist = ['hello', 'my', 'name', 'is', 'al', 'amin']
print(pthonlist)
print(pthonlist[3])
print(' '.join(pthonlist))

pthon3 = 'hello world'
print(pthon3[3])
print(pthon3[3:])
print(pthon3[3:7])
print(pthon3[:7])