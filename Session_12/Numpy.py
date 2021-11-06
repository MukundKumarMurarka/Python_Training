"""
NumPy is a Python library used for working with arrays.

It also has functions for working in domain of linear algebra, fourier transform, and matrices.

NumPy stands for Numerical Python.

Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.

NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.

The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.

Arrays are very frequently used in data science, where speed and resources are very important.

NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.

This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.

NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.
"""

import numpy  # we have to import the module of numpy we can import it as a object name like import numpy as np
print(numpy.__version__)  # this shows version of numpy
print("\n")


#$creating an empty array
emparr= numpy.array([])
print(emparr)

# example of numpy
import numpy as np
arr = np.array((1,2,3,4,56,6))    # creating an array using tuple
print(arr)

print(type(arr))


#example 2 creating string array by using string
#formiter():-  this method is usefull for creating non numeric sequence type array however it can create any type of
# array. Here we will convert a string into numpy array
str = "krishnanand roy"

str_arr =np.fromiter(str, dtype="U2")
print(str_arr)


# filter an array
# create a new array with existing array which contains only even number
existingarray = np.arange(20)
print("\n original array \n ",existingarray)
newarr = []
for element in existingarray:
    if element % 2==0:
        newarr.append((element))
filter_arr =  existingarray[newarr]
print(filter_arr)

