# program to find a number of words in a string

s = input("enter a string:")

print("method 2")
count = 0
for i in range(len(s)):
    if s[i] == ' ':
        count = count+1
print("no of words is:", count+1)

print("method 2")
l = s.split()
i = 0
for j in l:
    i = i+1

print("no of words is:", i)

