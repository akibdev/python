# currency converter with user input date (string to integer convert)

# bdt_exchange_rate = 106.5
# print(type(bdt_exchange_rate))
# usd_you_have = input('Enter your USD amount: ')
# print(type(usd_you_have))
# usd = int(usd_you_have)
# print(type(usd))
# calculation = bdt_exchange_rate*usd
# print('You have', calculation, 'Bangladeshi Taka')

# bdt_exchange_rate = 106.5
# usd_you_have = input('Enter Your USD Amount: ')
# usd = float(usd_you_have)
# calculation= bdt_exchange_rate*usd
# peragraph = str(usd) + ' USD is equals to ' + str(calculation) +' BDT'
# print(peragraph)

bdt_exchange_rate = 106.5
usd_you_have = input('Enter your USD amount: ')
usd = float(usd_you_have)
calculation = bdt_exchange_rate*usd
peragraph = str(usd) + ' USD is equals to ' + str(calculation) + ' BDT'
print(peragraph)