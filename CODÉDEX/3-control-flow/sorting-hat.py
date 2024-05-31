# Write a sorting_hat.py program that asks the user some questions using int() and places them into one of the Houses based on their answers

gryffidor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

print("Q1) Do you like Dawn or Dusk?")
print("      1) Dawn")
print("      2) Dusk")

answer = int(input('Answer: '))

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print('Wrong input.')

print("Q2) When I'm dead, I want to remember me as:")
print("      1) The Good")
print("      2) The Great")
print("      3) The Wise")
print("      4) The Bold")

answer = int(input('Answer: '))

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print('Wrong input.')

print("Q3) Which kind of instrument most pleases your ear?")
print("      1) The violin")
print("      2) The trumpet")
print("      3) The piano")
print("      4) The drum")

answer = int(input('Answer: '))

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 4
elif answer == 3:
    ravenclaw += 4
elif answer == 4:
    gryffindor += 4
else:
    print('Wrong input.')

if (gryffindor > hufflepuff)and(gryffindor>slytherin) and (gryffindor>ravenclaw):
    print('Welcome to GRYFFINDOR! 🦁')
elif (hufflepuff > gryffindor)and(hufflepuff > slytherin)and(hufflepuff > ravenclaw):
    print('Welcome to HUFFLEPUFF! 🦡')
elif (ravenclaw > gryffindor)and(ravenclaw > slytherin)and(ravenclaw > hufflepuff):
    print('Welcome to RAVENCLAW! 🦅')
elif (slytherin > gryffindor)and(slytherin > ravenclaw)and(slytherin > hufflepuff):
    print('Welcome to SLYTHERIN! 🐍')
else:
    print('Try again!')
