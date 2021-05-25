import sys

class Bank:

    def __init__(self, name, bb = 0.0):
        self.name = name
        self.bank_balance = bb

    def deposit(self):
        damount = int(input("Enter an amount to deposit:"))
        self.bank_balance = self.bank_balance + damount
        return self.bank_balance

    def withdrawal(self):
        wamount = int(input("Enter an amount to withdraw:"))
        if self.bank_balance <= 500:
            print("Insufficient balance !")
        else:
            print(wamount,"withdrawad")
            self.bank_balance = self.bank_balance - wamount
            return self.bank_balance

    def balance(self):
        return self.bank_balance


name = input("Enter account holder name:")

b = Bank(name)

print("Enter:\n1.'D' for Deposit.\n2.'W' for Withdrawal.\n3.'B' for Bank balance\n4.'E' for exit.")
while True:
    ch = input("enter your choice:")
    if ch == 'D' or ch == 'd':
        print("Balance after deposit is ", b.deposit())
    elif ch == 'W' or ch == 'w':
        print("Balance after withdrawal is ", b.withdrawal())
    elif ch == 'B' or ch == 'b':
        print("Dear {} ! \n your bank balance is {}".format(b.name, b.balance()))
    elif ch == 'E' or ch == 'e':
        sys.exit()