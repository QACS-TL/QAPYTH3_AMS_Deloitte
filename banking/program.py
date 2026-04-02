from account import Account

acc1 = Account()
acc2 = Account()

acc1.account_number = "876543221"
acc1.account_name = "Ted Lasso"
acc1.balance = 100

acc2.account_number = "123456789"
acc2.account_name = "Sadia Salleep"
acc2.balance = 200

acc1.deposit(100)
acc2.deposit(200)
print(f"Balance of {acc1.account_name} is {acc1.withdraw(150)}")
print(f"Balance of {acc2.account_name} is {acc2.withdraw(450)}")
