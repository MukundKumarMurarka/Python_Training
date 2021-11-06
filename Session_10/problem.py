import pandas as pd

data = {"a": [1, 5, 3, 4, 5],
        "b": [6, 7, 8, 9, 10],
        "c": [11, 12, 13, 14, 15],
        "d": [16, 17, 18, 19, 20],
        "e": [21, 22, 23, 24, 25],
        "f": [26, 27, 28, 29, 30],
        "g": [31, 32, 33, 34, 35],
        "h": [36, 37, 38, 39, 40],
        "i": [41, 42, 43, 44, 45],
        "j": [46, 47, 48, 49, 50]}
data1 = pd.DataFrame(data)
data_cpy = data1.to_csv("num_data.csv")

print(data1)

data_even = pd.read_csv("num_data.csv")

print(data_even.mask(data1%2==0 ,"Nan"))



"""
Drop function is used to drop a row column in  dataframe .
it is used to remove rows or columns by specifying labels names and corresponding axis, or by specifying directly index or column nmaes
syntax 
DataFrame.drop(self,labels=None, axis =0 ,index = None, lavel = none, inplace = False, errors="raise)
"""


print("new data after droping the data from datasheet : ")
print(data1.drop(columns=["i","j"]))