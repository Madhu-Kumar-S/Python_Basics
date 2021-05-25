# python program on inner classes

class Person:

    def __init__(self):
        self.name = "Kalki"

    def display(self):
        print("Dear {} !".format(self.name))

    class DOB:

        def __init__(self):
            self.dd = 18
            self.mm = 2
            self.yr = 2000

        def display(self):
            print("your DOB is {}/{}/{}".format(self.dd, self.mm, self.yr))

p = Person()
p.display()
dob = Person().DOB()
dob.display()
