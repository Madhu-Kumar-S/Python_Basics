# program on set method
s = {1, 2, 2, 2.2, "hello"}
print(*s)

# add element
s.add(3)
print(s)

# remove 1st element
s.pop()
print(s)
s.pop()
print(s)

ss = {1, 2, 3}
# returns union of of two sets
ns = s.union(ss)
print(ns)

ss = {1, 2, 3}
# returns intersection of of two sets
ns = s.intersection(ss)
print(ns)

s1 = {1, 2, 3, 4}
s2 = {1, 2}
print(s2.issubset(s2))
print(s1.issuperset(s2))

# to add and remove element
s = {1, 2, 3, 4}
s.update([4,5])
print(s)
s.remove(5)
print(s)

# to clear set
s.clear()
print(s)
del(s)


