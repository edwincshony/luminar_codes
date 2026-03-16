from csv import DictReader

fr = open("Tasks\\mar 12\\spotify-tracks-dataset.csv")

data = list(DictReader(fr))

print(data)

