# 16. Sum of digits of a number

number = 123

tot_sum = 0

while(number!=0):

    digit = number % 10 

    tot_sum += digit

    number //= 10

print(tot_sum)