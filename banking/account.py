class Account():
    # account_number = "00000000"
    _account_name = ""
    _balance = 0

    def __init__(self, account_number = "00000000", account_name="Anon", balance=0 ):
        self.account_number = account_number
        self.account_name = account_name
        self.balance = balance


    @property
    def account_name(self):
        return self._account_name

    @account_name.setter
    def account_name(self, value):
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

    def __str__(self):
        return f"The current balance of {self.account_name} is {self._balance}"