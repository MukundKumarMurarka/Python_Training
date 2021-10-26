"""
Polymorphism :-  the word polymorphism means heaving many forms.
                In programming polymorphism means that the same function name being used for different types
"""
# Example length function
name = "mukund"
list1 = [15, 12, 16]
print(len(name))
print(len(list1))
print(type(name))
print(type(list1))


# example of polymorphism with user defined function

def sumation(*d):
    add = 0
    for i in d:
        add = add + i
    print("Sumation of variable length : ", add)


sumation(5, 6, 9)
sumation(1, 2, 3, 4, 5, 6, 7, 8)


# example of polymorphism in in inheritance
class Human:
    def moving(self):
        print("young man can move fast")


class OldMan(Human):
    def moving(self):
        super().moving()
        print("old man move's slow")


human1 = Human()
human1.moving()
oldman1 = OldMan()
oldman1.moving()
oldman1.moving()


# polymorphism with function and objects
class car:
    def wheeler(self):
        print("car has 4 wheel")

    def cost(self):
        print("the cost of 4 wheeler is too high")


class Bike:
    def wheeler(self):
        print("bike has two wheel and its maintenance is too easy")

    def cost(self):
        print("bike cost is low as compare to car")


def fun_ojb(obj):
    obj.wheeler()
    obj.cost()


car1 = car()
bike1 = Bike()

fun_ojb(car1)
fun_ojb(bike1)




