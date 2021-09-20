# palindrome string

st = input("Enter a string to check if a string is palindrome or not:")
if st == st[::-1]:
    print("palindrome")
else:
    print("not palindrome")
l = len(st)


def palindrome(s, n):
    i = 0
    j = n-1
    while i < j:
        if s[i] != s[j]:
            print("not palindrome")
            break
        i += 1
        j -= 1
    else:
        print("palindrome")


palindrome(st, l)

# palindrome number

no = int(input("Enter a number:"))


def palindrome_number(n):
    temp = n
    s = 0
    while n > 0:
        r = n % 10
        n = n // 10
        s = s * 10 + r
    if temp == s:
        print("palindrome number")
    else:
        print("not a palindrome number")


palindrome_number(no)
