# Python | Ways to check if element exists in list

print("Diff ways to check if the element exists in list")

def m1(l, e):
    print("method 1 using in operator")
    if e in l:
        print("{} is in list {}".format(e,l))
    else:
        print("{} is not in list {}".format(e, l))

def m2(l, e):
    print("method 2 using Naive method")

    for i in l:
        if e == i:
            print("{} is in list {}".format(e, l))
            break
    else:
        print("{} is not in list {}".format(e, l))




l = [1, 2, 3, 4, 5]

e = int(input("enter an element to find if it is in list or not:"))

m1(l, e)
m2(l, e)