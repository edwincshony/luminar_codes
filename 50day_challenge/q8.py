# # Day 8: Odd and Even

# Write a function called `odd_even` that has one parameter and takes a list of numbers as an argument. The function returns the difference between the largest even number in the list and the smallest odd number in the list. For example, if you pass `[1,2,4,6]` as an argument the function should return `6 - 1 = 5`.

def odd_even(arr):

    largest_even = max(n for n in arr if n%2==0)
    smallest_odd = min(n for n in arr if n%2!=0)

    diff = largest_even - smallest_odd

    return diff

print(odd_even([1,2,4,6]))