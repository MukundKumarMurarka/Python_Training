import pandas as pd

"""
Pandas :- Pandas is a Python library used for working with data sets.
It has functions for analyzing, cleaning, exploring, and manipulating data.
The name "Pandas" has a reference to both "Panel Data", and "Python Data Analysis" and was created by Wes McKinney in 2008
Pandas allows us to analyze big data and make conclusions based on statistical theories.
pandas can merge or join two different data sets eaasily.
working with panda firstly we have to install panda in our system and import the module of panda in our program.
 we can import panda simply by syntax import panda 
 or we can can import it using alias name example     import panda as pd    here pd is the alias name 
pandas work on mainly e types of data structure  

1. series :- A Pandas Series is like a column in a table.
It is a one-dimensional array holding data of any type.
"""

print("1. example of panda by using list ", end="")
list1 = [10, 20, 30, 45, 56]
series = pd.Series(list1)  # this will create a series
print("print list by using series in panda : ")
print(series)

"""
whwn we execute the avove code it will print the list in tabular format and by default start the indexing by 0
we can also change the indexing of series .. for example :  
"""

series1 = pd.Series(list1, ["a", "b", "c", "d", "e"])
print("print series after changing the index format :  ")
print(series1)

# key/value objects as a series
# we also crete a series with key value pair just like dictionary :
dic = {"krishna": 65, "nitish": 45, "rahul": 64, "pankaj": 98}
dict = pd.Series(dic)
print(" print the didtionary i the series format : ")
print(dict)

"""
Accessing Elements of a Series
There are two common ways for accessing the elements
of a series: Indexing and Slicing.
"""
# example of accessing an element using indexing
print("Accesing an element of series by using index number : ")
print(series[1])

# in dictinary lavel is specified by key value
# if we want to acess some value in the dictionary then we have to specifies the key value
dic1 = pd.Series(dic, ["krishna", "rahul"])
print(dic1)

# sliecing in series :

print("Sliecing in series  : ")
print(series[1:3])  # this will include the value on index number 1 and exclude the value of index number 3

# sliecing in dictionary in series
print("sliecing in dictionary : ")
print(dict[0:2])

# method of series
"""
head(n) :- Returns the first n members of the series. If
the value for n is not passed, then by default
n takes 5 and the first five members are
displayed.

count() Returns the number of non-NaN values in
the Series

tail(n) Returns the last n members of the series. If
the value for n is not passed, then by default
n takes 5 and the last five members are
displayed.
"""
# head()
print("by default value ")
print(series.head())
print("first two rows in series ")
print(series.head(2))
print(dict.head(2))


#count()
print("print number of element in series : ")
print(series.count())



#Adition of two series by using + operator as well as add() and a parameter fill_value to
#replace missing value with a specified value

list2 = [11, 12, 13, 14, 15]
list3 = [16, 17, 18, 19,20 ]
print("Adding two series by simply + operator : ")
print(pd.Series(list2) + pd.Series(list3))

print(" adding two values by Addition method add() : ")
print(pd.Series(list2).add(pd.Series(list3),fill_value =0))


#now change indexing of both new list
series2 = pd.Series(list2,["a", "b", "c", "d", "e"])
series3 = pd.Series(list3,["c", "d", "e", "f","g"])
print(" adding both series again by using + operator ")
print(series2 + series3)
print("Adding both series again using add() method : ")
print(series2.add(series3, fill_value =0))