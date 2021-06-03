from abc import *

class CAR(ABC):

    def __init__(self, reg_no):
        self.reg_no = reg_no

    def openTank(self):
        print('Fill the fuel into the tank, for the car with reg_no {:s}'.format(self.reg_no))

    @abstractmethod
    def steering(self):
        pass

    @abstractmethod
    def breaking(self):
        pass

