a = int(input("Enter a num to check if it is prime or not:"))

c = True

for i in range(2, a):
    if a % i == 0:
        c = False

if c == 0:
    print("prime")
else:
    print("not prime")

