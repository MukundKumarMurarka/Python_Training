import pandas as pd
import datetime as dt

"""
In this module of Pandas, we can include the date and time for every record and can fetch the records of dataframe.
We can find out the data within a certain range of date and time by using pandas module named Time series

"""

# Creating  date and time series

creat_series = pd.date_range(start="1/01/2021", end="31/10/2021", freq="5H")
print(creat_series)
print("\n")

# in this code we create a time series at intervel of 5 hour.
print("print type of the series : ")
print(type(creat_series))
print("\n")


"""
we can also convert the avobe series in the dataframe. 
"""
print("convert the above series in the data frame and print the data frame : ")
df= pd.DataFrame(creat_series,columns=["Date"])
print(df.head(10))
print("\n")

"""
some features of data time 
pandas.Series.dt.year returns the year of the date time.
pandas.Series.dt.month returns the month of the date time.
pandas.Series.dt.day returns the day of the date time.
pandas.Series.dt.hour returns the hour of the date time.
pandas.Series.dt.minute returns the minute of the date time.
"""

print(" print dataframme in year month day and time : ")
df[:8]
df['year'] = df['Date'].dt.year
df['month'] = df['Date'].dt.month
df['day'] = df['Date'].dt.day
df['hour'] = df['Date'].dt.hour
df['minute'] = df['Date'].dt.minute
# df["week"] = df["Date"].dt.week
df["dayofweek"] = df["Date"].dt.dayofweek
df["is_leap_year"] = df["Date"].dt.is_leap_year
print(df.head(10))
print("\n")

"""
Note that Pandas dt.dayofweek attribute returns the day of the week and it is assumed the week starts on Monday,
 which is denoted by 0 and ends on Sunday which is denoted by 6. 
 To replace the number with full name, we can create a mapping and pass it to map() :

df['day_of_week_name']=df['DoB'].dt.weekday.map(dw_mapping)
df
"""
print("the name of day in the series  : ")
dw_mapping={
    0: 'Monday',
    1: 'Tuesday',
    2: 'Wednesday',
    3: 'Thursday',
    4: 'Friday',
    5: 'Saturday',
    6: 'Sunday'
}
df["day_of_week_name"]=df["Date"].dt.weekday.map(dw_mapping)
print(df.head(10))
print("\n")




# timestamp() :- this method is used to fetch the current time :
print("print current time and then convert it into datetime ")
curtime = pd.Timestamp.now()
print(curtime)
#convert this current time into datetime
curtime.to_datetime64()
print(curtime.year)
print(curtime.month)
print(curtime.day)
print(curtime.hour)

# we can also the date class type to  string class

print(" convert some date in string format and print ")
string_data = [str(x) for x in creat_series]
print(string_data[1:11])  # print  only 10 data form series starting from index 1 to 10

print("\n")


"""
Convert strings to datetime
Pandas has a built-in function called to_datetime() that can be used to convert strings to datetime. Let’s take a look at some examples
With default arguments
Pandas to_datetime() is able to parse any valid date string to datetime without any additional arguments. For example:

"""

df2 = pd.DataFrame({'date': ['3/1/2000', '3/2/2000', '3/3/2000','3/4/2000','3/5/2000','3/6/2000','3/7/2000','3/8/2000'],
                   'value': [2, 3, 4,5,6,7,8,9]})
print("print the type of date before converting it into datetime")
print(df2.dtypes)
df2['date'] = pd.to_datetime(df2['date'])
print("print the type of date after converting it into datetime ")

print(df2.dtypes)
print(df2)
print("\n")

"""
By default, to_datetime() will parse string with month first (MM/DD, MM DD, or MM-DD) format,
and this arrangement is relatively unique in the United State.
In most of the rest of the world, the day is written first (DD/MM, DD MM, or DD-MM). 
If you would like Pandas to consider day first instead of month, you can set the argument dayfirst to True.
"""
print(" print day first then month ")
df3 = pd.DataFrame({'date': ['3/1/2000', '3/2/2000', '3/3/2000','3/4/2000','3/5/2000','3/6/2000','3/7/2000','3/8/2000'],
                   'value': [2, 3, 4,5,6,7,8,9]})
df3['date'] = pd.to_datetime(df3['date'],dayfirst=True)
print(df3)
print("\n")

"""
Custome format
By default, strings are parsed using the Pandas built-in parser from dateutil.parser.parse. Sometimes, your strings might be in a custom format, for example, YYYY-DD-MM HH:MM:SS. Pandas to_datetime() has an argument called format that allows you to pass a custom format:

df['date'] = pd.to_datetime(df['date'], format="%Y-%d-%m %H:%M:%S")
df
"""




"""
Speed up parsing with infer_datetime_format
Passing infer_datetime_format=True can often speed up a parsing if its not an ISO8601 format exactly but in a regular format. 

"""


