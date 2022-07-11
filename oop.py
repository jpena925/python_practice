#object-oriented programming

#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
stella = Cat('stella', 7)
luna = Cat('luna', 5)
natalie = Cat('natalie', 33)


# 2 Create a function that finds the oldest cat
def oldest(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {oldest(stella.age, luna.age, natalie.age)} years old.')