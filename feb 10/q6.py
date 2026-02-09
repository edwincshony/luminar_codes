"""
6. Write a function that takes three numbers as parameters and returns the largest number.

"""

def largest_of_three(num1,num2,num3):

    if num1 >= num2 and num1 >= num3:

        return num1
    
    elif num2 >= num1 and num2 >= num3:

        return num2
    
    else:
        
        return num3
    
print(largest_of_three(30,20,10))