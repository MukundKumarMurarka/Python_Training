"""
Encaptulation :-Encapsulation is the packing of data and functions that work on that data within a single object.
By doing so, you can hide the internal state of the object from the outside. This is known as information hiding.
A class is an example of encapsulation. A class bundles data and methods into a single unit. And a class provides the access to its attributes via methods.
"""


# example of encaptulation
class Calculator:
    num = 5

    def __init__(self, num):
        self.num = num

    def increment(self):
        print("increment of number is ", self.num + 1)

    def decrement(self):
        print("decrement of number is ", self.num - 1)

    def current(self):
        print("current value of number is ", self.num)


calci = Calculator(Calculator.num)
calci.increment()
calci.decrement()
calci.current()
calci.num = 67
calci.increment()



#example of encapsulation by private attributes
# we can not change the value of private attributes.
#private attributes is declared by uderscore example  :-  _attributename
# class Calculator1:
#     __number1= 10
#     def add_by_1(self):
#         print(self.__number1 + 1)
#     def subs_by_1(self):
#         print(self.__number1-1)
# calci2 =Calculator1()
# calci2.add_by_1()
# calci2.subs_by_1()
# Calculator1.__number1 = 12
# print(calci2.__number1)
# calci2.add_by_1()
