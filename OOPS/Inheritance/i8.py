# pgm on single inheritance

class Bank(object):

    cash = 10_00_000.00

    @classmethod
    def avail_cash(cls):
        print("Available cash =", cls.cash)

class AndhraBank(Bank):
    pass

class StateBank(Bank):

    cash = 2_00_000.00
    @classmethod
    def avail_cash(cls):
        print("Available cash =", (cls.cash + Bank.cash))

a = AndhraBank()
a.avail_cash()
s = StateBank()
s.avail_cash()

# either way to call methods
AndhraBank.avail_cash()
StateBank.avail_cash()