"""
is_last_two_digit_in_range of 10 and 50
"""

number = 100

last_two_digit = number % 100

is_in_range = last_two_digit >= 10 and last_two_digit <= 50

print(is_in_range)