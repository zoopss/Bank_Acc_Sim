import random
class BankAccount():
    def __init__(self,name,balance):
        self.balance = balance
        self.name = name
        self.auth = int(raw_input("Enter a 4-Digit PIN for your account : "))
        
        self.statement ="Initial Balance :",self.balance
        self.anum = random.randint(0,100000)
        self.debt = 0
        print "Bank Account created successfully for",self.name,"with balance",self.balance,"And account number", self.anum
    
    def deposit(self,deposit):
        self.balance += deposit
        self.statement += "Deposited :", deposit
        print deposit,"deposited to",self.name,"'s Account"
        print "Current Balance is",self.balance
        
    def withdraw(self,amount):
        if amount >= self.balance :
            print "Sorry, you have insufficient funds"
            
        else :
            pin1 = int(raw_input("Enter your PIN : "))
            if pin1 == self.auth :
                self.balance -= amount
                self.statement += "Withdrawn :",amount
                print "After this operation your balance is:",self.balance

            else :
                print "Authentication Failed..."



    def loan(self,amount):
        rate = 0
        if amount <= 50000 :
            rate = 6
        elif amount > 50000 & amount < 100000 :
            rate = 8.5
        elif amount > 100000 :
            rate = 11

        self.debt += amount
        self.statement += "Loan Approved :",amount
        print "Your loan of",amount,"has been approved at a rate of",rate,"% per annum"

    def statement(self):
        print "" + self.statement
        print "Balance :",self.balance

        
    def __del__(self):
        print "Your account has been submitted for closure. Thank you for banking with us."
        
        
        
        #-------------main-----------------
        
print" Welcome to ABC Bank"
print"Functions defined in class BankAccount()"
print"+ __init__ - Creates a new Account"
print"Usage : obj_name = BankAccount("Name of Owner",initial_bal)"
print"+_deposit_ - deposits money in your account"
print"Usage : obj_name.deposit( amount)"
print"+_withdraw_ - withdraws money from your account"
print"Usage : obj_name.withdraw( amount )"
print"+_loan_ - grands you a loan "
print"Usage : obj_name.loan(amount )"
print"+_statement_ - lists or the transactions done on your account"
print"Usage : obj_name.statement()"
print"+_del_ - closes your account"
print"Usage : del obj_name"

