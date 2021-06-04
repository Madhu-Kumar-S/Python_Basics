class BookX(object):
    def __init__(self, pages):
        self.pages = pages

    def __add__(self, other):  # here self = b1 and sother = b2
        return self.pages+other.pages


class BookY(object):
    def __init__(self, pages):
        self.pages = pages

b1 = BookX(100)
b2 = BookY(200)
print("Total pages =", b1 + b2)  # b1+b2 --> BookX.__add__(b1,b2)
#  print("Total pages =", b1 + b2) -->gives error without creating an __add__() inbuilt method inside the class

a = 2
b = 3
print(a.__add__(b))  # so this inbuilt method performs addition operation and is called as magic methods
