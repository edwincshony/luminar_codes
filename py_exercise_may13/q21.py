# 21. Smallest digit in a number

number = 123

smallest = float('inf')

while(number!=0):

    digit = number % 10

    if digit < smallest:

        smallest = digit

    number //= 10

print(smallest)