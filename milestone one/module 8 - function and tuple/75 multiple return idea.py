# def calculation(a, b):
#    add = a+b
#    subs = a-b
#    mul = a*b
#    return add, subs, mul

# x, y, z = calculation(5, 6)
# print(x)
# print(y)
# print(z)


def calculation(a, b, c):   
   """_summary_

   Args:
       a (int): a value
       b (int): b value
       c (int): c value

   Returns:
       int: calculation of the value
   """
   add = a+b+c
   sub = a+b-c
   mul = a*b*c
   frac = a*b/c
   return add, sub, mul, frac

a,b,c,d = calculation(4,5,6)
print(a)
print(b)
print(c)
print(d)
print(a,b,c,d.__doc__)






# name = ['hello', 'one', 'two']
# role = {
#    'name':'al amin',
#    'role':'40'
# }
# print(type(role))