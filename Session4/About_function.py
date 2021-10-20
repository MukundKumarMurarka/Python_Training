#Function = function is block of codes and group of codes that can do a specific task.
#           when we use a particular task more than one time in the project then we create a function that will
#           does that task and call this fuction again and again
#           There are two things in function
#           1.  defining the function. syntax  def function_name()
#           2.  calling a function     syntax  funtion_name()
# there are two types of function
# 1.  user defined function :- this function is created by user for doing a specific task.
#2.    Built in function :- this function is not createdby user, like help(), min(), count(). it is defaultly present in python
 #Argument is the value which we put in function at the time of function calling
 # return statement is returned by function

# Fuction with arguments and with return Statement
def add_sub(x,y):    #defining function with argument(x,y) called formal argument
    add = x+y
    subs = x-y
    return add, subs   # retun rsult after addintion and substraction
add_result, subs_result = add_sub(5,4)
print(add_result,subs_result)

#Function with argument and without return value
def add(x,y):
    sum = x+y
    print(sum)
add(6,3)


#Function without argument and with return value
def multiply():  #defining function without argument
    a=18
    b=6
    product = a*b
    return product
print(multiply())

#function without argument and without return function
def addition():
    c=10
    d=19
    result = c+d
    print(result)
addition()
