# Python program to check if a string is palindrome or not

st = input("enter a string to check if it is palindrome or not:")

if st == st[::-1]:
    print("given string '{:s}' is palindrome".format(st))
else:
    print("given string {:s} is not palindrome",format(st))