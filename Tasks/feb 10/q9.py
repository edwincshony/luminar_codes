"""
9. Write a function that takes two numbers and an operator (+, -, *, /) as parameters and returns the calculated result.

"""

def calculator(num1,num2,op="+"):

    if op == "+":

        return num1 + num2
    
    elif op == "-":

        return num1 - num2
    
    elif op == "*":

        return num1 * num2
    
    elif op == "/":

        if num2 == 0:

            return "Error: division by zero"
        
        return num1 / num2

    
print(calculator(10,0,op="/"))