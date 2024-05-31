import random

guess = random.randint(0,10)
answer = 0

while answer != guess:
  answer = int(input("Guess the number:  "))

print("You got it!")
