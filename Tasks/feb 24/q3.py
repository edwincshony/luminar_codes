"""
3. Given a list of numbers, print only the even numbers.

"""

lst = [1,2,3,4,5,6,7,8,9,10]

even_nums = []

for num in lst:

    if num % 2 == 0:

        even_nums.append(num)

print(even_nums)