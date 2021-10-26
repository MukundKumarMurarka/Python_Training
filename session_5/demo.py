lst=[12, 9, 15, 13, 7, 17]

new_list = list(filter(lambda n: n%3 ==0, lst))
print(new_list)