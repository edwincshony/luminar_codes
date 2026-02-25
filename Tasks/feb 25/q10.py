"""
10. Create a list of numbers from 1 to 30 and use list comprehension to create a new list containing numbers divisible by 3 and 5.



"""

lst = [i for i in range(1,31) if i % 5 == 0 and i % 3 == 0]

print(lst)