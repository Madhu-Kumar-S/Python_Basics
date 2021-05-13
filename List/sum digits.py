# Python | Sum of number digits in List

l = [12, 67, 98, 34]
print("original list is ", l)

sd1 = []

for i in l:
    s = str(i)
    ci = 0
    for j in s:
        ci = ci + int(j)
    sd1.append(ci)

print("sum of number digits in list is :", sd1)

