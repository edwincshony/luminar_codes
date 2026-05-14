# 17. Sum of squares of digits

number = 18

tot_sq_sum = 0

while(number!=0):

    digit = number % 10

    tot_sq_sum += digit**2

    number //= 10

print(tot_sq_sum)