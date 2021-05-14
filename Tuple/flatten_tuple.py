# Python – Flatten tuple of List to tuple

t = ([5], [6], [3], [8])

print(tuple((j for i in t for j in i)))

l = [1, 2, 3]

