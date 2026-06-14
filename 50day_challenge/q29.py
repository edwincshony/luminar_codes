def middle_figure(a, b):
    combined = (a + b).replace(" ", "")
    
    if len(combined) % 2 == 1:
        return combined[len(combined) // 2]
    else:
        return "no middle figure"

print(middle_figure("make love", "not wars"))