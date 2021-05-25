# python program on namespaces

# modifying class variable in the class namespace

class Student1:

    n = 10  # class var

print(Student1.n)
Student1.n += 1
print(Student1.n)

s1 = Student1()
print(s1.n)
s2 = Student1()
print(s2.n)
print("..........................")
# modifying class variable in instance namespace

class Student2:
    n = 10

s1 = Student2()
print(s1.n)
s1.n += 1
print(s1.n)
s2 = Student2()
print(s2.n)

