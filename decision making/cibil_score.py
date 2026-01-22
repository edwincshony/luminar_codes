

cibil_score = int(input("Enter your cibil score: "))

if cibil_score >= 300 and cibil_score < 550:
    print("Poor")
elif cibil_score >= 500 and cibil_score < 650:
    print("average")
elif cibil_score >= 650 and cibil_score < 750:
    print("good")
elif cibil_score >= 750 and cibil_score <= 900:
    print("excellent")
else:
    print("invalid....")