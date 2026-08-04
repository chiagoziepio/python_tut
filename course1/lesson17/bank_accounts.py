class BalanceException(Exception):
    pass

class BankAccount():
    def __init__(self, initialAmt, acctName):
        self.balance = initialAmt
        self.name = acctName
        print(f"\nAccount '{self.name}' created.\n\nBalance = ${self.balance:.2f}  ")

    def getBalance(self):
         print(f"\nAccount '{self.name}' Balance = ${self.balance:.2f}  ")

    def deposit(self, amount) :
        self.balance += amount
        print(f"Deposit of ${amount:.2f} successful.")
        self.getBalance()
    def viableTransacion(self, amount):
        if amount > self.balance:
            raise BalanceException(f"Account '{self.name}' has insufficient funds.")
        else:
            return True

    def withdraw(self, amount):
        try:
            self.viableTransacion(amount)
            self.balance -= amount
            print(f"\nWithdrawal of ${amount:.2f} successful.")
            self.getBalance()
        except BalanceException as e:
            print(f"Withdrawal failed: {e}")

    def transfer(self, amount, recipient):
        try:
            print("\n************\n\nTransfer Initiated\n\n************")
            self.viableTransacion(amount)
            self.withdraw(amount)
            recipient.deposit(amount)
            
         
            recipient.getBalance()
            print("\n************\n\nTransfer Completed\n\n************")
        except BalanceException as e:
            print(f"Transfer failed: {e}")



class InterestBankAccount(BankAccount):
    def deposit(self, amount):
        interest = amount * 0.10
   
        totalDeposit = amount + interest
        self.balance += totalDeposit
        print(f"\nDeposit of ${amount:.2f} successful.")
        self.getBalance()


class SavingsAccount(InterestBankAccount):
    def __init__(self, initialAmt, acctName):
        super().__init__(initialAmt, acctName)
        self.fee = 5
    def withdraw(self, amount):
        try:
            amtToWithdraw =amount + self.fee
            self.viableTransacion(amtToWithdraw)
            self.balance -= amtToWithdraw
            print(f"\nWithdrawal of ${amount:.2f} successful.")
            self.getBalance()
        except BalanceException as e:
            print(f"\nWithdrawal failed: {e}")