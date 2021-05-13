# Maximum of two numbers in Python

def max(a, b):
    if a > b:
        return a
    else:
        return b


result = max(50, 6)

print("{} is maximum".format(result))