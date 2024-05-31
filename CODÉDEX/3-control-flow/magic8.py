# Create a magic8.py that can respond to any Yes or No questions with a different answer each time it executes.
import random

answer = random.randint(0,8)

if answer == 0: 
  answer = 'Yes - definitely.'
elif answer == 1:
    answer = 'It is decidedly so.'
elif answer == 2:
    answer = 'Without a doubt.'
elif answer == 3:
    answer = 'Reply hazy, try again.'
elif answer == 4:
    answer = 'Ask again later.'
elif answer == 5:
    answer = 'Better not tell you now.'
elif answer == 6:
    answer = 'My sources say no.'
elif answer == 7:
    answer = 'Outlook not so good.'
elif answer == 8:
    answer = 'Very doubtful.'
else:
    answer = 'Error.'

input('Question: ')
print(f'Magic 8 ball: {answer}')
