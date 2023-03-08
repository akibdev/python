# endswith, startswith, index, rindex


pthon = 'python is awesome language, isn\'t it?. yes really awesome'

print(pthon.endswith('?g'))
print(pthon.endswith('r'))
print(pthon.endswith('it'))
print(pthon.startswith('p'))
print(pthon.startswith('python'))
print(pthon.index('awesome' ))
print(pthon.rindex('awesome'))
print(pthon.index('is',10,50))
print(len(pthon))