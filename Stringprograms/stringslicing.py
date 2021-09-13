# slicing in string and accessing in reverse manner
s = input("Enter a string:")
print(s)

for i in s:
    print(i, end=' ')

print()
i = -1
while i>=-(len(s)):
    print(s[i], end=' ')
    i=i-1
print()

for i in range(1,len(s)+1):
    print(s[-i], end=' ')
print()

for i in s[::-1]:
    print(i, end=' ')