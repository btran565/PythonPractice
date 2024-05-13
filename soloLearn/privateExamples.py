class BankAccount:
    def __init__(self, balance):
        self._balance = balance     #single underscore

    def __repr__(self):     #double underscore
         return "Account Balance: {}".format(self._balance)
    
    def deposit(self, amount):
        #your code goes here
        self._balance = self._balance + amount

acc = BankAccount(0)
acc.deposit(int(input()))
print(acc)
