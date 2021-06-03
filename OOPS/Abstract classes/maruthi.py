from Car import CAR

class Maruthi(CAR):

    def steering(self):
        print('Maruthi uses manual steering')
        print('Drive the car')

    def breaking(self):
        print('Maruthi uses Hydraulic breaks')
        print('Apply breaks and stop it')

m = Maruthi('Tn70101')
m.openTank()
print('...................................')
m.steering()
print('...................................')
m.breaking()
