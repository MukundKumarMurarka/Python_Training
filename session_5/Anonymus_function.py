"""
lamda funcion :- Python Lambda Functions are anonymous function means that the function is without a name.
                Similarly, the lambda keyword is used to define an anonymous function in Pytthon.
                we know def keyword follwed by function name is used to define a function but when we dont need to define
                a function with name then we use lamda keyword.
                Python Lambda Function Syntax:
                lambda arguments: expression
                example of lamda anonymas function is as follows :
"""


# function with def keyword .WAP to find a square a number

def square(num):
    num = num * num
    print(num)


square(5)

# WAP to find square of a number using lamda function
f = lambda a: a * a
result = f(5)
print(result)

"""
Note :- This function can have any number of arguments but only one expression, which is evaluated and returned.
        One is free to use lambda functions wherever function objects are required.
"""
