# Python Program for n-th Fibonacci number

def fib(n, n1=0, n2=1):
    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        print("{}st term is {}".format(n, n1), end=' ')
    elif n == 2:
        print("{}nd term is {}".format(n, n2), end=' ')
    else:
        for i in range(2,n):
            n3 = n1 + n2
            n1 = n2
            n2 = n3
        print("{}th term is {}".format(n, n3))

no= int(input("enter which term to find fibonacci no:"))

fib(no)
