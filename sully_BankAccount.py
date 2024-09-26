class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self._account_number = account_number
        self._account_holder = account_holder
        self._balance = balance
    
    def get_account_number(self):
        return self._account_number
    
    def get_account_holder(self):
        return self._account_holder
    
    def get_balance(self):
        return self._balance
    
    def deposit(self, money):
        self._balance = self._balance + money
    
    def withdraw(self, money):
        self._balance = self._balance - money
    
    def account_details(self):
        details = f'Account Holder: {self._account_holder}\nAccount Number: {self._account_number}\nAccount Balance: {self._balance}'
        print(details)
        return details

peep = BankAccount(1234567, 'Peep McPeep', 12)
print(peep.get_account_holder())
print(peep.get_account_number())
print(peep.get_balance())

peep.account_details()

peep.deposit(8)

peep.account_details()

peep.withdraw(19)

peep.account_details()

    
