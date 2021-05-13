# Python | Remove empty tuples from a list

l = [1, 2, (), 4, (), 5]
print("original list is",l)

print("after removing empty tuples from list: ",list(filter(lambda x: x!=(), l)))