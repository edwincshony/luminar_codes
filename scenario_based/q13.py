# 13. Top K Frequent Elements
# nums = [1,1,1,2,2,3]
# k = 2
# Task: Return the top k most frequent elements.

# Here, k = 2 → you need the top 2 most common elements

# Count frequencies:

# 1 → 3 times
# 2 → 2 times
# 3 → 1 time

# Now rank them (highest first):

# 1 (3 times)
# 2 (2 times)
# 3 (1 time)

nums = [1,1,1,2,2,3]
k = 2

# count frequency
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

# directly get top k
result = sorted(freq, key=freq.get, reverse=True)[:k]
# By setting key=freq.get, you tell Python: "Don't sort the keys alphabetically."
# " Instead, look up the value (frequency) of each key in the freq dictionary, and sort the keys based on those values."
# Setting reverse=True changes the sort order to descending (largest to smallest).
# Setting reverse=False changes the sort order to ascending (smallest to largest).
# This is a list slicing operation. It takes the first k elements from the sorted list.

print(result)
