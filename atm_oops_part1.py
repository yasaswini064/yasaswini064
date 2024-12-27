class atm():
    bank_name = "kotak bank"
    color = "blue"
    time = 24*7
    def credit(self):
        print("I credited 1000rs in",self.bank_name)
    def withdraw(self):
        print("yesterday i withdraw 500 from the",self.bank_name)
        self.credit()
    def debit(self):
        print("last year 10,000 was debited from my bank account")
        self.withdraw()
obj = atm()
obj.credit()
obj.withdraw()
obj.debit()
