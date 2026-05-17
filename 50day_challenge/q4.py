# # Day 4: Only Floats

# Write a function called `only_floats`, which takes two parameters `a` and `b`, and returns `2` if both arguments are floats, returns `1` if only one argument is a float, and returns `0` if neither argument is a float.

# If you pass `(12.1, 23)` as an argument, your function should return a `1`.

def only_floats(a,b):

    count = 0

    if type(a) == float:

        count += 1

    if type(b) == float:

        count += 1

    return count

print(only_floats(12.1,23))
print(only_floats(12.1, 23.5))   
print(only_floats(12, 23))       