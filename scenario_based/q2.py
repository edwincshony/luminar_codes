"""
2. Missing Number in Sequence
A list contains numbers from 1 to n, but one number is missing:
arr = [1, 2, 4, 5, 6]
Task: Find the missing number efficiently (O(n)).
"""
# Approach 1
arr = list(map(int,input().split()))
#arr = [1, 2, 4, 5, 6]
n = len(arr) + 1
# You have 5 numbers
# But one is missing
# ➡️ So total should be 6 numbers (1 to 6)

tot = n*(n+1)//2

num = tot - sum(arr)

print(num)

# Approach 2

# arr = [1, 2, 4, 5, 6]

# arr.sort()

# prev = 0
# next = prev + 1

# if arr[0] != 1:

#     print(1,"is missing")
# else:
#     while(prev<len(arr)-1):

#         diff = arr[next] - arr[prev]

#         if diff != 1:

#             print(arr[prev]+1,"is missing")
#             break

#         prev += 1
#         next = prev + 1
#     else:
#         print(len(arr)+1,"is missing")

