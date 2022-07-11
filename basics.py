# Exercises

# counter
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

counter = 0
for num in my_list:
    counter += num

print(counter)

# Exercise!
# Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

for row in picture:
    for item in row:
        if (item == 1):
            # end with empty string keeps the new line from occuring
            print('*', end='')
        else:
            print(' ', end='')
    print('')  # adds new line after each row


# check for duplicates
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

res = []

for letter in some_list:
    if (some_list.count(letter) > 1):
        if letter not in res:
            res.append(letter)

print(res)


def checkDriverAge(age=0):

    if int(age) < 18:
        print("Sorry, you are too young to drive this car. Powering off")
    elif int(age) > 18:
        print("Powering On. Enjoy the ride!")
    elif int(age) == 18:
        print("Congratulations on your first year of driving. Enjoy the ride!")


# 1. Wrap the above code in a function called checkDriverAge(). Whenever you call this function, you will get prompted for age.
# Notice the benefit in having checkDriverAge() instead of copying and pasting the function everytime?

# 2 Instead of using the input(). Now, make the checkDriverAge() function accept an argument of age, so that if you enter:
# checkDriverAge();
# it returns "Powering On. Enjoy the ride!"
# also make it so that the default age is set to 0 if no argument is given.

# highest even

def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)

    return max(evens)


print(highest_even([10, 2, 3, 4, 8, 11]))
