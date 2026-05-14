"""
👉 For every new interval:

If it touches/overlaps → combine
If it doesn’t → add new
"""

Intervals= [[1,3],[2,6],[8,10],[15,18]]

merged=list()

for i in Intervals:
#👉 Take each interval one by one (i will be [1,3], then [2,6], etc.)
    if not merged or merged[-1][1] < i[0]:
        merged.append(i)
    else:
        merged[-1][1]=max(merged[-1][1],i[1])


print(merged)

