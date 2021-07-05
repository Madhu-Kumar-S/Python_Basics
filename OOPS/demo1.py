# python program to create class and object

class person:
    # class represents a common behavioural of an objects and is a blue print of an objects
    # class does not exist physically

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
#  calling class method through class name
person.display()

print("name = {:s}".format(p.name))

