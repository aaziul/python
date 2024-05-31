# Create a ph-levels.py program that checks whether a pH level is basic, acidic, or neutral.
import random

ph = random.randint(0,14)

print(f'pH level: {ph}')

if ph > 7:
    print('Basic.')
elif ph < 7:
    print('Acidic.')
else:
    print('Neutral.')
