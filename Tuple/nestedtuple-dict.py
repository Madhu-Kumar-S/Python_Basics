# Python – Convert Nested Tuple to Custom Key Dictionary
print("method 1")
t = (('a', 1), ('b', 2), ('c', 3))
l = ['k', 'v']

d = [{l[0]:i[0], l[1]:i[1]} for i in t]

print(d)

print("method 2")
d = []

for i in t:
        t = {l[0]:i[0], l[1]:i[1]}
        d.append(t)

print(d)