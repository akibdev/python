# a company decided to give bonnus of 5% to employee, if his or her year of service is more than 5 years.
# ask user for there salary and year of service and print the amount of net salary

salary = int(input('Enter your salary amount: '))
experience = float(input('enter your job experience year: '))
bonus = 0.25
expeccted_experience = 5
expeccted_salary = 5000 



if experience >= expeccted_experience and salary >= expeccted_salary:
   calculation = salary + (salary*bonus)
   print('your net salary will be', calculation)
else:
   print('sorry, you are not aligible')