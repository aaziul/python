'''
# exponents

score = 2 ** 2 # 2², score é igual a 4
print(score) #output: 4

score = 2 ** 3 # 2³, score é igual a 8
print(score) #output: 8

score = 2 ** 4 # 2^4, score é igual a 16
print(score) #output: 16

score = 2 ** 5 # 2^5, score é igual a 32
print(score) #output: 32
'''
#======================================
#BMI.PY
# Create a bmi.py program that calculates your own BMI.
# formula: bmi = mass/height²

height = 1.64
mass = 60

bmi = mass / (height**2)

print(f'your BMI is {bmi}')
