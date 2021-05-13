# String slicing in Python to rotate a string
s = input("enter a string:")

ch = input("enter r for right and l for left rotation:")

n = int(input("enter how many times:"))

def rotate(s, ch, n):
    if ch == 'r':
        print("right rotation")
        sr = s[n:] + s[:n]
        print(sr)
    elif ch == 'l':
        print("left rotation")
        sl = s[-1:((-n) - 1):-1] + s[:len(s) - n]
        print(sl)
    else:
        print("input error")

rotate(s, ch, n)
