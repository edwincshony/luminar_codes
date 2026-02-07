"""
pgm to find largest of 3
"""

number1 = int(input("enter num1: "))

number2 = int(input("enter num2: "))

number3 = int(input("enter num3: "))

if number1 >= number2 and number1 >= number3:
    print(number1,"is larger")
elif number2 >= number1 and number2 >= number3:
    print(number2,"is larger")
elif number3 >= number1 and number3 >= number2:
    print(number3,"is larger")