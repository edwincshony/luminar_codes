"""
read num 15
display FIZZ if num / by 3
display BUZZ if num / by 5
display FIZZBUZZ if num / by 15
else: invalid
"""

number = int(input("enter num: "))

if number % 15 == 0:
    print("FIZZBUZZ")
elif number % 3 == 0: # if this was wrote as first condition then 15 would print FIZZ, because the program stops at the first true condition.
    print("FIZZ")
elif number % 5 == 0:
    print("BUZZ")
else:
    print("invalid")
