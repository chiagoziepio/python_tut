from bank_accounts import *

Emeka = BankAccount(500,"Emeka")
Paddy = BankAccount(1000,"Paddy")

Emeka.getBalance()
Paddy.getBalance()

Emeka.deposit(100)

Paddy.withdraw(200)
Paddy.withdraw(800)
Paddy.withdraw(100)

Emeka.transfer(300, Paddy)
Paddy.transfer(500, Emeka)
# Paddy.transfer(100, Emeka)


john =  InterestBankAccount(1000, "John")
john.deposit(150)

john.transfer(100, Paddy)


Agu = SavingsAccount(2000, "Agu")
Agu.deposit(1000)

Agu.withdraw(500)