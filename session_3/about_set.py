#Sets  :- A collection of unique elements is known as set.
#          set is represented by curly bracket. systex = set1= { }
#           Set using the concept of hash. it does not support indexing
#              Set items are unordered, unchangeable, and do not allow duplicate values.
#creating sets
employee={"mukund", "vijay", "amal", "faizan"}
print(employee)  # this will print the whole set but may be it is not in original sequence


employe={"mukund", "vijay", "amal", "faizan","viajy"} # this will remove the duplicity and print only single value
print(employe)

# Traversing the set
for i in employee:
    print("elements of set", i, end=" ")


employee.add("krishna")    #Add an item to a set, using the add() method
print("print sets after adding new element", employee, end=" ")

old_emp = {"satish", "abbas","ravi"}
employee.update(old_emp) # this update() method joins two sets we can use union() method also
print("collection of all employee", employee)


employee.discard("kishna")   # this discard() method is used to remove elemnet from set.
print("print sets after removing", employee)



