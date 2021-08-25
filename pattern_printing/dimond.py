n = int(input("Enter limit:"))
s = n
for i in range(1, n+1):
    print(" " * s, end=' ')
    print("* "*i)
    s = s-1

s = s+2

for i in range(n-1, 0, -1):
    print(" " * s, end=' ')
    print("* "*i)
    s = s+1
