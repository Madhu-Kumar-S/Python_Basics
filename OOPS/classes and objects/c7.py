# python program for passing of attributes and methods of one class to another class
# this class contains employee details
class Emp:

    def __init__(self, id, name, salary,):  # constructor
        self.id = id
        self.name = name
        self.salary = salary

    def display(self):  # instance method
        print("Id = ", self.id)
        print("Name  = ", self.name)
        print("Salary = ", self.salary)
# this class displays employee details
class Myclass:

    @staticmethod
    def display(e):  # static method to receive Emp class instance and display employee details
        print("Id = ", e.id)
        print("Name  = ", e.name)
        print("Salary = ", e.salary)

e = Emp(56, "Madhu Kumar", 100000000.00)

Myclass.display(e)  # passing Emp class object e to Myclass-static method ie.display(e) and calling it
