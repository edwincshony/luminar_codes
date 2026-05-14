# 22. Largest and smallest digit in a number

number = 172

largest = float('-inf')
smallest = float('inf')

org_num = number

while(number!=0):

    digit = number % 10

    if digit > largest:

        largest = digit

    if digit < smallest:

        smallest = digit

    number //= 10

print(f"Largest digit in number {org_num} is {largest}")
print(f"Smallest digit in number {org_num} is {smallest}")

