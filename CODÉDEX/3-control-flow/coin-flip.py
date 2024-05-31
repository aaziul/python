import random

# all you need to know is that this program simulates a coin toss

num = random.randint(0,1) # gera um numero aleatorio no intervalo de 0 e 1

if num > 0.5:
  print('Heads')
else:
  print('Tails')
