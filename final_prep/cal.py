
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

# num1 = int(input("Enter the num1: "))
# num2 = int(input("Enter the num2: "))

# op = input("Enter op: ")

# if num2 == 0 and op in ["%","/","//"]:

#        print("Division by zero not possible")

# else:
       
#     match op:

#         case "+":
#             result = num1 + num2
#             print(result)
#         case "-":
#                 result = num1 - num2
#                 print(result)
#         case "*":
#                 result = num1 * num2
#                 print(result)
#         case "/":
#                 result = num1 / num2
#                 print(result)

#         case "%":
#                 result = num1 % num2
#                 print(result)

#         case "**":
#                 result = num1 ** num2
#                 print(result)
#         case "//":
#                 result = num1 // num2
#                 print(result)

#         case _:

#                 print("invalid operation")

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))
# num3 = int(input("Enter num3: "))

# if num1>=num2 and num1>=num3:
#     print(num1,"is greater")
# elif num2>=num1 and num2>=num3:
#     print(num2,"is greater")
# elif num3>=num1 and num3>=num2:
#     print(num3,"is greater")

# year = int(input("Enter year: "))

# if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

#     print("Leap year")

# else:

#     print("not Leap year")

# i = 1

# while(i<=10):

#     print(i)

#     i = i + 1

"""
w.a.p display numbers from 50 - 100
"""

# i=50
# while(i<=100):
#     print(i)
#     i+=1

"""
w.a.p to display all century years from 1800 to 2026
"""

# year = 1800

# while(year<=2026):

#     if year%100 == 0:

#         print(year)

#     year += 1

# w.a.p to display all even numbers from 50 to 100

# i = 50

# while(i<=100):

#     if i % 2 == 0:

#         print(i)

#     i+=1
"""
w.a.p to display all leap years from 1800 to 2026
"""

# year = 1800
# while(year<=2026):

#     if (year % 100 == 0 and year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):

#         print(year)

#     year+=1
"""
w.a.p to display all non century years from 1800 to 2026
"""

# year = 1800

# while(year<=2026):

#     if year % 100 != 0:

#         print(year)

#     year+=1

"""
number = 1234

sum of digits = 1 + 2 + 3 + 4 = 10
"""

# number = 679
# sum=0
# while(number!=0):
#     ld = number%10
#     sum = sum + ld
#     number=number//10
# print(sum)

"""
w.a.p display sum of odd_numbers and sum of even_numbers upto limit 6
"""
# number = 1234

# tmp_number = 1234

# even_sum = 0
# odd_sum = 0

# while(number!=0):
#     ld = number%10
#     if ld%2 == 0:
#         even_sum += ld
#     else:
#         odd_sum += ld
#     number=number//10
# print(f"sum of odd_numbers in {tmp_number} is {odd_sum}")
# print(f"sum of even_numbers in {tmp_number} is {even_sum}")

"""
sum of even number upto limit
"""
# i=1
# limit = int(input("Enter the limit: "))
# sum=0
# while(i<=limit):
#     if i %2==0:
#         sum = sum + i
#     i+=1
# print(sum)

# number = 123
# rev=0
# while(number!=0):
#     ld = number % 10
#     rev = rev * 10 + ld
#     number //=10
# print(rev)

#armstrong

# 1³ + 5³ + 3³ = 1 + 125 + 27 = 153

# number = 54740
# sum=0
# count=0
# count_num = number
# while(count_num!=0):
#     count_num//=10
#     count +=1

# number_for_sum = number

# while(number_for_sum!=0):

#     ld = number_for_sum % 10
#     sum = sum + ld ** count
#     number_for_sum //=10
# if sum == number:
#     print(f"{number} is a armstrong number")
# else:
#     print(f"{number} is not a armstrong number")

#palindrome

# number = 122
# rev=0
# number_copy = number
# while(number!=0):
#     ld = number % 10
#     rev = rev * 10 + ld
#     number //= 10
# if rev == number_copy:
#     print(number_copy," is palindrome")
# else:
#     print("not")

#program prints all even digits of a number, starting from the rightmost digit (last digit) and moving left.

# number = 123456

# while(number!=0):

#     ld = number % 10
#     if ld % 2 == 0:
#         print(ld)
#     number//=10

"""while loop completed remain for and nest in folder looping_works"""

