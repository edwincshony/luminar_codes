"""
10. Create a class BankAccount with a constructor that initializes account holder name and balance. Display the account details.

"""

class BankAccount:

    def __init__(self,holder_name,balance):
        self.holder_name = holder_name
        self.balance = balance

    def display(self):
        print(self.holder_name,self.balance)

bank_inst = BankAccount("edwin",10000)
bank_inst.display()