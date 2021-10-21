# WAP to filter even number in a list without using filter and without lamda
def num_even(lst):
    even_list = []
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            even_list.append(lst[i])
    print("even number list : ", even_list)


lst1 = [2, 3, 5, 4, 6, 7, 9, 8, 11, 12]
print("original list : ", lst1)
num_even(lst1)

# WAP to filter even number in a list without using filter and without lamda

even_list2 = list(filter(lambda n: n % 2 == 0, lst1))
print("even number list using filter and lamda : ", even_list2)


# WAP to filter even number in a list with using filter and without lamda
def even_filter(n):
    return n % 2 == 0


even_list3 = list(filter(even_filter, lst1))
print("even number list using filter and withoue lamda : ",even_list3)
