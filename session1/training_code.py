# Write a code in python to determine a year is leap eyar not not ;

year = int(input("enter the year"))
if (year %4 ==0):
    if (year %100==0):
        if(year %400 ==0):
            print(year ," is a leap year")
        else:
            print(year ," is not a leap year")
    else:
        print(year ," is a leap year")
else:
    print(year ," is not a leap year")


# WAP to display the smallest amongst three number

number1 = int(input("enter first number"))
number2 = int(input("enter second number"))
number3 = int(input("enter third number"))

if(number1 < number2 and number1 < number3):
    print("smallest number is " , number1)
elif(number2 < number1 and number2 < number3 ):
    print("smallest number is ", number2)
else:
    print("smallest number is ", number3)


# WAP to check given  number is armstrong or not
num = int(input("enter a number"))
length = len(str(num))
sum =0
temp = num
while temp>0:
    digits = temp % 10
    sum = sum + (digits ** length)
    temp //=10
if(num == sum):
    print(num ," is a armstrong number")
else:
    print(num,"is not a armstrong number")

# WAP tp print multipliaction table
n1 = int(input("enter a number"))
start_range=int(input("enter the start range"))
range_num = int(input("enter range of multiplication"))
for i in range(start_range,range_num+1):
    n2 = n1*i
    print(n1,"*",i ,n2)

# WAP to reverse a number using while loop
num1 =  int(input("enter a number "))
rev_num=0
while num1 !=0:
    rem = num1 %10
    rev_num = rev_num*10 +rem
    num1 //=10
print("reversed number is ",rev_num)

# WAP to display fibonaci series upto given terms
given_num=int(input("enter the range of series"))
n1=0
n2=1
sum=0
count =1
if(given_num<0):
    print("enter a positive number")
elif(given_num==1):
    print("fibonaci series upto 1 term is :",n1)
else:
    print("fibonaci series upto given term is :", end=" ")
    while(count <=given_num):
        print(sum,end=" ")
        count = count+1
        n1=n2
        n2=sum
        sum = n1+n2

# WAP to calculate the cube of all the numner to a givn number
given_num = int(input("enter the number "))
for i in range (1,given_num+1):
    cube = i**3
    print(cube)


#WAP to remove all the integers from a string

import re
string1 = input("enter a string")
patr = r'[0-9]'
new_str = re.sub(patr,"",string1)
print(new_str)