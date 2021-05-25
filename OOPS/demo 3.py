# python program - an example for abstraction

class myclass:

    def __init__(self):
        self.__a = 10
        self.b = 20

    def display(self):
        print(self.__a)
        print(self.b)

m = myclass()

print("accessing variables through method:")
m.display()

print("accessing variables through instance(mangling):")
# print(m.a) ---gives error becoz a var is private __
print(m._myclass__a)  # private variable can be accessed through mangling ---- instancename_classname__varname
print(m.b)  #---prints value 20