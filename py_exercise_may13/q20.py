# 20. Largest digit in a number

number = 123

largest = float('-inf')

while(number!=0):

    digit = number % 10

    if digit > largest:

        largest = digit

    number //= 10

print(largest)