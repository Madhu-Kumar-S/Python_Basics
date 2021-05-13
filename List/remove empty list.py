# Python – Remove empty List from List

lst = [1, 2, [], 3, [], 4, 5]
print("original list is {}".format(lst))

print("method 1 using Naive method")
l1 = [1, 2, [], 3, [], 4, 5]
for i in l1:
    if i == []:
        l1.remove(i)

print("after removing empty list, new list is {}".format(l1))
print()

print("method 2 using list comprehenshion")
l2 = [1, 2, [], 3, [], 4, 5]
print("after removing empty list, new list is {}".format([res for res in l2 if res != []]))
print()

print("method 3 using filter() method")
l3 = [1, 2, [], 3, [], 4, 5]
print("list after removing empty list is:",list(filter(None, l3)))
print()

print("method 4 using filter() method with lambda")
l4 = [1, 2, [], 3, [], 4, 5]
print("list after removing empty list is:",list(filter(lambda x: x!=[], l4)))

