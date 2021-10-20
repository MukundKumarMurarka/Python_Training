# 1. Python program to interchange first and last elements in a list.

def interchange_list(lst):
    lst[0], lst[n-1] =lst[n-1], lst[0]
    print("interchanged list ", lst)


n= int(input("enter the length of list : "))
lst = [ele for ele in input("enter the element if list : ").split()]
print("print original list" ,lst)
interchange_list(lst)

