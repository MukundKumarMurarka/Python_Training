#CONDITIONAL STATEMNT, LOOPING STATEMENT, OPERATORS IN PYTHON

#IF STATEMENT, ELIF STATEMENT, IF ELSE STATEMENT
#IF STATEMENT is executed when the condition is true
# for example check between a and b which is greater
a=10
b=5
if a>b: #check condition is true or false
    print(a) # conditionn is true the if lock is executed

#if else statement :- else statement is executed when the condition is false
#for example check which one is larger between c and d
c=15
d=17
if c>d:
    print(c, " is larger")
else:
    print(d," is larger")


# elif :- elif statement is used when ther is need of more then one if else statement
#for example chevk which one larger among three number
e=12
f=13
g=18
if(e>f and e>g):
    print(e,"is larger among three number")
elif(f>e and f>g):
    print(f,"is larger among three number")
else:
    print(g,"is larger among three number")


#Nestes if :- Nested if means that if inside the if block
#for example:- first check a number is even or odd if number is even then check it is greater then 5 or not
h=8
if (h%2==0):
    print(h," is even number")
    if(h>=5):
        print("yes",h," is greater then 5")
    else:
        print("no", h, " is not greater then 5")
else:
    print(h," is odd number")





#LOOPING STATEMENT IN PYTHON
#FOR LOOP IN PYTHON
# A for loop is used for iterating over a sequence
#With the for loop we can execute a set of statements once for each tem ina list,set tuple, set etc
# for example :- print 1 to 10 number by using for loop

for i in range(10):
    print(i,end=" ")
print(" ")

#if statement inside for loop
# for example print the value from 1 to 20 which is not divisible by 5
for i in range(20):
    if(i%5!=0):
        print(i, end=" ")
print(" ")

# while loop :- this loop is as same as for loop the basic deffrence is that in while loop initialization, condition check
#and increment all is done manually but in for loop all is done automatically

i =0 #initialization of i
while i<=10:  #condition check
    print(i,end=" ")
    i=i+1   #incrimenting of i
print(" ")
#while loop with if statment
j=0
while j<=20:
    if(j%5!=0):
        print(j, end=" ")
    j=j+1
print(" ")

# OPERATORS:- Operators are used to perform operations on variables and values.
#              operator is type of operation which is happend on variable
#               variable on which operation is done is called operand
#               whole the process is know as operation.
# Python divides the operators in the following groups:
# # Arithmetic operators:- All the mathematical orerator is comes under Arithmetic operator
#                           fir examole :- +(Addition),-(substraction),*(Multiplication),%(Modulas),/(devide),//(floor) ,**(square)
h=10
k=3
print(h+k) # Addition operator
print(h-k) #Substraction operator
print(h*k)  #multiplication operator
print(h/k)  #divide operator
print(h//k)  #floor operator
print(h%k)    #modulas operator


# # Assignment operators:- Assignment operators are used to assign values to variables:
# =	    x = 5	x = 5	 Assign 5 to x
# +=	x += 3	x = x + 3 add 3 in x
# -=	x -= 3	x = x - 3	substract 3 in x
# *=	x *= 3	x = x * 3	multiply 3 in x
# /=	x /= 3	x = x / 3	divide x by 3
# %=	x %= 3	x = x % 3	find modulas of x by 3
# //=	x //= 3	x = x // 3	floor x by 3
# **=	x **= 3	x = x ** 3	taking cube root of x
# &=	x &= 3	x = x & 3	fing AND of x with 3
# |=	x |= 3	x = x | 3	finding OR of x with 3
# ^=	x ^= 3	x = x ^ 3	finding XOR of x withh 3
# >>=	x >>= 3	x = x >> 3	 finding left shift of x by 3
# <<=	x <<= 3	x = x << 3    finding right shift of x by 3

x=5
print(x)
x = x+5
print(x)
x=x-3
print(x)
x=x*3
print(x)
x=x/3
print(x)
x=x%3
print(x)
x=x//3
print(x)
x=x**3
print(x)
x=x&3
print(x)
x=x|3
print(x)
x=x^3
print(x)
x=x<<3
print(x)
x=x>>3
print(x)

# # Comparison operators :- This operator is used to compair two variables:
# ==	Equal	x == y
# !=	Not equal	x != y
# >	Greater than	x > y
# <	Less than	x < y
# >=	Greater than or equal to	x >= y
# <=	Less than or equal to	x <= y
#for example
l=14
m=19
if(l==m):
    print("both are equal")
if(l!=m):
    print("both are not equal")
if(l>=m):
    print(l,"is greater than ", m)
if(l<=m):
    print(l," is less than ", m)


# # Logical operators:- Logical operators are used to combine conditional statements:
# and 	Returns True if both statements are true	x < 5 and  x < 10
# or	Returns True if one of the statements is true	x < 5 or x < 4
# not	Reverse the result, returns False if the result is true	not(x < 5 and x < 10)


# # Identity operators:-Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:
# is 	Returns True if both variables are the same object	x is y
# is not	Returns True if both variables are not the same object	x is not y


# # Membership operators:- Membership operators are used to test if a sequence is presented in an object:
# in 	Returns True if a sequence with the specified value is present in the object	x in y
# not in	Returns True if a sequence with the specified value is not present in the object	x not in y



# # Bitwise operators:- Bitwise operators are used to compare (binary) numbers
# & 	AND	Sets each bit to 1 if both bits are 1
# |	OR	Sets each bit to 1 if one of two bits is 1
#  ^	XOR	Sets each bit to 1 if only one of two bits is 1
# ~ 	NOT	Inverts all the bits
# <<	Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	Signed right shift	Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off