# Python program to find uncommon words from two Strings

s1 = "Hi welcome to python"

s2 = "python is powerful programming language"

for i in s1.split(' '):
    if i in s2.split(' '):
        pass
    else:
        print(i)


for j in s2.split(' '):
    if j in s1.split(' '):
        pass
    else:
        print(j)