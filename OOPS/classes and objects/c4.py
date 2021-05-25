# Types of methods - instance methods

from array import *

class Student:

    def __init__(self, name, age, marks):  # constructor
        self.name = name
        self.age = age
        self.marks = marks

    def display(self):  # instance method

        print("name is {}".format(self.name))
        print("age is {}".format(self.age))

    def cal_total(self):  # instance method

        sum = 0
        for i in self.marks:
            sum = sum + i

        print("Total marks = {}".format(sum))

        avg = sum // len(marks)

        if avg == 100:
            print("grade is Out standing")
        elif avg > 90 and avg < 100:
            print("grade is A")
        elif avg > 80 and avg < 90:
            print("grade is B")
        elif avg > 70 and avg < 80:
            print("grade is C")
        elif avg > 60 and avg < 70:
            print("grade is D")
        else:
            print("no grade since ur avg marks {} is less than {}".format(avg, 60))


ns = int(input("enter how many students:"))

for i in range(1, ns+1):

    name = input("enter a name:")
    age = int(input("enter a age:"))
    print("enter marks of five subjects:")
    marks = array('i', [])
    for j in range(5):
        m = int(input())
        marks.append(m)
    print("your marks are:", *marks)

    s = Student(name, age, marks)
    print()
    print("student {} details are:".format(i))
    s.display()
    s.cal_total()
    print(".......................................")

print("******************************************************************")

# Instance methods---->2 types 1.Accessor methods, 2.Mutator methods

class demo:

    def set_name(self, name):  # Accessor method
        self.name = name

    def get_name(self):  # Mutator method
        return self.name


d = demo()

d.set_name("madhu")
print(d.get_name())
