nums = [2, -1, 1]
closest=nums[0]
for n in nums:

    if abs(n) < abs(closest):
        closest = n
    elif abs(n) == abs(closest) and n>closest:
        closest = n
print(closest)