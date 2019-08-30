import random

number = random.randint(1,10)
print(number)
question = int(input('Guess a number between 1 and 10: '))
while question:
    if number > question:
        print('too low')
    elif number < question:
        print('too high')
    else:
        print('You got it')
        break
    question = int(input('Guess a number between 1 and 10: '))