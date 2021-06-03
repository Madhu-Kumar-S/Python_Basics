# example on magic methods --> > = object.__gt__(self, other)

class Ramayan(object):
    def __init__(self, pages):
        self.pages = pages

    def __gt__(self, other):
        return self.pages>other.pages

class Mahabharat(object):
    def __init__(self, pages):
        self.pages = pages

r = Ramayan(10000)

m = Mahabharat(50000)

if r>m:
    print("Ramayan has more pages.")
else:
    print("Mahabharat has more pages.")