"""
8. Given a tuple of numbers, count how many times a specific number appears.

"""

tup = (1,2,3,4,5,5)

count = 0

try:
    freq_track_num = int(input("Enter the number to track frequency: "))
except ValueError:
    print("Invalid value")
    exit()

for num in tup:

    if num == freq_track_num:

        count += 1

print(f"{freq_track_num} appeared {count} times in tuple")

