from current_account import Current_account
from account import Account

acc1 = Account("876543221", "Ted Lasso", 100)
acc2 = Account()
cacc = Current_account("876543221", "Ted Lasso", 100, 200)
print(f"current account balance: {cacc.balance}")
print(f"current account balance: {cacc.withdraw(300)}")
try:
    cacc.withdraw(1)
except Exception as e:
    print(e)
print(f"current account balance: {cacc.balance}")

# acc1.account_number = "876543221"
# acc1.account_name = "Ted Lasso"
# acc1.balance = 100

acc2.account_number = "123456789"
try:
    acc2.account_name = "S"
except Exception as e:
    print(e)
    acc2.account_name = "Anonymous"
acc2.balance = 200

acc1.deposit(100)
acc2.deposit(200)
print(f"Balance of {acc1.account_name} is {acc1.withdraw(150)}")
print(f"Balance of {acc2.account_name} is {acc2.withdraw(450)}")
print(acc1)