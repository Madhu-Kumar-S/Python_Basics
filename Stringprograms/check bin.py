# Python | Check if a given string is binary string or not

s = input("enter a string:")

t = {'0','1'}

t1 = []

for i in s:
    if i in t:
        t1.append(True)
    else:
        t1.append(False)

if all(t1):
    print("given string is binary")
else:
    print("given string is not binary")
