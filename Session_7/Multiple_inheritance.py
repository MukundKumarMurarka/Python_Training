"""
Multiple Inheritance means that we derive a class from two or more parent class
"""


class Additon:
    a = 10
    b = 13

    def __init__(self):
        self.a = 10
        self.b = 12

    def sumation(self):
        print("Addition of two number is : ", (self.a + self.b))


class Substraction:
    c=16
    d=6
    def __init__(self):
        self.c = 16
        self.d = 6

    def minus(self):
        print("Substraction of two number is  : ", (self.c - self.d))


class Calculator(Additon, Substraction):
    def __init__(self):
        self.e = 13
        self.f = 2

    def calculation(self):
        super().sumation()
        super().minus()
        print("Multiplication of two number is : ", self.e * self.f)


calci = Calculator()
# add = Additon()
# sub = Substraction()
calci.calculation()
# add.sumation()
# sub.minus()
calci.sumation()
# calci.minus()
