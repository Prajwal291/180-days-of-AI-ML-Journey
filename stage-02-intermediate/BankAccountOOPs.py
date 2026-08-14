'''OOP Challenge — Bank Account

Create a class called:

BankAccount
1️⃣ Attributes

Your object should store:

account_holder
account_number
balance

Initialize them using __init__.

2️⃣ Create these methods
deposit(amount)

Adds money to the balance.

Example:

Initial balance: ₹5000
Deposit: ₹2000
New balance: ₹7000
withdraw(amount)

Subtracts money from the balance.

But there are two conditions:

If amount > balance:
    "Insufficient balance"

Otherwise, subtract it.

display_balance()

Print:

Account Holder: Prajwal
Balance: ₹7000
3️⃣ Create two objects

For example:

Account 1:
Prajwal
12345
₹5000

Account 2:
Rahul
67890
₹10000

Perform different deposits and withdrawals on each account.

🎯 Extra challenge

Add one more method:

transfer(amount, another_account)

So you can do:

account1.transfer(1000, account2)

After the transfer:

Account 1 balance → ₹4000
Account 2 balance → ₹11000
💡 Hints for the extra challenge

You already know everything required.

Think:

self.balance

represents the balance of the current account.

And:

another_account.balance

represents the other account's balance.

You can call another object's methods too.'''


#Code.........................................................................
class Bank_Account:
    def __init__(self,account_holder,account_number,balance):
        self.account_holder=account_holder
        self.account_number=account_number
        self.balance=balance

    def display_info(self):
        print(f"Account_holder: {self.account_holder}")
        print(f"Account_Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")

    def deposit(self,amount):
        self.balance=self.balance+amount

    def withdraw(self,amount):
        if amount>self.balance:
            print("Insufficient Balance!!")
        else:
            self.balance=self.balance-amount

    def display_balance(self):
        print(f"Account Holder: {self.account_holder}")
        print(f"Balance: {self.balance}")
        
    def transfer(self,amount,another_account):
        if amount > self.balance:
            print("Insufficient Balance!")
        else:
            self.balance=self.balance-amount
            another_account.balance=another_account.balance+amount


account1=Bank_Account("Prajwal",12345,5000)
account2=Bank_Account("Rahul",67890,10000)

account1.display_info()
print("\n")
account2.display_info()
print("\n")
account1.deposit(50000)
account2.deposit(70000)
account1.display_balance()
print("\n")
account2.display_balance()
print("\n")
account1.withdraw(10000)
account1.display_balance()
print("\n")
account2.withdraw(20000)
account2.display_balance()
print("\n")
account2.withdraw(1000000)
account2.display_balance()
print("\n")
account1.transfer(10000,account2)

account1.display_balance()
print("\n")
account2.display_balance()






