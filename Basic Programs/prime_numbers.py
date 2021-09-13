# Prime numbers till certain range

low = int(input("Enter lower limit: "))
high = int(input("Enter upper limit: "))
print()

print("Prime number from {:d} to {:d} are: ".format(low, high))

for i in range(low, high+1):
    c = 0
    for j in range(2, i):
        if i % j == 0:
            c = 1
            break
    if c == 0:  # else can use for - else loop
        print(i)
