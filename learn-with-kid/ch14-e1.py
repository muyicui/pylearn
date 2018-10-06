class BankAccount:
    def __init__(self, acc_name, acc_number):
        self.Account = acc_name
        self.AccountNumber = acc_number
        self.Balance = 0.0
    def ShowBalance(self):
        print("Your account has $", self.Balance,sep='')
    def deposite(self,money):
        self.Balance = self.Balance + money
        print("you are saving $", money,sep='')
        print("Your account has $", self.Balance,sep='')

    def withdraw(self,money):
        if self.Balance < money:
            print("you don't have enough money")
        else:
            self.Balance = self.Balance - money
            print("you are withdrawing $", money)
            print("Your account has $", self.Balance,sep='')

class InterestAccount(BankAccount):
    def AddInterest(self,rate):
        interest = self.Balance * rate
        print("add", rate*100, "percent interest")
        self.deposite(interest)
myAccount = InterestAccount("Huanran",130536)
myAccount.ShowBalance()
myAccount.deposite(124)
myAccount.withdraw(12)
myAccount.withdraw(131)
myAccount.AddInterest(0.15)