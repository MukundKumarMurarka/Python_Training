"""
A shallow copy is a copy of an object that stores the reference of the original elements.
It creates the new collection object and then occupying it with reference to the child objects found in the original.
It makes copies of the nested objects' reference and doesn't create a copy of the nested objects.
So if we make any changes to the copy of the object will reflect in the original object. We will use the copy() function to implement it.
"""
# copy one list into other list using assignment opearator

list1 =  [1,2,3,4,5,6]
print("original list  : ", list1)
list2 = list1
print("copied list : ", list2)

"""
the drow back with the assignment operator is that when we change the value of element in list1 or list2 it will
autometically reflect in other list.
that's not hapenning with shallow copy 
for example :

"""
list3 =  [4,5,6,7,8,9]
print("list 3 original copy : ",list3)
list4 = list3.copy()
print("copied list list4 : ",list4)
list4[2] =  100
print(" print list4 after change the value :  ", list4)
print(" print again list after change the value in list4 : ", list3)

"""
Shallow copy slightly change with nested list or we can say two dimension list. 
for example :

"""
list5 = [[1,2,3],[4,5,6],[7,8,9]]
print ("original list5 : ",list5)
list6 = list5.copy()
print(" print copied list list6 : ", list6)
list6[2][1] = 154
print("print list list6 after changing the vlaue : ",list6)
print("print list5 after changing the value from list6 : ",list5)

"""
Deep copy :- A deep copy is a process where we create a new object and add copy elements recursively. 
We will use the deecopy() method which present in copy module. 
The independent copy is created of original object and its entire object. 
 example.

"""
import copy

x = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
z = copy.deepcopy(x)
print("print original copy of list x :  ",x)
print("print copied of list x which is list z : ",z)

#change the value of any element in list z
z[1][1]=165
print("print new list z after changing the value :  ",z)
print("print again list x after changing the value of list z : ",x)

"""
now value will not change in list x 
"""

"""
Copying Arbitrary Python Objects
We can also copy the arbitrary Python objects including custom classes using copy method. 
The copy.copy() and copy.deepcopy() method can be used to duplicate any objects.
"""
class Myclass:
    def __init__(self,x,y):
        self.x=x
        self.y=y
    def new_fun(self):
        print(self.x, self.y)
clss1 = Myclass(15,19)
clss2= copy.copy(clss1)
clss1.new_fun()
print(clss1)
clss2.new_fun()
print(clss2)
print(clss1 is clss2)