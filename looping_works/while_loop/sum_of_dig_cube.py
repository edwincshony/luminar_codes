number = int(input("enter number: "))

sum = 0

while(number!=0):

    last_digit = number % 10

    # cube_of_last_digit = last_digit ** 3

    sum = sum + last_digit ** 3

    number = number // 10

print(sum)