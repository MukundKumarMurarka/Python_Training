# 4. WAP to print duplicates from a list of integers

def dup_item(bike):
    dup_list=[]
    for i in range(len(bike)):
        j = i+1
        for h in range(j,len(bike)):
            if bike[i] == bike[h] and bike[i] not in dup_list:
                dup_list.append(bike[i])
    print("duplicate list:  ",dup_list)
n=int(input("enter the length of list : "))
bike = [x for x in input("enter element : ").split()]
print("original list : ",bike)
dup_item(bike)