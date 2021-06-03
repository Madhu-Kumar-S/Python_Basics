# pgm to show method overloading to find the sum of the two numbers

def sum(a=None, b=None, c=None):

    if a!=None and b!=None and c!=None:
        print("Sum of Three numbers =", (a+b+c))
    elif a!=None and b!=None and c==None:
        print("Sum of Two numbers =",(a+b))
    else:
        print("please enter two or three arguments")

n = int(input("Enter how many numbers:"))

if n==2:
    a, b = [int(i) for i in input("Enter values:").split()]
    sum(a, b)
elif n==3:
    a, b, c = [int(i) for i in input("Enter values:").split()]
    sum(a, b, c)