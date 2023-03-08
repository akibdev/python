#write a python function to convert string to url
# 'md al amin' to 'md-al-amin'

'''
steps: convert it to lowercase
replace blank spece with - (dash)
convert it to function
'''

def urlify(string):
   """
   this function will convert string to url
   :param string:
   :return: url 
   """

lower_case = string.lower()
url = lower_case.replace(' ','-')

print(url)


