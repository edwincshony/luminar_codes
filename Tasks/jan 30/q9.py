"""
9. Write a Python program to print each digit of a number separately using a while loop.

Any number less than 10 % 10 gives the same number
Any number less than 10 // 10 = 0

number reverse
"""

number = int(input("enter number: ")) #123  
 
result = 0 
 
while(number!=0): # 123!=0 T, 12!=0 T, 1!=0 T, 1!=0, 0!=0 F

    last_digit = number % 10 #123%10=3, 12%10=2, 1%10=0, 1%10=1

    result = result * 10 + last_digit #0*10+3=3, 3*10+2=32 , 32*10+1=321

    number = number // 10 #123//10=12, 12//10=1, 1//10=0

print(result)



