# 3. WAP to Reverse List.

def reverse_list(names):
    new_list = names[::-1]
    print("reversed list : ",new_list)
n= int(input("enter the length of list : "))
names =[x for x in input("enter the element of list : ").split()]
print("original list : ",names)
reverse_list(names)