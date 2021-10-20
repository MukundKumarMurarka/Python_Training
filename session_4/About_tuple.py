###Tuple :- Tuples are used to store multiple items in a single variable.
# A tuple is a collection which is ordered, unchangeable and support duplicate element.
# Tuples are written with round brackets.
#syntex of tuple is tup =()

#create a tuple
brand= ("adidas","U S polo","jockey", "puma", 10,20)
print("print the Tuple : " ,brand)  # printing the tuple


#Access the element of tuple by giving index number in square bracket
print(brand[2]," element present at index 2")
print(brand[-1]," element present at last position")

#Slicing of tuple
print("short tuple : ",brand[1:3])
print("short tuple : ",brand[-5:-3])

#tuple with if Statement
if "jockey" in brand:
    print("yes it is present")
else:
    print("no it is not present")


#Tuple are basically is immutable we cannot change the value of tuple.
#we can change the value of tuple by convert it into list and again the updated list into tuple
# we can add, update,and remove the value of tuple by convert it into list just like we do in list
#convert tuple into list
brand_list= list(brand)
print("branding list",brand_list)
brand_list[0]= "roaduster"
brand_list.append("wrong")  #add element in tuple
brand = tuple(brand_list)
print("updated tuple : ",brand)


#add two tuple
item = ("shoes", "jeans", "shirts","jacket")
brand += item
print("print tuple after adding", brand)

#for loop in tuple
for i in range(len(brand)-1):
    print(brand[i],end=" ")

#while loop in tuple
i=0
while i<len(brand):
    print(brand[i], end=" ")
    i=i+1

#count() method in tuple count number of appearence of a particuler element in tuple
#syntax tuple.count(value)
print(brand.count(10))

#Deleting the tuple del() htis will delete thw hole tuple
del(brand)


#create an empty list,set,tuple and dictionary
emp_list = []
print(type(emp_list))

emp_tuple = ()
print(type(emp_tuple))

emp_set={}
print(type(emp_set))

emp_dict=dict()
print(type(emp_dict))






