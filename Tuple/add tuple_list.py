# Python – Adding Tuple to List and vice – versa

# tuple to list
l = [1, 2, 3]
t = (4, 5)
res =l + list(t)
print(res)

# another way using assignment operator
l += t
print(l)

# list to tuple
tup = tuple(list((1, 2)) + [3, 4, 5])

print(tup)