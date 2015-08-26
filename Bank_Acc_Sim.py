class BankAccount():
"""A class to simulate a bank account"""
    def __init__(self,name,balance):
        self.balance = balance
        self.name = name
        self.statement = {"Initial Balance",self.balance}
        print "Bank Account created successfully for",self.name,"with balance",self.balance
    
    def deposit(self,deposit):
        self.balance += deposit
        self.statement["Deposited"] = amount
        print deposit,"depositted to Mr.",self.name,"'s Account"
        print "Current Balance is",self.balance
        
    def withdraw(self,amount):
        if amount >= self.balance :
            print "Sorry, you have insufficient funds"

        else :
            self.balance -= amount
            self.statement["Withdrawen"] = amount
            print "After this operation your balance is:",self.balance
    def del_ver(self):
        ver = raw_input("Are you sure(Y/N): ")
        if ver == "Y" :
            print "Destructor started"
            
        elif ver == "N" :
            print "Why are you playing around???"
            
        else :
            print "You're such a jerk!!!"
            print "Can't you read a simple instruction ???"
