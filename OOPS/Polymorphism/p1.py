# Duck typing philosophy in python

class Duck(object):

    def talk(self):
        print("quack quack !")

class Human(object):

    def talk(self):
        print("hi , hello!")

class Dog(object):

    def bark(self):
        print("bow bow !")

def call_talk(obj):   # method exhibiting different behaviour while taking different objects --polymorphism
    if hasattr(obj, 'talk'):
        print(type(obj))
        obj.talk()
    elif hasattr(obj, 'bark'):
        print(type(obj))
        obj.bark()
    else:
        print("wrong object passed")


du = Duck()
call_talk(du)

h = Human()
call_talk(h)

do = Dog()
call_talk(do)

print(hasattr(do, 'talk'))  # this method returns true if the attribute (method/var/object) is present in that class
print(hasattr(do, 'bark'))  # hasattr(object, 'method/variable')--syntax

