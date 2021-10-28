"""
If a function contains at least one yield statement (it may contain other yield or return statements),
it becomes a generator function. Both yield and return will return some value from a function.

The difference is that while a return statement terminates a function entirely,
yield statement pauses the function saving all its states and later continues from there on successive calls.

yield keyword fetch the data from the database one by one
"""
print("1. example of generator ")


def topten():
    n = 1
    while n <= 10:
        yield n # ths will return the n values yield is justblikea return keyword
        n = n + 1


values = topten()
for i in values:
    print(i)


print("2. Example of generator calcualting square of topten numbers")
def topten_square():
    num=1
    while num <=10:
        square = num*num
        yield square
        num =  num+1
value = topten_square()
for i in value:
    print(i)