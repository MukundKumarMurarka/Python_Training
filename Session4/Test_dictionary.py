# 5. WAP to sort (ascending and descending) a dictionary by value.
# 7. WAP to test value of a dictionary in a given range.
def test_dict(mobile_price):
    i = int(input("enter the starting range"))
    j = int(input("enter the ending point"))
    res = dict()
    for key, val in mobile_price.items():
        if int(val) >= i and int(val) <= j:
            res[key] = val
    print("short dictionary : " + str(res))

mobile_price={"motorala":19,"samsung":8,"oneplus":12,"iphone": 20,"realme" :13}
print("print original dictionary : ",str(mobile_price))
test_dict(mobile_price)

