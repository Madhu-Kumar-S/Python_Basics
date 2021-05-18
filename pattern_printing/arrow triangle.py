# python pgm to print arrow triamgle
r = 5
c = 5
for i in range(r):
    for j in range(i+1):
        print("*", end=' ')
    print()

print("* " * (r+1))
for i in range(r):
    for j in range(c):
        print("*", end=' ')
    print()
    c = c - 1