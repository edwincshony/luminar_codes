# shallow copy = create a copy of outer object using copy().
# = points to same memory location

arun_fvt_colors = ["red","green","blue"]

hari_fvt_colors = arun_fvt_colors.copy() # shallow copy

hari_fvt_colors[0] = "purple"

print(arun_fvt_colors) #['red', 'green', 'blue']
print(hari_fvt_colors) #['purple', 'green', 'blue']

print(arun_fvt_colors is hari_fvt_colors) # False bcoz both point to separate objects, True only when both point to same objects