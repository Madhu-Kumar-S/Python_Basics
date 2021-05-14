# Python program to sort a list of tuples by second Item

l = [('for', 24), ('Geeks', 8), ('Geeks', 30)]

res1 = sorted(l, key=lambda x: x[1])

print(res1)

e =[('452', 10), ('256', 5), ('100', 20), ('135', 15)]

res2 = sorted(e, key=lambda x: x[1])

print(res2)