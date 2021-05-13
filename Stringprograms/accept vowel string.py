# Python program to accept the strings which contains all vowels

s = input("enter a string:")

s = s.lower()

if ('a' and 'e' and 'i' and 'o' and 'u') in s:
    print("your string is accepted as it contains vowels!")
else:
    print("your string not is accepted as it does not contains vowels!")


