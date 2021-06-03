from Car import CAR

class Benz(CAR):

    def steering(self):
        print('Benz uses power steering')
        print('plz drive the car safely')

    def breaking(self):
        print('Benz uses Gas breaks')
        print('Apply breaks and stop it')

b = Benz('Tn70102')
b.openTank()
print('.....................................')
b.steering()
print('.....................................')
b.breaking()