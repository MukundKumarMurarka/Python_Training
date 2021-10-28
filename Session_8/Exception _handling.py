"""
Exceptions: Exceptions are raised when the program is syntactically correct, but the code resulted in an error.
This error does not stop the execution of the program, however, it changes the normal flow of the program.
eception is occured due to wrong input given by user.
Exception handling : -  the process by which we handle the exception is known as exception handling .
there are two blocks in exception handling.
1. try block : in this block we know that we get error. error occur by giving the wrong input
2. except block :- in this block we catch the error and out logic to handle the error, so that our code is run properly.

 for example
"""
# this example of exception comes under arithmatic error
print(" 1. example of exception ")
a = int(input("enter the first number "))
b  = int(input(" enter the second number "))
try:
    print(a/b)
except Exception as exe:
    print(" we cannot devide any number by zero ", exe )


# example of exceptoin i.e comes under the  exception LookupError. index error comess under the exception lookuperror
print("2. example of exception in list  ")
list = [10, 20, 23, 34, 45]
length = len(list)
n = int(input("enter the index number "))

try:
    print(list[n])
except Exception as ex:
    print(" invaild input ", ex)


#Example of exeption with more than one except block
print("Example of exeption with more than one except block ")
def calculation():
    c =  int(input(" enter a number "))
    d = int(input("enter the second number "))
    if c<d:

        result = (c+d)/(c-d)
    print("result = ",result)


try:
    calculation()
except ZeroDivisionError:
    print("denomintor will become zero ")
except Exception as e :
    print(" invaid input ",e )


#example of exception with else block
print("example of exception with else block")

c =  int(input(" enter a number "))
d = int(input("enter the second number "))
if c<d:
    try:
        result = (c + d) / (c - d)

    except ZeroDivisionError:
        print("denomintor should not be  zero ")

    else:
        print(result)
else:
    result = (c + d) / (c - d)
    print(result)





"""
Python provides a keyword finally, which is always executed after the try and except blocks. 
The final block always executes after normal termination of try block or after try block terminates due to some exception.
Syntax:

try:
    # Some Code.... 

except:
    # optional block
    # Handling of exception (if required)

else:
    # execute if no exception

finally:

"""
#example of exception with finally keyword :
print("example of exception with finally keyword :")
e =  int(input(" enter a number "))
f = int(input("enter the second number "))

try:
    result1 = (e + f) / (e - f)

except ZeroDivisionError:
    print("denomintor should not be  zero ")

else:
    print(result1)
finally:
    print("calculation is done successfully")



