# def multiple_number(*args):
#   total_number = 0
#   for number in args:
#     total_number += number
#   return total_number

# total_number = multiple_number(1,2,3,4,5,6,7,8,9)
# print(total_number)

# def add_number(*args):
#   total = 0
#   for number in args:
#     total += number
#   return total

# total = add_number(1,2,3,4,5,6,7,8,9)
# print(total)



def add_number(*args):
  total = 0
  for number in args:
    total += number
  return total

total_number = add_number(int(1,2,3,4,5,6,6))
print(total_number)