# Python program to create a list of tuples from given list having number and its cube in each tuple

l1 = [1, 2, 3, 4, 5]
l2 = []

for i in l1:
    s = int((pow(i,3)))
    l2.append(s)

d = list(zip(l1,l2))
print(d)

# creating a list
list1 = [1, 2, 5, 6]

# using list comprehension to iterate each
# values in list and create a tuple as specified
res = [(val, pow(val, 3)) for val in list1]

# print the result
print(res)

l = [1, 2, 3, 4, 5]

r = [ {i:[pow(i,3)]} for i in l]

print(r)