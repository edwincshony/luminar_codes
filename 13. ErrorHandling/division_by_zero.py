# division by zero

"""
try:

    doubtful code

except:

    handling code
"""

n1 = int(input("enter number1: "))
n2 = int(input("enter number2: "))

try:

    result = n1/n2

    print("Result of division is",result)

except Exception as e:

    n2 = int(input("enter number2: "))

    result = n1/n2

finally:

    print("Database commit")