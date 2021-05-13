# Python program to print even  and odd numbers in a list

def eve_odd(l):
    e = []
    o = []
    for i in l:
        if i % 2 == 0:
            e.append(i)
        else:
            o.append(i)

    return e, o



lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("even  and odd numbers in a list")

even, odd = eve_odd(lst)

print("even no in list are:")
for i in even:
    print(i, end=' ')
print()
print("odd no in list are:")
for i in odd:
    print(i, end=' ')
print()

print(".........................................................")
print("even  and odd numbers in a range")

start = int(input("enter starting no of the range:"))

end = int(input("enter ending no of the range:"))

e1 = []
o1 = []

for i in range(start,end+1):
    if i % 2 == 0:
        e1.append(i)
    else:
        o1.append(i)

print("even no in range are:")
for i in e1:
    print(i, end=' ')
print()
print("odd no in range are:")
for i in o1:
    print(i, end=' ')
print()

print(".........................................................")
print("even no's are:")
nl1 = list(filter(lambda x: (x%2 == 0),lst))
for i in nl1:
    print(i, end=' ')
print("\nodd no's are:")
nl2 = list(filter(lambda x: (x%2 != 0),lst))
for i in nl2:
    print(i, end=' ')



