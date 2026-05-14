# 18. Display number of digits in a number

number = -121

count=0

number = abs(number)

if number == 0:

    count = 1

while(number!=0):

    number//=10
    count += 1

print(count)