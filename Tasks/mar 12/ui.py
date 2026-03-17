from csv import DictReader

fr = open("Tasks\\mar 12\\spotify-tracks-dataset.csv",encoding="utf-8")

data = list(DictReader(fr))

"""1. Create a Track Class
Create a class Track with attributes:
track_name
artist
popularity
Create a method display_info() to print track details."""

