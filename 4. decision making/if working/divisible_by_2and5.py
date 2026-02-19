"""
w.a.p to check if a number is divisible by both 2 and 5
"""

number = int(input("Enter number: "))

if number % 2 == 0 and number % 5 == 0:
    print("number is divisible by both 2 and 5")
else:
    print("number is not divisible by both 2 and 5")