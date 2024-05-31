# CURRENCY.PY (feito em 15/05/2024)
# Create a currency.py program that asks the user for the amount they have in pesos, soles and reais and calculates the total in USD.

pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))

total = (pesos * 0.00026) + (soles * 0.27) + reais * 0.19)

print(f'The total in USD is {total}')
