# Function returning multiple values

def add_sub_mul_div(a, b):
    return a+b, a-b, a*b, a/2  # function returning multiple values


t = add_sub_mul_div(3, 2)  # note : returning values are stored in form of tuple

print("Addition is: ", t[0])
print("Subtraction is :", t[1])
print("Multiplication is: ", t[2])
print("Division is: ", t[3])
