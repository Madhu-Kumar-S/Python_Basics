# Python program to print the star pattern in right tringle

# method 1

r = 5
for i in range(r):
    print("* " * i)

print("...................................")
# method 2

for i in range(r):
    for j in range(i+1):
        print("*", end=' ')
    print()