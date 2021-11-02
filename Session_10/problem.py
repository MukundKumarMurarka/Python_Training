import pandas as pd

data = {"a": [1, 2, 3, 4, 5],
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
even_data = data_even[2: :2]


print(even_data)
newdata= data1.replace(even_data, "Nan")
print(newdata)