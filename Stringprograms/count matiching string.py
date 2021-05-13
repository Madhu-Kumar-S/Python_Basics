# Python | Count the Number of matching characters in a pair of string

s1 = input("enter 1st string:")

s2 = input("enter 2nd string:")

print("method 1")

l = []

for i in s1:
    for j in s2:
        if i == j:
            l.append(i)

print("there are {:d} matching char in {:s} and {:s}\nthey are:".format(len(l), s1, s2))

s = set(l)
s = sorted(s)
for i in s:
    print(i, end=' ')

print("\nmethod 2")
k = 0
for i in s1:
    if s2.find(i) != -1:
        print(i, end=' ')
        k = k+1

print("\n there are {:d} matching characters".format(k))
