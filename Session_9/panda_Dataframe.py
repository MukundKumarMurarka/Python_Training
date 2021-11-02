import pandas as pd
#
# """
# Data sets in Pandas are usually multi-dimensional tables, called DataFrames.
# Series is like a column, a DataFrame is the whole table.
# A Pandas DataFrame is a 2 dimensional data structure, like a 2 dimensional array, or a table with rows and columns.
# """
#
#
# Example of panda bu using datafarme
print(" Example of panda bu using datafarme :  ")
dict1 ={"cars":["Bmw", "lamborgini", "mercidise", "maruti", "thar"],
        "milage":[10, 20, 30, 40, 50],
        "cost":[10000, 20000, 30000, 40000, 50000]
        }
df = pd.DataFrame(dict1)
#df.to_csv("cars.csv")  # to_csv method is used for creating a excel sheet in file manager

print(df)

# change the index value of data frame
# for there is index keyword in pandas dataframe
df2 = pd.DataFrame(dict1 , index=["a","b","c","d","e"])
print(" print dataframe after changing the indixing of dataframe : ")
print(df2)
#
# #Accessing element of dataframe using indexing number for this we have to use loc keyword

print("access row at index number 1 in data frame : ")
print(df.loc[[1]])

print("access row of index number 0 and 1 in databframe :  ")
print(df.loc[[0,1]])


#slicing of dataframe
print(df.loc[0:2])


# #to_csv and read_csv method.
# #to_csv method is used to create a file.
# #read_csv method is used to fetch a file
#
print(" Example of panda bu using datafarme :  ")
dict5 ={"cars":["Bmw", "lamborgini", "mercidise", "maruti", "thar"],
        "milage":[10, 20, 30, 40, 50],
        "cost":[10000, 20000, 30000, 40000, 50000]
        }
df4 = pd.DataFrame(dict5)
df4.to_csv("cars.csv")  # to_csv method is used for creating a excel sheet in file manager
df6=pd.read_csv("cars.csv")

print(df6.to_string())



