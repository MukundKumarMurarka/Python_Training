# 1. Python program to interchange first and last elements in a list.
list = [11,13,15,"john","peater","banana"]
print("print original list", list)
list[0] , list[len(list)-1] = list[len(list)-1] , list[0]
print("print list after interchange", list)


# 2. WAP to find the minimum and maximum of a list
list1 = [16,18,15,17,20]
print("print minimum element of list", min(list1))
print("print maximum of element of list ",max(list1))


# 3. WAP to Reverse List.
fruits =["banana", "mango","cherry","guava","papaya"]
print("print original list", fruits)
rev_fruits= reversed(fruits)
print("reversed list ")
for x in rev_fruits:
    print(x,end=" ") #


# 4. WAP to print duplicates from a list of integers
bike=["bmw","ktm","pulser","splender","bmw", "pulser"]
dup_list=[]
for i in range (len(bike)):
    k=i+1
    for j in range(k,len(bike)):
        if bike[i] == bike[j] and bike[i] not in dup_list:
            dup_list.append(bike[i])
print("Reversed list ",dup_list)


# 5. WAP to sort (ascending and descending) a dictionary by value.



# 6. WAP to iterate over a dictionary using for loop
mobile={"rahul":"iphone", "john":"motorola", "peter":"ineplus","shyam":"samsung"}
#using loop for iterating keys and value
for i, j in mobile.items():
    print(i, j)


# 7. WAP to test value of a dictionary in a given range.
mobile_price={"motorala":19,"samsung":8,"oneplus":12,"iphone": 20,"realme" :13}
print(str(mobile_price))
# initialize the range which we have to test
i = int(input("enter the starting range"))
j =int(input("enter the ending point"))

#using loops to iterate through all the elements
res = dict()
for key, val in mobile_price.items():
    if int(val) >= i and int(val) <= j:
        res[key] = val

# printing result
print("short dictionary : " + str(res))