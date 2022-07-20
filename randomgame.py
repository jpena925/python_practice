#creating a game that has lets a user see if they can guess a number within a range of their choice


import sys
import random

begin = int(sys.argv[1])
end = int(sys.argv[2])

answer = random.randint(begin,end)

print(f'Hello! Let\'s choose a random number between {begin} and {end}')

while True:
    try:
        chosen = int(input('Please choose a number:  '))
        if begin <= chosen <= end:
            if chosen == answer:
                print(f'We chose {chosen}, too! You win!!!')
                break;
            else:
                print(f'You chose the wrong number. You lost, loser.')
        else:
            print(f'Please select a number between {begin} and {end}.')
    except ValueError:
        print('Please enter a number.')
        continue;


