# 2. WAP to find the minimum and maximum of a list

def min_max(marks):
    min_marks = min(marks)
    max_marks = max(marks)
    print("minimum marks of list : ",min_marks)
    print("maximum marks of list : ",max_marks)

n =  int(input("enter length of list : "))
marks = [x for x in input( "enter the marks  : " ).split()]
print("original marks list : " ,marks)
min_max(marks)