"""8. Create a class Payment with a method pay(). Create subclasses CreditCard and UPI that override the pay() method.
"""

# base class
class Payment:
    def pay(self):
        print("Processing generic payment")

# subclass 1
class CreditCard(Payment):
    def pay(self):
        print("Payment done using Credit Card")

# subclass 2
class UPI(Payment):
    def pay(self):
        print("Payment done using UPI")

# create objects
p1 = CreditCard()
p2 = UPI()

# call methods
p1.pay()
p2.pay()