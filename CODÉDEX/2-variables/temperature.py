'''
score = 0 # score no momento é igual a zero
print(score) # output: 0

score = 10 + 5 # score no meomento é igual a 15
print(score) # output: 15

score = 10 - 5 #score nest momento é igual a 5
print(score) # output: 5

score = 10 * 5 # score no momento é igual a 50
print(score) # output: 50

score = 10 / 5 # score no momento é igual a 2
print(score) # output: 2.0 | p.s: resultado de divisão é em float

score = 10 % 5 # score agora é igual ao resto da divisao de 10 por 5, logo score é igual a 0
print(score) # output: 0
'''

#------------------------------------------------------------------------------

# Create a temperature.py program that converts a temperature from Fahrenheit (°F) to Celsius (°C).
# formula: °C = (°F - 32)/1.8

fahrenheit = 62

celsius = (fahrenheit - 32) / 1.8

print(f'Converted temperature: {celsius}')
