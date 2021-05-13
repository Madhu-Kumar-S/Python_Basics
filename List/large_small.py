# python program to find largest and smallest no in list
l = []

n = int(input("enter how many elements:"))

for i in range(n):
    e = int(input("enter an elemnt:"))
    l.append(e)
print(l)

def large(a):
    big = 0
    for i in range(n):
        if a[i] > big:
            big = a[i]
    return big

def small(a):
    smal = a[0]
    for i in range(1, n):
        if a[i] < smal:
            smal = a[i]
    return smal

print("largest number in list is {}".format(large(l)))

print("smallest number in list is {}".format(small(l)))