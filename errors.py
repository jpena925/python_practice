#create error handling for a value error when asking input for their age.
#include try, except, else and finally

while True:
    try:
        age = int(input('how old are you?'))
    except ValueError:
        print('please enter a number')
    else:
        print(f'Wow you don\'t look {age} years old!')
        break
    finally:
        print('Have a good day you old bat')
