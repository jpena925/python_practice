from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(item):
    return item.capitalize()

print(list(map(capitalize, my_pets)))

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

print(list(zip(my_strings, sorted(my_numbers))))

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def passing(item):
    return item > 50

print(list(filter(passing, scores)))

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def accu(acc, item):
    return acc + item

print(reduce(accu, scores + my_numbers))

#print a squared list using lambda
my_list = [5,4,3]

print(list(map(lambda item: item**2, my_list)))

#List Sorting
#sort based on the second number in the tuple
a = [(0,2), (4,3), (9,9), (10, -1)]

a.sort(key = lambda x: x[1])
print(a)

#Comprehensions
#return list of duplicates letters
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = list({letter for letter in some_list if some_list.count(letter) > 1})
print(duplicates)