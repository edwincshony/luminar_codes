nums = [4, 6, 2, 6, 4, 4, 2]

# Step 1: Count frequency manually
freq = {}
for num in nums:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

result = sorted(nums,key=lambda x:(-freq[x],x))
print(result)