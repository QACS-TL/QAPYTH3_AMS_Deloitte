
class Account():
    account_number = "00000000"
    _account_name = "Anon"
    _balance = 0.00

    def get_account_name(self):
        return self._account_name

    def set_account_name(self, value):
        if len(value) < 2:
            raise ValueError("Account name must be at least 2 characters long")
        self._account_name = value

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value < 0:
            value = 0
        self._balance = value

    balance = property(get_balance, set_balance)

    def deposit(self, amount):
        if (amount <= 0):
            print("value must be positive")
            return self.balance
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if (amount <= 0 or self.balance < amount):
            print("value must be positive and less than the current balance")
            return self.balance
        self.balance -= amount
        return self.balance
