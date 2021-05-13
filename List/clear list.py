# Different ways to clear a list in Python

print("Diff ways to clear a list")

def m1(l):
    print("method 1 using clea() method")
    l.clear()
    print(l)

def m2(l):
    print("method 2 using Naive method")

    for i in range(len(l)):
        l.pop()

    print(l)

l = [1, 2, 3, 4, 5]
print("befor clearing")
print(l)
print("after clearing")
m1(l)
m2(l)