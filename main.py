import array
l = [1, 2, 3, 4, 5]
a = array.array('i', l)
print(*a)

b = array.array('u', ['a', 'b'])
print(*b)

c = array.array(a.typecode, [i for i in a])
print(*c)
print(type(a), type(b), type(c), end=' ')
print()
a[0] = 3
print(*a)
print(a[0])
i = 0
while i < len(a):
    print(a[i], end=' ')
    i += 1

