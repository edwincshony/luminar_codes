"""
3. Create a menu-driven program using match–case for basic arithmetic operations:
* 1 → Addition
* 2 → Subtraction
* 3 → Multiplication
* 4 → Division
"""

number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))

print("1 → Addition")
print("2 → Subtraction")
print("3 → Multiplication")
print("4 → Division")

operation = int(input("enter operation: "))

match operation:
    case 1: print(f"{number1} + {number2} = {number1+number2}")
    case 2: print(f"{number1} - {number2} = {number1-number2}")
    case 3: print(f"{number1} * {number2} = {number1*number2}")
    case 4: 
        if number2 == 0:
            print("not possible")
        else:
            print(f"{number1} / {number2} = {number1/number2}")
    case _: print("invalid")