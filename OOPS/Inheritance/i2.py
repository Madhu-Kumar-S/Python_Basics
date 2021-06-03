# creating Student class and deriving attributes and methods from Teacher class to Student class

from i1 import Teacher

class Student(Teacher):

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks

si = int(input("Enter id:"))
sn = input("Enter name:")
sa = input("Enter address:")
sm = int(input("Enter marks:"))

s = Student()
s.set_data(si, sn, sa)
id, name, address = s.get_data()
s.set_marks(sm)

print("Student deatils are:")
print("ID = ", id)
print("Name = ", name)
print("Address = ", address)
print("Marks = ", s.get_marks())
