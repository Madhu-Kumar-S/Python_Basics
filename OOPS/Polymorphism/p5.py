# example on magic methods --> * = object.__mul__(self, other)

class Employee(object):
    def __init__(self, name, daily_sal):
        self.name = name
        self. daily_salary = daily_sal

    def __mul__(self, other):
        return self.daily_salary * other.attendance

class Attendance(object):
    def __init__(self, att):
        self.attendance = att

e = Employee("kalki", 1000)
days = int(input("enter no of working days:"))
a = Attendance(days)
print("Employee details:")
print("Name =", e.name)
print("monthly salary =", e*a)

