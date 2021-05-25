# python program to create class and obect

class person:

    # attributes = variables
    name = "Saphire Leo"
    age = 21

    # actions = methods
    @classmethod
    def display(cls):
        print("name = {:s}".format(cls.name))
        print(("age = {:d}".format(cls.age)))

# creating object to class
p = person()
#  calling class method through object
p.display()

print("name = {:s}".format(p.name))

