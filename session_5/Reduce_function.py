"""
Reduce function :- The reduce(fun,seq) function is used to apply a particular function passed in its argument to all of
                the list elements mentioned in the sequence passed along.This function is defined in “functools” module.
                reduce is present in module called funtools, we ave to import it from funtools by using syntax:-
                from functools import reduce

Working :

At first step, first two elements of sequence are picked and the result is obtained.
Next step is to apply the same function to the previously attained result and the number just succeeding the
second element and the result is again stored.
This process continues till no more elements are left in the container.
The final returned result is returned and printed on console.
"""

# example of reduce function without lamda fuction
from functools import reduce


def add_all(a, b):
    return a + b


list = [10, 21, 22, 23, 12, 25]
print("adding all values in the list : ", reduce(add_all, list))

# example of reduce function with lamda fuction
print("adding all elements of list using lamda function : ",reduce(lambda a,b : a+b,list))