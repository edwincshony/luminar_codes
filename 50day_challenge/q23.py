def simple_calculator():

    try:

        num1 = int(input("Enter number1: "))
        num2 = int(input("Enter number2: "))

        operation = input("Enter the operation to perform (+, -, *, /): ")

        if operation == "+":

            result = num1 + num2

        elif operation == "-":

            result = num1 - num2

        elif operation == "*":

            result = num1 * num2

        elif operation == "/":

            result = num1 / num2
        else:
            raise NameError("Invalid operation")
        
        print(result)

    except ZeroDivisionError:
        print("division by zero not allowed")
    except ValueError:
        print("please enter valid numbers")
    except NameError:
        print("invalid operation")

simple_calculator()