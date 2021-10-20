# 6. WAP to iterate over a dictionary using for loop
def iterate_dict(mobile):

    for i, j in mobile.items():
        print(i, j)


mobile={"rahul":"iphone", "john":"motorola", "peter":"ineplus","shyam":"samsung"}
iterate_dict(mobile)