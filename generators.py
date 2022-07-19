#get the fib numbers up to the nth number in the sequence
#the generator solution prints the numbers once at a time instead of saving all of it to one list

def fib(num):
    a = 0
    b = 1
    for i in range(num):
        yield a
        temp = a
        a = b
        b = temp + b

for x in fib(20):
    print(x)


#as a list, where the numbers are stored in a list vs printed in memory once at a time

def fib2(number):
    a = 0
    b = 1
    result = []
    for i in range(number):
        result.append(a)
        temp = a
        a = b
        b = temp + b
    return result

print(fib2(20))