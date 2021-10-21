"""
Map Function:- map() function returns a map object(which is an iterator) of the results after
               applying the given function to each item of a given iterable (list, tuple etc.)
                Syntax :
                map(fun, iter)
                Parameters :
                fun : It is a function to which map passes each element of given iterable.
                iter : It is a iterable which is to be mapped. like list set etc
"""
# for example creating a list using map function and takes input from user
n= int(input("enter the size of list : "))
lst = list(map(int, input("enter the element of list : ").split(",")))[:n]
print(lst)
