# Create a new file called the_cyclone.py. Ask the user what their height is and how many credits they have, and store the values in a height variable and a credits variable.

height = int(input('Your height: '))

credits = int(input('Credits: '))

if (height >= 137) and (credits >= 10):
    print('Enjoy the ride!')
elif (height < 137) and (credits >= 10):
    print('You are not tall enough to ride.')
elif (height >= 137) and (credits < 10):
    print("You don't have enough credits.")
else:
    print("You haven't met either requirement.")
