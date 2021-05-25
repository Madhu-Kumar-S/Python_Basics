# python program on Class methods

class Bird:

    wings = 2  # class variable

    @classmethod
    def fly(cls, name):  # class method
        print('{:s} flies with {:d} wings.'.format(name, cls.wings))

Bird.fly("peacock")  # calling class method
Bird.fly("Sparrow")