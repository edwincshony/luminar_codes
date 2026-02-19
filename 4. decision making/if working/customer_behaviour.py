"""
display unsatisfied if rating < 4.0

display neutral if rating >= 4.0 to <4.5

display satisfied if rating >= 4.0

"""

rating = float(input("enter rating: ")) #5

if rating < 4.0: #5 < 4.0 F
    print("unsatisfied")
elif rating >= 4.0 and rating < 4.5: #5 >= 4.0 T and 5 < 4.5 F 
    print("neutral")
else:
    print("satisfied") 
