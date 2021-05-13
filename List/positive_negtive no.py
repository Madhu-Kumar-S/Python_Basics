# Python program to print positive and negative numbers in a list

def p_n(l):
    p = []
    n = []
    for i in l:
        if i > 0:
            p.append(i)
        elif i < 0:
            n.append(i)

    return p, n



lst = eval(input("enter a list:"))
print("positive and negative numbers in a list")

p1, n1 = p_n(lst)

print("positive no's in list are:")
for i in p1:
    print(i, end=' ')
print()
print("negative no's in list are:")
for i in n1:
    print(i, end=' ')

print("\n.........................................................")
print("positive and negative numbers in a range")

start = int(input("enter starting no of the range:"))

end = int(input("enter ending no of the range:"))

p2 = []
n2 = []

for i in range(start,end+1):
    if i > 0:
        p2.append(i)
    elif i < 0:
        n2.append(i)

print("positive no's in range are:")
for i in p2:
    print(i, end=' ')
print()
print("negative no's in range are:")
for i in n2:
    print(i, end=' ')