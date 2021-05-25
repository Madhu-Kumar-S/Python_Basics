# python program using classes and objects

class Computer:

    def __init__(self, cpu, ram):  # constructor / instance method / predefined method
        # instance variables
        self.cpu = cpu
        self.ram = ram

    def config(self):  # instance methods

        print("Configuration is:")
        print("CPU = ", self.cpu)
        print("RAM = ", self.ram)

    def compare(self, c2):  # self = c1 and c2 = c2
        if self.ram == c2.ram: return "both rams are same"
        else: return "both rams are different"

# creating (instance)object to class / intantiating
c1 = Computer('i7', '8 GB')
c2 = Computer('i9', '16 GB')

# calling methods through instance
c1.config()
Computer.config(c2)

print("comparision of RAM")
print(c1.ram == c2.ram)  # using == operator
print(c1.compare(c2))  # using pre-defined function




