import random
##this prints out a random number
number = random.randint(1,10)
##fetches user input
question = int(input('Guess a number between 1 and 10: '))

##uses while loop that is only true when the user enters something if the user is either hot or cold they are told the question is re asked and if the user guesses correctly
## it breaks the loop
while question:
    if number > question:
        print('too low')
    elif number < question:
        print('too high')
    else:
        print('You got it')
        break
    question = int(input('Guess a number between 1 and 10: '))