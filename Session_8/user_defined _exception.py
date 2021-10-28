"""
user defined exception means that the error defined by user.
Exceptions need to be derived from the Exception class, either directly or indirectly.
Although not mandatory, most of the exceptions are named as names that end in “Error” similar to the
naming of the standard exceptions in python. For example:

"""


# exanple of user defined exception
class MyError1(Exception):


    def __init__(self, value):
        self.value = value


    def findError(self):
        return (self.value)


try:
    raise (MyError1(3 * 2))


except MyError1 as error:
    print('A New Exception occured: ', error.value)


    """
Deriving Error from Super Class Exception

Superclass Exceptions are created when a module needs to handle several distinct errors. 
One of the common ways of doing this is to create a base class for exceptions defined by that module. 

    """


# class Error is derived from super class Exception
class MyError(Exception):

    pass


class TransitionError(MyError):


    def __init__(self, prev, nex, msg):
        self.prev = prev
        self.next = nex

        self.msg = msg


try:
    raise (TransitionError(2, 3 * 2, "Not Allowed"))


except TransitionError as error:
    print('Exception occured: ', error.msg)