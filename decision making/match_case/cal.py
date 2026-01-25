
"""
create a calculator application
read num1,num2 and operation

if operation == "+" => add num1+num2
if operation == "-" => sub num1-num2
if operation == "*" => multiply num1*num2
if operation == "/" => divide num1/num2
if operation == "%" => modulus num1%num2
if operation == "**" => exponentation num1**num2
if operation == "//" => floor division num1//num2
else invalid operation
"""

num1 = int(input("enter number1: "))
num2 = int(input("enter number2: "))

operation = input("enter opeartion symbol: ")

match operation:
    case "+":
        result = num1 + num2
        print("result is:",result)
    case "-":
        result = num1 - num2
        print("result is:",result)
    case "*":
        result = num1 * num2
        print("result is:",result)
    case "/":
        result = num1 / num2
        print("result is:",result)
    case "%":
        result = num1 % num2
        print("result is:",result)
    case "**":
        result = num1 ** num2
        print("result is:",result)
    case "//":
        result = num1 // num2
        print("result is:",result)