class Teacher(object):

    def __init__(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def display(self):
        print("Id  =", self.id)
        print("Name =", self.name)
        print("Address =",self.address)

    def get_salary(self, salary=0.0):
        print("Salary =", salary)

class Student(Teacher):
    def __init__(self, id, name, address):
        super().__init__(id, name, address)

    def display(self):
        super().display()

    def get_marks(self, marks=0.0):
        print("Marks =", marks)

id1 = int(input("enter teacher\'s id:"))
name1 = input("enter teacher\'s name:")
address1 = input("enter teacher\'s address:")
salary = float(input("enter teacher\'s salary:"))
print()
print("Teacher Details:")
t =Teacher(id1, name1, address1)
t.display()
t.get_salary(salary)

print("......................................")

id2 = int(input("enter student\'s id:"))
name2 = input("enter student\'s name:")
address2 = input("enter student\'s address:")
marks = float(input("enter student\'s marks:"))
print()
print("Students Details:")
s = Student(id2, name2, address2)
print(s.display())
s.get_marks(marks)