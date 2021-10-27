"""
This term comes from the saying “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

Duck typing is a concept related to dynamic typing, where the type or the class of an object is less important than the methods it defines.
 When you use duck typing, you do not check types at all. Instead, you check for the presence of a given method or attribute.
"""


# example of ducktyping
class Bird:
    def fly(self):
        print("Birds can fly with help of their wings ")


class Flight:
    def fly(self):
        print("fight can fly with the help of fuel of piolet ")


class Bird_Flight:
    def move(self, bir1):
        bir1.fly()


obj = Bird()
bird = Bird_Flight()
bird.move(obj)
