import pandas as pd
import datetime as dt

"""
now we read a external csv read and dod some operation on it.
"""

create_dataframe = pd.read_csv("/home/mukund/Downloads/timedata.csv")
print("print only first 10 rows of that data : ")
print(create_dataframe.head(10))
print("shape of that csv file : ")
print(create_dataframe.shape)
print("print size of that csv file ")
print(create_dataframe.size)
print("\n")

"""
when we access any csv file then in that csv file date  will store in the string  type class by defaultly 
for example  
"""
print(type("Date"))
print("\n")

"""
to_datetime() :- Pandas has a built-in function called to_datetime() that can be used to convert strings to datetime. 
Let’s take a look at some examples
"""

create_dataframe["Date"] = pd.to_datetime(create_dataframe["Date"])
print("print that csv after converting it into datetime : ")
print(create_dataframe.head(10))


"""
Day first format
By default, to_datetime() will parse string with month first (MM/DD, MM DD, or MM-DD) format, and this arrangement 
is relatively unique in the United State.
In most of the rest of the world, the day is written first (DD/MM, DD MM, or DD-MM). 
If you would like Pandas to consider day first instead of month, you can set the argument dayfirst to True.

"""

# create_dataframe