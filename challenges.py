#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

def day_one():
    for i in range(2000,3201):
        if i % 7 == 0 and i % 5 != 0:
            print(i, end=',')

#Day 1a
#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
# Then, the output should be:40320_**

def factorial(num):
    if(num == 1):
        return 1
    
    return factorial(num - 1) * num

#Day 1c

#With a given integral number n, write a program to generate a dictionary that contains (i, i x i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.Suppose the following input is supplied to the program: 
# 8 should return {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

def num_dict(num):
    res = {}
    for i in range(1, num+1):
        res[i] = i * i
    return res



#day 2a

#Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a 
# tuple which contains every number.Suppose the following input is supplied to the program:

# 34,67,55,33,12,98

# Then, the output should be:


# ['34', '67', '55', '33', '12', '98']
# ('34', '67', '55', '33', '12', '98')

def day2a():
    l = input("please enter a list a numbers").split(',')
    t = tuple(l)
    print(l, t)
    

#Day 2b

# Define a class which has at least two methods:

# getString: to get a string from console input
# printString: to print the string in upper case.

# Also please include simple test function to test the class methods.

### Hints:

#Use **init** method to construct some parameters_

class Day2b(object):
    def __init__(self):
        self.s = ""

    def get_string(self):
        self.s = input("please enter a string  ")

    def print_string(self):
        print(self.s.upper())


# test1 = Day2b()
# test1.get_string()
# test1.print_string()

        









### **Question:**

# Write a program that calculates and prints the value according to the given formula:

# Q = Square root of [(2 _ C _ D)/H]

# Following are the fixed values of C and H:
# C is 50. H is 30.

# D is the variable whose values should be input to your program in a comma-separated sequence.For example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180

# The output of the program should be:
# 18,22,24
from math import sqrt

C = 50
H = 30

def math_prob(D):
    return sqrt((2 * C * D)/ H)