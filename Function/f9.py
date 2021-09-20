# passing a group of elements to a fun

def calculate(l):
    sum = 0
    for j in l:
        sum = sum+j
    print("sum of all values is:", sum)


lst = [int(i) for i in input("enter a list of numbers:").split()]
calculate(lst)