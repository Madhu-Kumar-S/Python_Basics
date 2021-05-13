# Python Program for How to check if a given number is Fibonacci number?


def fib(n, n1=0, n2=1):
    l = [0, 1]
    for i in range(2, n):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        l.append(n3)
    return l


def is_fibonacci(s, l):
    if s in l:
        print("{} is fibonacci noumber".format(s))
    else:
        print("{} is not fibonacci noumber".format(s))



no = int(input("enter no of terms:"))
print()
s = int(input("enter an element to check if it is fibonacci or not:"))
print()

is_fibonacci(s, fib(no))