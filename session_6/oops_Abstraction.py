"""
Abstraction :- Abstraction is used to hide the internal functionality of the function from the users.
                The users only interact with the basic implementation of the function, but inner working is hidden.
                User is familiar with that "what function does" but they don't know "how it does.

                In Python abstraction can be achieved by using abstract classes and interfaces.
                Python provides the abc module to use the abstraction in the Python program.

            Syntax
            from abc import ABC
            class ClassName(ABC):
"""
from abc import ABC, abstractmethod

# class Student(ABC):
#     @abstractmethod
#     def detail(self):
#         pass
# stu1 = Student()
# stu1.detail()
#


# abstract base class work



class Car(ABC):

    def mileage(self):
        print("different car gives different milage")


class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")


class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph ")


class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")


class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph ")


car1 = Car()
car1.mileage()

t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()

"""
Implementation Through Subclassing : 
By subclassing directly from the base, we can avoid the need to register the class explicitly. 
In this case, the Python class management is used to recognize PluginImplementation as implementing the abstract PluginBase. 
"""
# example
import abc


class Animal:
    def move(self):
        print("thay can walk")


class Bird(Animal):
    def move_bird(self):
        print("birds can't wolk but they fly")


print(issubclass(Bird, Animal))
print(isinstance(Bird(), Animal))

"""
Concrete Methods in Abstract Base Classes : 
Concrete classes contain only concrete (normal)methods whereas abstract 
classes may contain both concrete methods and abstract methods. 
The concrete class provides an implementation of abstract methods, 
the abstract base class can also provide an implementation by invoking the methods via super(). 

"""


class Rectangle(ABC):
    length =5
    bredth =7
    def area(self):
        print("area of rectangle is ", self.length*self.bredth)


class square(Rectangle):
    side_length =6
    def area_square(self):
        super().area()
        print("the area of square is ", self.side_length**2)


b1 = square()
b1.area_square()