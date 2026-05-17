nums = [-4,-2,1,4,8]

closest = nums[0]  # Start with the first number

for num in nums:
    # If current number is closer to 0
    if abs(num) < abs(closest):
        closest = num
    # If equally close, pick the larger one
    elif abs(num) == abs(closest) and num > closest:
        closest = num

print(closest)  # Output: 1