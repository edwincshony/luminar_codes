from csv import DictReader
fr = open("12.file_operations\\tips_data\\tips.csv")
data = list(DictReader(fr))
print(data)

#male or female give more tip

tip_male = sum([float(t.get("tip")) for t in data if t.get("sex") == "Male"])
tip_female = sum([float(t.get("tip")) for t in data if t.get("sex") == "Female"])

largest = 0

if tip_male > tip_female:

    largest = tip_male

    print("Largest tip given by Males")

else:

    largest  = tip_female

    print("Largest tip given by females")

