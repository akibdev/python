# year = [1953, 1952,1913,1962,2001,1911,1974,1959,1927,1917,1920,1981,1933,1928,]
# i = 0
# while i < len(year):
#    if year[i] % 4 == 0:
#       print(year[i], 'is leap year')
#    i = i + 1
# print(len(year))



year = [1986,1984,1962,2007,1961,2017,1949,2019,1917,1965,1955,1940,1978,1998,1947,1946,1992,1958,1954,1942,1971,1901,1987,1960,1962,1906,1957,1966,1964,2002,1900,961,1919,1909,
1946,1971,1966,1935,1940,1916,18,1920,2010,1935,2006,2004,1947,1993,1999,2000]
year.sort(reverse=True)
# i = 0
# while i < len(year):
#    if year[i] % 4 == 0:
#       print(year[i], 'is leap year')
#    i += 1
   
# year.sort()
# print(year)

i = 0
while i < len(year):
   if year[i] % 4 == 0:
      print(year[i], 'is leap year')
   i += 1
print(year)