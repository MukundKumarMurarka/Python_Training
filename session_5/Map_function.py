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
# n = int(input("enter the size of list : "))
# lst = list(map(int, input("enter the element of list : ").split(",")))[:n]
# print(lst)


# example of map function WAP to check even number in a list
def even_num(n):
    return n % 2 == 0


num = [3, 2, 4, 5, 7, 6, 8, 12, 11, 14]
even_lst = list(map(even_num, num))
print("original list : ", num)
print("even number list : ", even_lst)

# map function using lamda function (doing same problem)
even_lst2 = list(map(lambda n: n % 2 == 0, num))
print("print even list using lamda function : ", even_lst2)
