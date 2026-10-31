# Bank Account
class Account():
    Bank = "Hello Bank"
    def __init__(self,name,total):
        self.name = name
        self.total = int(total)
        
    def deposit(self,update):
        self.total += update

    def withdrawl(self,taken):
        self.total -= taken

    def current_balance(self):
        return f'Total Balance: {self.total}'

customer = Account("Apil","10000")
customer.deposit(500)
customer.withdrawl(250)
print(customer.name,customer.Bank,customer.current_balance())