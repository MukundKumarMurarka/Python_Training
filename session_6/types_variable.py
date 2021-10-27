"""
there are two types of variables in python
1. instance variable:-  instance variables are those variables which is define inside a method. and they only accessible
                        inside that variable
2. class or static variable:- class variables are those variable which is define inside a class and outside the method.
                            and they are accessible in the wholw program.

"""


class School:
    name = "upgrad"  # class variable

    def __init__(self, mst1, mst2, mst3):  #mst1, mst2, mst3 are instance variable
        self.mst1 = mst1
        self.mst2 = mst2
        self.mst3 = mst3

    def average(self):
        print("average of all mst marks : ", (self.mst1 + self.mst2 + self.mst3) / 3)
        print(School.name)


sch = School(30, 31, 35)
print("marks1 ", getattr(sch,"mst1"))  # accessing instance variable using getattr
sch.average()
print(School.name)

