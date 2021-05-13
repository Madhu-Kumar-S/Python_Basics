# Python program to print even length words in a string

str = input("enter a string:")

print("your string is:", str)

print("even length of words in a string are:")

for i in str.split():
    if len(i)%2 ==0:
        print(i)