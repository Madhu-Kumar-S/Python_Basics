# Python Program for n-th Fibonacci number using dynamic programming

n = int(input("enter upto how many terms:"))

n1 = int(input("enter 1st no:"))

n2 = int(input("enter 2nd no:"))

print("\nfibonacci series\n")

def fib(n1, n2, n):
    if n < 0:
        print("Incorrect Input")
    elif n == 1:
        print(n1, end=' ')
    elif n == 2:
        print(n1, n2, end=' ')
    else:
        print(n1, n2, end=' ')

        for i in range(2,n):
            n3 = n1 + n2
            print(n3, end=' ')
            n1 = n2
            n2 = n3

fib(n1, n2, n)





