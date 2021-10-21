# WAP to add number from list using reduce function and without lamda function
from functools import reduce


def add_all(a, b):
    return a + b


list = [14, 23, 25, 29, 19, 55]
print("adding all values in the list : ", reduce(add_all, list))

# WAP to add number from list using reduce function with lamda fuction
print("adding all elements of list using lamda function : ",reduce(lambda a,b : a+b,list))
