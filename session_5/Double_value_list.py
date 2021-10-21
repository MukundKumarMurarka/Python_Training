# WAP to double all the values in the list using map and without lamda function

def double_all(n):
    return n * 2


lst = [10, 20, 22, 23, 24, 15, 14]
print("original list : ",lst)
double_list=list(map(double_all,lst))
print("doublly list : ",double_list)


# WAP to double all the values in the list using map and with lamda function
double_list2 = list(map(lambda n: n*2, lst))
print("doubly list using lamda function : ", double_list2)