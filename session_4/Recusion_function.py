#Recusion :- it is a process in which a function calls itself directly or indirectly.
#Advantages :- A complicated function can be split down into smaller sub-problems utilizing recursion.
#               Sequence creation is simpler through recursion than utilizing any nested iteration.
#Disadvantages :-A lot of memory and time is taken through recursive calls which makes it expensive for use.
#               The reasoning behind recursion can sometimes be tough to think through.


#WAP to find Factorial of a number using recursion
def factorial_fun(num):
    if num <=0 :
        print("invailed input")
    if (num ==1 ):
        return 1
    return num*factorial_fun(num-1)
number = int(input("enter number "))
print("factorial using recursion ", factorial_fun(number))

#Factorial of a funtion without using recursion
def fact_func(num1):
    if num1 <=0 :
        print("invailed input")
    if num1==1:
        return 1
    fact =1
    for i in range(1,num1):
        fact=fact*(i+1)
    print(fact)
fact_func(4)