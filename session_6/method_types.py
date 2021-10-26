"""
Method :- Method are also called as function.
          there are 3 types of methods in python 1. instance method    2. static method    3. class method
          we can difference between all the three methods using decorators.
          Like any function, decorators perform a task.
          The difference here is that decorators apply logic or change the behavior of other functions.
          They are an excellent way to reuse code, and can help to separate logic into individual concerns.
          The decorator pattern is Python's preferred way of defining static or class methods.
          Decorators have to immediately precede a function or class declaration. They start with the @ sign, and unlike normal methods, you don't have to put parentheses on the end unless you are passing in arguments.
"""
"""
1. Instance method :-  Instance methods must have self as a parameter, but you don't need to pass this in every time. 
                        instance method is declared without any decorators.
                        it works with instance variable.
                        example:
                        
"""


class car:
    def __init__(self, company, milage, sitter):  # instance variable is company milage and sitter
        self.company = company
        self.milage = milage
        self.sitter = sitter

    def configuration(self):  # defining of instance method with accessor method
        print("configuration of car is : ", self.company, self.milage, self.sitter)

    def fetch_detail(self):  # defining instance method with mutator method means modify the value
        self.milage = 20
        print(self.milage)


car1 = car("bmw", 15, 4)
car1.configuration()
car1.fetch_detail()

"""
static method :- this method does not belongs with class variables and instance variable.
                This method is used when we want to do something which is not concern with class variable and instance
                variable. 
                This method define by a decorators name @staticmethod
                 this method doesn't keeps any arguments.

"""
"""
Class Method:- class method works with class variables and keeps cls as argument.
                this is define by a decorators named @classmethod 
"""


class Company:
    company_name = "Tibil solutions"

    def __init__(self, s1, s2, s3):
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3

    def avderage(self):
        print((self.s1 + self.s2 + self.s3) / 3)
        print("accessing class variable in instance method ",self.company_name)

    @classmethod
    def get_name(cls):  # defining class method by  using decorators classmethod it uses cls as parameter
        print(cls.company_name)    #accessing class variable

    @staticmethod
    def info():   # defining static method using staticmethod decorators.
        print("this company belongs to data solution")


salary_1 = int(input("enter the salary of emp1 of first month"))

salary_2 = int(input("enter the salary of emp1 of second month"))
salary_3 = int(input("enter the salary of emp1 of third month"))
emp1 = Company(salary_1, salary_2, salary_3)
emp1.avderage()
emp1.get_name()
emp1.info()
