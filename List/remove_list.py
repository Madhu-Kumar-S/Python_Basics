# Remove multiple elements from a list in Python

lst = [1, 2, 3, 4, 5]

t = lst.copy()

print("enter elements to remove from the list")
r = [int(x) for x in input().split()]

for i in r:
    for j in t:
        if i == j:
            t.remove(i)

print("new list after deleting elements is = {}".format(t))

