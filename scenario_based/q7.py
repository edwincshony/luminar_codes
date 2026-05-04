"""7. Merge Overlapping Intervals
intervals = [(1,3), (2,6), (8,10), (9,12)]
Task: Merge all overlapping intervals.
"""
intervals = [(1,3), (2,6), (8,10), (9,12)]

intervals.sort(key=lambda x : x[0])

res = [intervals[0]]
for start,end in intervals[1:]:
    last_start,last_end = res[-1]
    if start <= last_end:
        res[-1] = (last_start, max(last_end, end))
    else:
        res.append((start,end))

print(res)

