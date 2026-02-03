"""
9. Write a program using match–case to perform addition, subtraction, multiplication, or division based on user choice.

"""
number1 = int(input("enter number1: "))
number2 = int(input("enter number2: "))
operation = (input("enter operation: "))
match operation:
    case "+": 
        print(f"{number1} + {number2} = {number1+number2}")
    case "-": 
        print(f"{number1} - {number2} = {number1-number2}")  
    case "*": 
        print(f"{number1} * {number2} = {number1*number2}") 
    case "/":
        if number2 == 0:
            print("Error: Division by zero")
        else:

            print(f"{number1} / {number2} = {number1/number2}")
    case _: print("invalid")
  