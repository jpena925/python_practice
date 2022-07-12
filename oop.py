# #object-oriented programming

# #Given the below class:
# class Cat:
#     species = 'mammal'
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age


# # 1 Instantiate the Cat object with 3 cats
# stella = Cat('stella', 7)
# luna = Cat('luna', 5)
# natalie = Cat('natalie', 33)


# # 2 Create a function that finds the oldest cat
# def oldest(*args):
#     return max(args)


# # 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
# print(f'The oldest cat is {oldest(stella.age, luna.age, natalie.age)} years old.')

class Pets():
    animals = []
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Simon(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Sally(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#1 Add nother Cat
class Jack(Cat):
    def sing(self, sounds):
        return f'{sounds}'

#2 Create a list of all of the pets (create 3 cat instances from the above)
my_cats = [Jack('Jack', 15), Sally('Sally', 16), Simon('Simon', 4)]

#3 Instantiate the Pet class with all your cats use variable my_pets
my_pets = Pets(my_cats)

#4 Output all of the cats walking using the my_pets instance
my_pets.walk()


class SuperList(list):
    def __len__(self):
        return 1000

super_list1 = SuperList();
super_list1.append(5)
print(issubclass(SuperList, list))


class Reed():
    def __init__(self, type, density, age):
        self.type = type
        self.density = density
        self.age = age


reed1 = Reed('Glotin', 16, 0)
print(reed1.type)