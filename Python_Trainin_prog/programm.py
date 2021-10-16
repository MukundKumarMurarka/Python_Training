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

if(number1 < number2 & number1 < number3):
    print("smallest number is " , number1)
elif(number2 < number1 & number2 < number3 ):
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
for i in range(1,11):
    n2 = n1*i
    print(n1,i,"ja",n2)

# WAP to reverse a number using while loop
num1 =  int(input("enter a number "))
rev_num=0
while num1 !=0:
    dig = num1 %10
    rev_num = rev_num*10 +dig
    num1 //=10
print("reversed number is ",rev_num)

