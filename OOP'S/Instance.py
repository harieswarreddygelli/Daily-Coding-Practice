class Bank:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.balance=balance
    
    def Deposit(self,amount):
        self.balance+=amount
        return self.balance
a=Bank("Hari",1006)
amount=int(input("Enter How much you want to Deposit: "))
print("The current Balance after Deposit: ",a.Deposit(amount))
