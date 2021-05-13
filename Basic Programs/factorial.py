# Python Program for factorial of a number

def factorial(no):
    if no == 0:
        return 1
    else:
        fact = 1
        for i in range(1,no+1):
            fact = fact * i
        return fact



no = int(input("enter a no:"))

result = factorial(no)

print("factorial of {} is {}".format(no, result))