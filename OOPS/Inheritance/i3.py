# simple inheritance

class A(object):
    print("This is class A")
    
    def f1(self):
        print("This is feature 1")

    def f2(self):
        print("This is feature 2")

class B(A):
    print("This is class B")

    def f3(self):
        print("This is feature 3")

    def f4(self):
        print("This is feature 4")

b = B()

b.f1()
b.f2()
b.f3()
b.f4()