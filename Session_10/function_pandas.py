import pandas as pd

# more function  in pandas


# creating a dictionary
mobile = {"model_number": ["one fusion plus", "one plus nord", "redmi note 9", "realme 8", "iphone xr", "nokia 6",
                           "micromax A4", "oppo A17", "karbon 2", "iball 5"],
          "company": ["motorola", "one plus", "redmi", "realme", "apple", "nokia", "micromax", "oppo", "karbon",
                     "iball"],
          "cost": [15000, 28000, 12000, 16000, 55000, 13500, 6000, 18000, 1500, 3500]}

# convert it into dataframe
df_phone = pd.DataFrame(mobile)
df_phone.to_csv("phone.csv")  # careating a excel sheet
df_phone_data = pd.read_csv("phone.csv")  # read the csv file
print("print all the data available in phone.csv xcelsheet : ")
print(df_phone_data)


"""
Describe():- describe() is used to generate descriptive statistics of the data in a pandas  dataframe or series.
It summerizes as central tendency and dispersion of the datasheet 
"""
# descibe the data available in csv excel sheet
print("print discription of xcel sheet ")
print(df_phone.describe())

"""
head() :- head(n) is used to return the first n rows of datasheet 
By default head will return the first 5 roes of the datasheet  
"""

# head()
print("print wholw rows of datatsheet using head() method ")
print(df_phone.head(10))
print("print only 5 rows of datasheet : ")
print(df_phone.head())


"""
Memory_usage() :- memory_usege() return a panda series having the memory usages of each column in a panda dataframe 
by specifu=ying deep attribute is true we can get to know tthe actual space being taken by each column.
 
"""
print ("memoru usege by each column in datasheet ")
print(df_phone.memory_usage())

"""
loc[:] :- 6. loc[:]
loc[:] helps to access a group of rows and columns in a dataset, a slice of the dataset, as per our requirement. 
For instance, if we only want the last 2 rows and the first 3 columns of a dataset, we can access them with the help of loc[:]. 
We can also access rows and columns based on labels instead of row and column number.
"""

#slicing of datasheet by using loc
print("slicing of datasheet ")
print(df_phone.loc[0:4, ["company","cost"]])

"""
to_datetime()
to_datetime() converts a Python object to datetime format. 
It can take an integer, floating point number, list, Pandas Series, or Pandas DataFrame as argument. 
to_datetime() is very powerful when the dataset has time series values or dates.
syntax:- 
dataframe_object ['DOB'] = pd.to_datetime(data_1['DOB'])
"""


"""
sort_values()
sort_values() is used to sort column in a Pandas DataFrame (or a Pandas Series) by values in ascending or descending order.
 By specifying the inplace attribute as True
"""
print("sort all the data available in the data sheet : ")
sort_data=df_phone.sort_values(by="cost", inplace=False)
print(sort_data)


"""
Shape :-  The shape attribute of pandas.DataFrame stores the number of rows and columns as a tuple 
(number of rows, number of columns).
"""
print("number of rows and column in datasheet ")
print(df_phone.shape)

print(df_phone.shape[0])
print(df_phone.shape[1])

#t is also possible to unpack and store them in separate variables.
#Unpack a tuple / list in Python

row , column = df_phone.shape

print(row)
print(column)




"""
The total number of elements of pandas.DataFrame is stored in the size attribute. 
This is equal to the row_count * column_count.

print(df.size)
# 10692

print(df.shape[0] * df.shape[1])
# 10692
"""


print("size of datasheet : ")
print(df_phone.size)

print(df_phone.shape[0]*df_phone.shape[1])


""""
max  :- Pandas dataframe.max() function returns the maximum of the values in the given object.
 If the input is a series, the method will return a scalar which will be the maximum of the values in the series. 
 If the input is a dataframe, then the method will return a series with maximum of values over the specified axis in the dataframe. 
By default the axis is the index axis.
"""

print("maxium cost of datasheet : ")

print(df_phone.loc[:,"cost"])
print(df_phone.max(axis=0))
print("minimum cost of datasheet : ")
print(df_phone.min(axis=0))
print(df_phone["cost"].max())




"""
replace function is used to replace a string, regex,list, dictionary, series, number etc. from a dataframe.
Syntax = 
dataframe.replace(to_replace=none, value = None, inplace = false, limit= None, regex = False, method= "pad", axis = None
"""
print(" printing the new data : ")
print(df_phone.replace(to_replace="oppo", value=" xiomi "))


"""
Mask function :-  
Pandas dataframe.mask() function return an object of same shape as self and whose corresponding entries are from self where cond is False and otherwise are from other object.
The other object could be a scalar, series, dataframe or could be a callable. 
The mask method is an application of the if-then idiom.
For each element in the calling DataFrame, if cond is False the element is used; otherwise the corresponding element from the DataFrame other is used.
syntax: 
DataFrame.mask(cond, other=nan, inplace=False, axis=None, level=None, errors=’raise’, try_cast=False, raise_on_error=None)
"""

# importing pandas as pd
import pandas as pd

# Creating the dataframe

dict = {"A": [12, 4, 5, 44, 1],
        "B": [5, 2, 54, 3, 2],
       "C": [20, 16, 7, 3, 8],
       "D": [14, 3, 17, 2, 6]}
df = pd.DataFrame(dict)


print (df)
print("updated list : ")

print(df.mask(df > 10, 100))

