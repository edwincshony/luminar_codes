"""Create a program that:
Takes student name
Takes course fee
Takes amount paid
Raise error if:
Fee is negative
Paid amount is negative
Paid amount is greater than fee
Handle invalid input
Always print "Registration Process Finished" using finally"""


try: 

    name = input("enter name: ")

    fee = int(input("enter course fee: "))

    amount_paid = int(input("enter amount paid: "))

    if fee < 0:

        raise Exception("Fee is negative")

    if amount_paid < 0:

        raise Exception("Paid amount is negative")

    if amount_paid > fee:

        raise Exception("Fee is negative")

except Exception as e:

    print(e)

finally:

    print("Registration Process Finished")





