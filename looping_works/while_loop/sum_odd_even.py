"""
w.a.p display sum of odd_numbers and sum of even_numbers upto limit 6
"""


limit = int(input("enter number: "))

i = 1

even_sum = 0

odd_sum = 0

while(i<=limit):

    if i % 2 == 0:

        even_sum = even_sum + i
    
    else:

        odd_sum = odd_sum + i

    i = i + 1

print(f"Sum of even numbers upto {limit} is",even_sum)
print(f"Sum of odd numbers upto {limit} is",odd_sum)
