# Find words which are greater than given length k

s = input("enter a string:")

s.replace('.' or ',' or ';', '')

n = int(input("enter the length to print the words in string equal to len:"))

for i in s.split():
    if len(i) >n:
        print(i, end=' ')
