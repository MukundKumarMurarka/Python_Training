# Dictionary :- Dictionary stores the valus in key and values form.
#              Dictionary is mutable and does not support duplicate keys
#              This is writeen in curly bracket. syntax = dic ={ key_value: value }

# Creating a dictionary
pens = {"brand": "flair", "model": " write_o_meter", "price": 20}
print(pens)  # printing whole dictionary
print("printing whole dictionary ", pens.items())  # printing whole dictionary
print("printing only keys o dictionary ", pens.keys())  # printing only keys o dictionary
print("printing only values of dictionary ", pens.values())  # printing only values of dictionary
print("print value of particular key ", pens["model"])  # print value of particular key

# change  the exixting dictionary
pens = {"brand": "flair", "model": " write_o_meter", "price": 20,
        "country": "india"}  # this will change the exixting dictionary
print(pens)

print(pens.get("brand"))  # get()  method access the values of a particular key

# add new item in exixting dictonary
# pens["color"]="black"
pens.update({"color": "black"})
print("print ditionary after adding new item", pens)

# change the item in dictionary
pens["color"] = "blue"
print("print dictionary after change the valve of color key", pens.items())

# Traversing the dictionary
for i in pens:
    print("print the element of dictionary ", i, end=" ")

for x in pens.values():  # values() method prints only values of dictionary
    print("print only values", x, end="")

for x in pens.keys():  # keys() method prints only values of dictionary
    print("print only keys", x, end="")

# The pop() method removes the item with the specified key name
pens.pop("model")
print("print dictionary after removing model keys and value", pens)

pens.popitem()  # popitem() methods removes the last element of dictionary
print("print dictionary after removing last element", pens)

# Make a copy of a dictionary with the dict() function:
my_pens = dict(pens)
print("new copied list", my_pens)

# clear() methiod removes all the elements of dictionsry
my_pens.clear()
print("print dictionary after removing all the elements", my_pens)
