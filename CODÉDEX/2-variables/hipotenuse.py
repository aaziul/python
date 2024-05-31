import math

username = input('Enter your name: ')
print(username)

# quando recebemos no input, recebemos como string, para transformar em inteiro, por exemplo, fazemos:

age = int(input('What is your age? '))
print(age)

# -------------------------------------------------------------------

# HIPOTENUSE.PY
# Create a hipotenuse.py program that asks the user for two numbers, a and b, and then calculates the hypotenuse c.

a = int(input('Number a: '))
b = int(input('Number b: '))

c = math.sqrt((a ** 2) + (b ** 2))

print(f'Hipotenuse = {c}')
