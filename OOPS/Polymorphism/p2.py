# operator overloading -->ex for polymorphism

a = 5
b = 2

print(a+b)  # adds two no
print(int.__add__(a,b))

s1 = "hi "
s2 = "hello!"

print(s1+s2)  # concatinates two strings
print(str.__add__(s1,s2))

l1 = [1, 2]
l2 = [3, 4]

print(l1+l2)  # combines two lists

# so here + operator is performing different task depending upon the context we give


