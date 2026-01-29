"""
10. Write a program to find the factorial of a given number using a while loop.

"""

"""
“If I need digit 1 → use != 0
If 1 does nothing → use > 1”
"""

# number = int(input("enter number to get factorial: "))

# fact = 1 # factorial is initialized to 1 because multiplication with 0 gives 0

# while(number>1): # The loop repeatedly multiplies values while number is non-zero and stops when it reaches 0.

#     fact = fact * number # Multiplies the current value of fact with number to build the factorial step by step.

#     number = number - 1 # Decreases number by 1 each iteration to move toward the stopping condition (number == 0).

# print(fact)


number = int(input("enter number to get factorial: "))

i = 1 #used for iteration

result = 1 #used to store result after each iteration, used 1 bcoz if 0 all will become zero

while(i<=number):

    result = result * i

    i = i + 1

print(number,"factorial is ",result)