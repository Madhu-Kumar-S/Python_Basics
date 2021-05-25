# python program on instance variables

class Sample1:

    def __init__(self):

        self.x = 10  # instance variable

    def modify(self):

        self.x = self.x + 1

s1 = Sample1()
s2 = Sample1()

print("s1 = ", s1.x)
print("s2 = ", s2.x)
s1.modify()  # or s1.x = 11
print("s1 = ", s1.x)
print("s2 = ", s2.x)

print("..................................")
# python program on class / static variable

class Sample2:

    x = 10  # class variable

    @classmethod  # decorator since
    def modify(cls):  # this is class method and cls is the first parameter
        cls.x = cls.x + 1

ss1 = Sample2()
ss2 = Sample2()

print("s1 = ", ss1.x)
print("s2 = ", ss2.x)
ss1.modify()  # or s1.x = 11
print("s1 = ", ss1.x)
print("s2 = ", ss2.x)

print("class var x = ", Sample2.x)  # to access class variable outside the class

