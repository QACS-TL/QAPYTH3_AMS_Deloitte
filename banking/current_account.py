from account import Account
class Current_account(Account):
    _overdraft_limit = 0
    def __init__(self, account_number, account_name, balance, overdraft_limit):
        super().__init__(account_number, account_name, balance)
        self.overdraft_limit = overdraft_limit

    @property
    def overdraft_limit(self):
        return self._overdraft_limit

    @overdraft_limit.setter
    def overdraft_limit(self, value):
        if value < 0:
            value = 0
        self._overdraft_limit = value

    def get_balance(self):
        return self._balance

    def set_balance(self, value):
        if value + self.overdraft_limit < 0:
            raise ValueError("Insufficient funds. Overdraft limit exceeded")
        self._balance = value

    balance = property(get_balance, set_balance)

    def withdraw(self, amount):
        if amount < 0 or self.overdraft_limit < -(self.balance - amount):
            raise ValueError("Insufficient funds. Overdraft limit exceeded")
        self.balance = self.balance - amount
        return self.balance