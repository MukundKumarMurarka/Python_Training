"""
Iterator : An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().


"""

print("example 1 of iterator ")
names = ["mukund", "krishna", "nitish", "peater", "sanjay"]
iter_object = iter(names)
print(iter_object.__next__())
print(iter_object.__next__())
print(iter_object.__next__())
print(iter_object.__next__())
print(iter_object.__next__())
# print(iter_object.__next__())

print("2. example of iterator using for loop : ")
for i in names:
    print(i)

"""
To create an object/class as an iterator you have to implement the methods __iter__() and __next__() to your object.
iter method do the same thing which is done by init method i.e initialization. 
The __iter__() method acts similar, you can do operations, but must always return the iterator object itself.
The __next__() method also allows you to do operations, and must return the next item in the sequence.

"""

print("3. example of iterator by making ou own iterator  ")


class Topten:
    def __init__(self):
        self.num = 1

    def __iter__(self):  # this will initialize an iterator
        return self

    def __next__(self):  # this will increment the iterator
        if self.num <= 10:
            val = self.num
            self.num = self.num + 1

            return val
        else:
            raise StopIteration  # this will stop the iterator when the condition is satisfies.


number = Topten()     #creating objets of Topten class
print(number.__next__())
for i in number:
    print(i)

"""
StopIteration is used to stop the iteration. when we dont use StopIteration then the loop cann't stop even condition
will gone false. it will print the exact value till the condition is fulfill after that it will print None only infinetly 
"""