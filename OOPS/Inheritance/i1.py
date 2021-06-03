# creating Teacher class and defining its attributes and methods

class Teacher:

    def set_data(self, id, name, address):
        self.id = id
        self.name = name
        self.address = address

    def set_salary(self, salary):
        self.salary = salary

    def get_data(self):
        return self.id, self.name, self.address

    def get_salary(self):
        return self.salary

i = int(input("Enter id:"))
n = input("Enter name:")
a = input("Enter address:")
s = int(input("Enter salary:"))

t = Teacher()
t.set_data(i, n, a)
id, name, address = t.get_data()
t.set_salary(s)

print("Teacher details are:")
print("ID = ", id)
print("Name = ", name)
print("Address = ", address)
print("Salary = ", t.get_salary())

