"""
Class:- class is just called the blueprint or sketch of objects.
        A class creates a new local namespace where all its attributes are defined.
        class is collection of objects and method it indicstes the state and behaviour of objects.
        we define class in python by class method.
        syntex of defining of class :- class class_name:

"""


# example of class
class Student:  # defining a class:  always put first letter of class is capital.
    marks = 95


print(Student.marks)  # print marks of student. we create instance of class


# example of class by using method and attributes
# The self parameter is a reference to the current instance of the class, and is used to access variables that belongs to the class.
class Student_2:
    marks1 = 99

    def maks_stu(self):  # defining function inside a class.
        print("i have got ", self.marks1, " in math")


print(Student_2.marks1)  # this will print the marks of student.
print(Student_2.maks_stu)  # this will print the hexadecimal output which indicates the address of class. we can call the function of class by classname.


#  There are also special attributes in it that begins with double underscores __.
#  For example, __doc__ gives us the docstring of that class.


class Student_2:
    """This is a student class with user defined function"""  # this is docstring of student class
    marks1 = 98

    def maks_stu(self):  # defining function inside a class.
        print("i have got ", self.marks1, " in math")


print(Student_2.marks1)  # this will print the marks of student.
print(Student_2.maks_stu)  # this will print the hexadecimal output which indicates the address of class
print(Student_2.__doc__)  # this will print the output of docsstring

"""
Objects:- Objects are called the instance of class.
        It can also be used to create new object instances (instantiation) of that class. 
        The procedure to create an object is similar to a function call.
        Syntax :-   objectname = classname()
        every time we create a object it is allocated a new space in the memory and its size is depend on
        its size of veriable and number of variable.
        Attributes may be data or method. Methods of an object are corresponding functions of that class.
"""


class Student_2:
    """This is a student class with creating an object."""  # this is docstring of student class
    marks1 = 97

    def maks_stu(self):  # defining function inside a class.
        print("i have got ", self.marks1, " in math")


stu = Student_2()  # creating an object and instantiating an objects of class
print(stu.marks1)  # calling attributes of class by its object. we can define more than one objects in a single class.
Student_2.maks_stu(stu)  # calling function of class by giving object as a parameter
stu.maks_stu()  # callling method of class by its object.
print(stu.__doc__)  # printing docstring of class by its object.

"""
Inner class:- we can create a class with in existing class. This is called inner class.
we can create object of inner class outisde the inner class and outer class as well as outside the inner class and 
inside the outer class 
"""


class Company():
    def __init__(self, name, address, item):
        self.name = name
        self.address = address
        self.item = item
        # self.emp1 = self.Employee(100, 25)  # defining an object of inner class inside outer class.

    def details(self):
        print("company detail : ", self.name, self.address, self.item)
        # print(self.emp1.emp_detail())  # calling method of inner class inside the outer class function

    class Employee:
        def __init__(self, total_number, team_number):
            self.total_number = total_number
            self.team_number = team_number

        def emp_detail(self):
            print("employee detail : ", self.total_number, self.team_number)


compn1 = Company("tibil", "banglore", "software")
compn2 = Company("mahindra", "delhi", "cars")

emp1 = Company.Employee(100, 25)  # creating object of inner class outside of both class
emp2 = Company.Employee(112, 23)  # creating object of inner class outside of both class
compn1.details()
emp1.emp_detail()  # calling method of inner class outside the both class
compn2.details()  # calling method of inner class outside the both class
emp2.emp_detail()
