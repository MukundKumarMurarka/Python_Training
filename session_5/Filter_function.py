"""
Filter funtion :- The filter() method filters the given sequence with the help of a function that tests each element
                   in the sequence to be true or not.
        syntax:
        filter(function, sequence)
        Parameters:
        function: function that tests if each element of a sequence true or not.
        sequence: sequence which needs to be filtered, it can  be sets, lists, tuples, or containers of any iterators.
        Returns:
        returns an iterator that is already filtered.
"""


# example of filter function WAP to check even number in a list
def even_num(n):
    return n % 2 == 0


num = [3, 2, 4, 5, 7, 6, 8, 12, 11, 14]
even_lst = list(filter(even_num, num))
print("original list : ", num)
print("even number list : ", even_lst)

# filter function using lamda function (doing same problem
even_lst2 = list(filter(lambda n: n % 2 == 0, num))
print("print even list using lamda function : ", even_lst2)
