#   There are two types of arguments in python
#       1. formal argument :- when a function is defined, it may have some parameters.
#                             These parameters are useful to receive values from outside of the function.
#                             They are called 'formal arguments'.
#       2. Actual arguments :- When we call the function, we should pass data or values to the function.
#                              These values are called 'actual arguments'.

# example of arguments
def sumation(x,y):      #x and y are formal argument
    sum_result=x+y
    print(sum_result)
sumation(5,3)         # 5 and 3 are actual argumens

# 1. Default :- Default arguments allow us to provide defaults for corresponding formal arguments in the function definition.
#               Python uses these defaults if corresponding actual arguments are not passed in the function call.
# examle of Default arguments in this example message is default argument.
def wishing(name, message="happy birthday to you"):
    wishes=(name,message)
    print(wishes)
wishing("krishna")


# 2. position :- position means that we pass the value in a particular series i.e in same way we define the arguments
   # example of position. in this example 5 assigns to x and 3 to y
def sumation(x,y):
    sum_result=x+y
    print(sum_result)
sumation(5,7)

# 3. keyword :- when we dont know the series in which the arguments define in the function definition,
                #then we use keyword like this
def sumation(x=5,y=9):   #here x and y are keyword whose value is 5 and 9 respectively
    sum_result=x-y
    print(sum_result)
sumation()              #at the time of calling we don't need to pass any value


# 4. variable length :-  variable length is used when we don't know how many arguments are required in function definition
#                        this can be  denoted as * sign
# variable length example
def sumation(a,b,c, *d):
    print("Sumation of position argument : " ,a+b+c)
    add =0
    for i in d:
        add= add+i
    print("Sumation of variable length : ",add)
sumation( 1,2,3,4,5,6,7,8)

