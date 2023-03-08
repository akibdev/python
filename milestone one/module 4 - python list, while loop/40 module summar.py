# student = ['rony', 'samrat', 'sony', 'mony', 'jony']

# print(student[0]) 
# print(student[-2])
# student.append('pony')
# student.remove(student[3])
# student.insert(3, 'belal')
# student.sort(reverse= True)
# print(student)


number = [ 70, 26, 23, 55, 96, 69, 17, 44, 50, 61, 82, 65, 79, 58, 78, 16, 36, 40,  3, 71, 99, 20, 47, 64, 52, 80, 85, 77, 15, 66, 21, 33,  2, 98, 11, 42, 97, 38,  1, 56, 76, 25, 93,
 49, 63, 35, 13, 83, 88, 37, 32, 92, 31, 19, 34, 94, 72, 51, 87,  9, 57, 74,  5, 18, 27, 60]
number.sort()
# i = 0
# while i < len(number):
#    if number[i] % 2 == 0:
#       print(number[i], 'is even number')
#    i = i+1

i = 0
while i < len(number):
    if number[i] % 2 == 0:
        print(number[i], 'is even')
    i += 1