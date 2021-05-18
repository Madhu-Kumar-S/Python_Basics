# Python pgm to print upside down right angle triangle
r = 5
c = 5
for i in range(r):
    for j in range(c):
        print("*", end=' ')
    print()
    c = c - 1