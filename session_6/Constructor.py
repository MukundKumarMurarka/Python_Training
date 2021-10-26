"""
In pyhton there is a special method which is started with double underscore (__) called init method as well as constructor in python
In Python, the method the __init__() simulates the constructor of the class.
This method is called when the class is instantiated.
It accepts the self-keyword as a first argument which allows accessing the attributes or method of the class.

We can pass any number of arguments at the time of creating the class object, depending upon the __init__() definition.
It is mostly used to initialize the class attributes. Every class must have a constructor, even if it simply relies on the default constructor.

Example of constructor or init method
"""


class Computer:  # creting class

    def __init__(self, cpu, ram):  # creating constructor
        self.cpu = cpu
        self.ram = ram

    def config(self):  # creating new function
        print("config is ", self.cpu, self.ram)


com1 = Computer("i5", 8)  # assgning value of variables
com2 = Computer("i7", 4)

com1.config()
com2.config()


# exaplem of constructor by definig veriables

class Employee:
    def __init__(self):
        self.name = "mukund"
        self.age = 23

    def show_detail(self):
        print("employee detail is ", self.name, self.age)


emp1 = Employee()
emp1.show_detail()


# example with if condition:
class Student:
    def __init__(self):
        self.name = "krishna"
        self.marks = 91

    def compare(self, stu2):
        if stu1.marks == stu2.marks:
            return True
        else:
            return False


stu1 = Student()
stu1.marks = 85  # changing the marks of student stu1
stu2 = Student()
if stu1.compare(stu2):
    print("there marks are same ")
else:
    print("there marks are not same ")


