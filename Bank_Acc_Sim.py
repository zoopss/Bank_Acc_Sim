class BankAccount():
    def __init__(self,name,balance):
        self.balance = balance
        self.name = name
        self.statement ="Initial Balance :",self.balance,"\n"
        self.debt = 0
        print "Bank Account created successfully for",self.name,"with balance",self.balance
    
    def deposit(self,deposit):
        self.balance += deposit
        self.statement += "Deposited :", deposit,"\n"
        print deposit,"deposited to",self.name,"'s Account"
        print "Current Balance is",self.balance
        
    def withdraw(self,amount):
        if amount >= self.balance :
            print "Sorry, you have insufficient funds"

        else :
            self.balance -= amount
            self.statement += "Withdrawn :",amount,"\n"
            print "After this operation your balance is:",self.balance



    def loan(self,amount):
        rate = 0
        if amount <= 50000 :
            rate = 6
        elif amount > 50000 & amount < 100000 :
            rate = 8.5
        elif amount > 100000 :
            rate = 11

        self.debt += amount
        self.statement += "Loan Approved :",amount,"\n"
        print "Your loan of",amount,"has been approved at a rate of",rate

    def statement(self):
        self.statement += "Balance :",self.balance,"\n"

        
    def __del__(self):
        print "Your account has been submitted for closure. Thank you for banking with us."
