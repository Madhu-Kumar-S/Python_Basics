# python program on inner classes

class Person:

    def __init__(self, name):
        self.name = name
        # self.dob = self.DOB() --creating inner class object

    def display(self):
        print("Dear {} !".format(self.name))
        # self.dob.display() --calling inner class instance method

    class DOB:

        def __init__(self, dd, mm, yr):
            self.dd = dd
            self.mm = mm
            self.yr = yr

        def display(self):
            print("your DOB is {}/{}/{}".format(self.dd, self.mm, self.yr))

p = Person("Kalki")
p.display()

# way 1 -- creating object to inner class and calling its instance method
dob = Person.DOB(18, 2, 2000)
dob.display()

# way 2
# db = p.dob --creating inner class object outside the main class
# db.display() --calling inner class instance method
