# creating an array in numpy with basics details
# Python program to demonstrate
# basic array characteristics
import numpy as np

arr = np.array([[1, 2, 3],
                [4, 2, 5]])

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing array dimensions (axes)
print("No. of dimensions: ", arr.ndim)

# Printing shape of array
print("Shape of array: ", arr.shape)

# Printing size (total number of elements) of array
print("Size of array: ", arr.size)

# Printing type of elements in array
print("Array stores elements of type: ", arr.dtype)
print("\n")

# we can create a array in different ways in numpy like np.zeros, np.ones, np.full, np.empty, etc.


a = np.array([[3, 5, 6], [5, 9, 7]], dtype='float')  # Creating array from list with type float
print("Array created using passed list:\n", a)

b = np.array((1, 3, 2, 7, 8, 4))  # Creating array from tuple
print("\nArray created using passed tuple:\n", b)

c = np.zeros((3, 4))  # Creating a 3X4 array with all zeros
print("\nAn array initialized with all zeros:\n", c)

d = np.full((3, 3), 8, dtype='complex')  # Create a constant value array of complex type
print("\nAn array initialized with all 8s."
      "Array type is complex:\n", d)

e = np.random.random((3, 3))  # Create an array with random values
print("\nA random array:\n", e)

# Create a sequence of integers
# from 0 to 30 with steps of 5
f = np.arange(0, 54, 6)
print("\nA sequential array with steps of 6:\n", f)

# Create a sequence of 10 values in range 0 to 5
g = np.linspace(0, 5, 15)
print("\nA sequential array with 10 values between"
      "0 and 5:\n", g)

# Reshaping 3X4 array to 2X2X3 array
arr = np.array([[1, 2, 3, 4],
                [5, 2, 4, 2],
                [1, 2, 0, 1]])

newarr = arr.reshape(2, 2, 3)

print("\nOriginal array:\n", arr)
print("Reshaped array:\n", newarr)

# Flatten array
arr = np.array([[1, 2, 3], [4, 5, 6]])
flarr = arr.flatten()

print("\nOriginal array:\n", arr)
print("Fattened array:\n", flarr)

# Array slicing :- Just like lists in python, NumPy arrays can be sliced.
# As arrays can be multidimensional, you need to specify a slice for each dimension of the array.


arr1 = np.array([[1, 2, 3, 4], [-1, -5, -6, 5], [8, 7, 9, 4]])
print("\n original Array : \n", arr1)
slice_arr1 = arr1[:2, ::3]
print("\n print sliced array : \n", slice_arr1)

"""
Array Indexing: Knowing the basics of array indexing is important for analysing and manipulating the array object. 
NumPy offers many ways to do array indexing. 
  Integer array indexing: In this method, lists are passed for indexing for each dimension. 
  One to one mapping of corresponding elements is done to construct a new arbitrary array.
  """

index_array = arr1[[0, 1, 2], [2, 1, 0]]
print("\n print index of the array\n", index_array)

"""
Boolean array indexing: This method is used when we want to pick elements from array which satisfy some condition.
"""

cond = arr1 > 0  # cond is a boolean array
temp = arr1[cond]
print("\nElements greater than 0:\n", temp)

"""
sorting :-   Sorting refers to arranging data in a particular format. 
Sorting algorithm specifies the way to arrange data in a particular order. 
Most common orders are in numerical or lexicographical order. 
In Numpy, we can perform various sorting operations using the various functions that are provided in the library
 like sort, lexsort, argsort etc. 
"""

# example of sort
sorted_array = np.sort(arr1, axis=0)
print("\n print sorted array by column  \n", sorted_array)

sorted_array1 = np.sort(arr1, axis=-1)
print("\n print sorted array by rows  \n", sorted_array1)

sorted_array2 = np.sort(arr1, axis=None)
print("\n sort an array with none axis  \n", sorted_array2)

# example of sorted array according to argsort
# numpy.argsort() : This function returns the indices that would sort an array.

arr2 = np.array([15, 13, 14, 21, 16, 19, 5])
index_sort_array = np.argsort(arr2)
print("\n original array \n", arr2)
print("\n print sorted indices \n", index_sort_array)

# we can access the sorted array indices element
new_arr = np.zeros(len(index_sort_array), dtype=int)
for i in range(0, len(index_sort_array)):
    new_arr[i] = arr2[index_sort_array[i]]
print("\n sorted array \n ", new_arr)

# example of sorted array using
# numpy.lexsort() : This function returns an indirect stable sort using a sequence of keys.


"""
Searching :- 
Searching is an operation or a technique that helps finds the place of a given element or value in the list.
 In Numpy, we can perform various searching operations 
 using the various functions that are provided in the library like argmax, argmin, nanaargmax etc.

numpy.argmax() : This function returns indices of the max element of the array in a particular axis.
"""

# example of argmax searching
arr3 = np.arange(0, 100, 5).reshape(4,5)
print("\n print original array \n:  ",arr3)
# No axis mentioned, so works on entire array
print("\nMax element : ", np.argmax(arr3))

# returning Indices of the max element
# as per the indices
print(("\nIndices of Max element according to column  : "
       , np.argmax(arr3, axis=0)))

print(arr3[np.argmax(arr3,axis=0)])
print(("\nIndices of Max element according to rows : "
       , np.argmax(arr3, axis=1)))


# numpy.argmin() : This function returns the indices of the minimum values along an axis.
# example of argmin searching
arr4 = np.arange(0, 100, 5).reshape(4,5)
print("\n print original array \n:  ",arr4)
# No axis mentioned, so works on entire array
print("\n minimum element : ", np.argmin(arr4))

# returning Indices of the max element
# as per the indices
print(("\nIndices of min element according to column  : "
       , np.argmin(arr4, axis=0)))

print(arr3[np.argmin(arr4,axis=0)])
print(("\nIndices of Min element according to rows : "
       , np.argmin(arr4, axis=1)))


"""
nanaargmax
numpy.nanargmax() : This function returns indices of the max element of the array in a particular axis ignoring NaNs.
The results cannot be trusted if a slice contains only NaNs and Infs.
"""

array = [np.nan, 4, 2, 3, 1]
print("INPUT ARRAY 1 : \n", array)

array2 = np.array([[np.nan, 4], [1, 3]])

# returning Indices of the max element
# as per the indices ingnoring NaN
print(("\nIndices of max in array1 : "
       , np.nanargmax(array)))

# Working on 2D array
print("\nINPUT ARRAY 2 : \n", array2)
print(("\nIndices of max in array2 : "
       , np.nanargmax(array2)))

print(("\nIndices at axis 1 of array2 : "
       , np.nanargmax(array2, axis=1)))
