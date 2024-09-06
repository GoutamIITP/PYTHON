'''Create account class with 2 attributes- balance & account no.,
Create account for debit,credit & printing the balance'''

class Account:
    def __init__(self, bal, acc_no):
        self.balance = bal
        self.account_no = acc_no

    def debit(self, amount):
        self.balance -= amount
        print(f"Rs. {amount} was debited")
        print("Total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print(f"Rs. {amount} was credited")
        print("Total balance = ", self.get_balance())

    def get_balance(self):
        return self.balance


acc1 = Account(10000, 5291951)
acc1.debit(5000)
acc1.credit(40000)
acc1.get_balance()