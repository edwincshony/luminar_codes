nums = [10,11,10,11,12,13,14,15,16,15]

# create a new collection that contain recursive numbers

recursive = {n for n in nums if nums.count(n)>1}

print(recursive)

