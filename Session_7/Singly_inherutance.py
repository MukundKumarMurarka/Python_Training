"""
Singly Inheritance :-Single inheritance enables a derived class to inherit properties from a single parent class,
                        thus enabling code reusability and the addition of new features to existing code.
"""


# example of singly inheritance:
class Animal:
    def insect(self):
        print("they can not walk ")

    def bird(self):
        print("they can not walk they can fly")



class Animal_A(Animal):
    def isAnimal(self):
        super().insect()
        super().bird()
        print("some animal can walk and some are some can not walk they can fly")
animal = Animal_A()
animal.isAnimal()



