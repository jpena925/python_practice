#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included).The numbers obtained should be printed in a comma-separated sequence on a single line.

for i in range(2000,3201):
    if i % 7 == 0 and i % 5 != 0:
        print(i, end=',')

#Day 2
#Write a program which can compute the factorial of a given numbers.The results should be printed in a comma-separated sequence on a single line.Suppose the following input is supplied to the program: 8
# Then, the output should be:40320_**

def factorial(num):
    if(num == 1):
        return 1
    
    return factorial(num - 1) * num
