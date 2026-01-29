"""
153 = 3^3 + 5^3 + 1^3 = 153

"""

number = 54749

number_for_count = number

number_for_last_digit = number

count = 0

sum = 0

while(number_for_count!=0): # 153 != 0 T, 15!=0 T,1!=0T, 0!=0 F

    number_for_count = number_for_count // 10 #153//10=15, #15//10=1, 1//10=0

    count = count + 1 #c=1,2.3

while(number_for_last_digit!=0): #153!=0T

    last_digit = number_for_last_digit % 10 #153%10=3

    sum = sum + last_digit ** count  # 3^3 = 27

    number_for_last_digit = number_for_last_digit // 10 #153//10

print(sum)

if number == sum:

    print("Armstrong number")

else:

    print("Not Armstrong number")


