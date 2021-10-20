# List :- List is just like a array declared in other language.
#         A single list may contain datatypes like  integer, String as well as objects.
#         list is denoted by square bracket []. it is mutable. example
list1 = [10, 20, "mukund", "python", 20.56, "vijay", 15.32]
list2 = [15, 16, "nitish", "john", "peter"]
# print list
print(list1)

# add the element in list at the end
list1.append(50)
print(list1)

# add the element at a particular positon in list
list1.insert(2, "krishna")
print(list1)

# remove a particular value from the list
list1.remove(20)
print(list1)

# remove element at a particular index in the list
list1.pop(0)
print(list1)

# #print minimum abd maximum value from the list this works when all the integer value present in the list
# print(min(list1))
# print(max(list1))
#
# #sort the list in  increasing order
# list1.sort()
# print(list1)

# concatinate two lists
print(list1 + list2)

# change the value of particular index in the list
list2[1] = 30
print(list2)

# calculate length odf list
print(len(list1))

# list comprehension means that creating a newlist by compairing a particular value. for example in the below code
# make a new list with elememts which has n alphates. without using comprehension we use if condition in the for loop
# for creating a new list.
car = ["bmw", "lamborgini", "mercidize", "benz"]
newlist = []
for x in car:
    if "n" in x:
        newlist.append(x)
print(newlist)

# By using comprehension
car = ["bmw", "lamborgini", "mercidize", "benz"]
newlist = [x for x in car if "m" in x]
print(newlist)

# copy a list into other list
list3 = list2.copy()
print("list3", list3)
# another method by using builtin method
list4 = list(list2)
print("lst4", list4)

# slicing the list
print(list1[2:4])
