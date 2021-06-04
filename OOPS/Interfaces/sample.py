# example to an Interface -->is an ex for polymorphism
from abc import *

class Connection(ABC):

    @abstractmethod
    def show(self):
        pass

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def disconnect(self):
        pass

class Oracle(Connection):

    def show(self):
        print("==========================================")
        print("WellCome to Oracle DataBase!")
        print("==========================================")

    def connect(self):
        print("please wait while connecting to database!")
        print(". . . . . . . .")
        print("Successfully connected to the Oracle database.")

    def disconnect(self):
        print("Successfully disconnected to the Oracle database.")

class Sybase(Connection):

    def show(self):
        print("==========================================")
        print("WellCome to Sybase DataBase!")
        print("==========================================")

    def connect(self):
        print("please wait while connecting to database!")
        print(". . . . . . . .")
        print("Successfully connected to the Sybase database.")

    def disconnect(self):
        print("Successfully disconnected to the Sybase database.")

class Database(object):

    str = input("Enter database name:")
    classname = globals()[str]
    obj = classname()
    obj.show()
    obj.connect()
    obj.disconnect()
