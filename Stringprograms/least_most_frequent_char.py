# Python – Least  and maximum Frequent Character in String
print("method 1")
s = input("enter a string:")

d = {}

for i in s:
    k = i
    v = s.count(i)
    d.update({k:v})

nd =dict(sorted(d.items(), key=lambda x: x[1]))

for i,j in nd.items():
    print("least frequent char in string is: '{:s}'".format(i))
    break

print("......................................................................................")
print("method 2")
# Maximum frequency character in String
# naive method

# initializing string
test_str = "GeeksforGeeks"

# printing original string
print("The original string is : " + test_str)

# using naive method to get
# Maximum frequency character in String
all_freq = {}
for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

res1 = max(all_freq, key=all_freq.get)
res2 = min(all_freq, key=all_freq.get)
# printing result
print("The maximum of all characters in GeeksforGeeks is : " + str(res1))
print("The minimum of all characters in GeeksforGeeks is : " + str(res2))


